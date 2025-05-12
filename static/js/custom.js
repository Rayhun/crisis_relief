    // Initialize the map centered on Albania
    var map = L.map('map').setView([41.1533, 20.1683], 7.7);
    
    // Add OpenStreetMap tiles with a grayscale filter for non-Albania areas
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        className: 'albania-focused-map'
    }).addTo(map);

    // Set Albania bounds
    var southWest = L.latLng(39.1, 18.9),
        northEast = L.latLng(42.9, 21.3);
    var bounds = L.latLngBounds(southWest, northEast);
    
    // Restrict view to Albania
    map.setMaxBounds(bounds);
    map.on('drag', function() {
        map.panInsideBounds(bounds, { animate: false });
    });

    const manualUrl = window.location.protocol + "//" + window.location.host;

    // Add Albania's precise boundary (using GeoJSON)
    var geojson = manualUrl + '/static/js/alb.geo.json'
    fetch(geojson)
        .then(response => response.json())
        .then(data => {
            // Highlight Albania with a colored border
            L.geoJSON(data, {
                style: {
                    color: '#3388ff',  // Border color
                    weight: 2,         // Border width
                    fillColor: '#3388ff', // Fill color
                    fillOpacity: 0.1   // Fill opacity
                }
            }).addTo(map);
        });

    // add red circle for Flood and blue circle for Earthquake
    var earthquakeCircle = L.circle([41.3275, 19.8187], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: 7.99
    }).addTo(map).bindPopup("Earthquake Area");

    // Add number of people affected
    var floodAffected = 1000;
    var floodPopup = L.popup()
        .setLatLng([41.3275, 19.8187])
        .setContent("Flood Affected: " + floodAffected)
        .openOn(map);


    // add another circle for another location in Albania
    var floodCircle = L.circle([41.5675, 20.4687], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: 25000
    }).addTo(map).bindPopup("Flood Area");
    // Add number of people affected
    var earthquakeAffected = 500;
    var earthquakePopup = L.popup()
        .setLatLng([41.3275, 19.8187])
        .setContent("Earthquake Affected: " + earthquakeAffected)
        .openOn(map);

    
    // Show Bootstrap modal on map click with lat/lng
    map.on('click', function(e) {
        var lat = e.latlng.lat.toFixed(5);
        var lng = e.latlng.lng.toFixed(5);
    
        // Show loading text
        var modalBody = document.getElementById('latLngModalBody');
        modalBody.innerHTML = `<strong>Latitude:</strong> ${lat}<br><strong>Longitude:</strong> ${lng}<br><em>Fetching address...</em>`;
    
        var latLngModal = new bootstrap.Modal(document.getElementById('latLngModal'));
        latLngModal.show();
    
        // Fetch address using reverse geocoding
        fetch(`https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lng}&format=json`)
            .then(response => response.json())
            .then(data => {
                const address = data.display_name || "Address not found";
    
                modalBody.innerHTML = `
                    <strong>Latitude:</strong> ${lat}<br>
                    <strong>Longitude:</strong> ${lng}<br>
                    <strong>Address:</strong><br>${address}
                `;
            })
            .catch(error => {
                modalBody.innerHTML += `<br><em>Address lookup failed.</em>`;
                console.error("Reverse geocoding error:", error);
            });
    });
    
