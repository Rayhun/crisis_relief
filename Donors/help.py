import requests


def get_latlng_from_address(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "Donors/1.0 (localhost)"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data:
            return {
                "lat": data[0]["lat"],
                "lon": data[0]["lon"],
                "display_name": data[0]["display_name"]
            }
        return {"error": "No result found"}
    except requests.RequestException as e:
        return {"error": str(e)}
