Here's the updated `README.md` file based on your project structure:

```markdown
# 🌍 CrisisReliefApp

**CrisisReliefApp** is a Django-based platform designed to assist with organizing and delivering aid to individuals affected by crises. It supports multiple modules like Donors, Affected Individuals, and Task Management. This document guides you through setting up and running the project locally.

```

## 📁 Project Structure

```plaintext
CrisisReliefApp/
├── Affected/               # App for managing affected individuals
├── Donors/                 # App for donor management
├── Task/                   # Task assignment and tracking
├── core/                   # Common utilities or base configurations
├── crisis_relief/          # Main Django project settings
├── templates/              # HTML templates for rendering views
├── static/                 # Static files (CSS, JS, images)
├── media/                  # Media files (uploads)
├── example/
│   └── env                 # Sample .env file (copy this to root)
├── .env                    # Environment variables (create this file)
├── db.sqlite3              # SQLite database file
├── manage.py               # Django's command-line utility
├── requirements.txt        # Python dependencies
├── utils.py                # Project utility functions
├── .gitignore              # Git ignored files
└── venv/                   # Virtual environment (excluded from version control)


````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Rayhun/crisis_relief.git CrisisReliefApp
cd CrisisReliefApp
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install project dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Configuration

### 4. Set up environment variables

Copy the sample `.env` file from `example/` to the root directory:

```bash
cp example/env .env
```

Then edit the `.env` file to add your sensitive keys like email credentials:

```env

STRIPE_SECRET_KEY=
STRIPE_PUBLISHABLE_KEY=
STRIPE_WEBHOOK_SECRET=

# SMTP
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

> ✅ Use an [App Password](https://support.google.com/accounts/answer/185833) if 2FA is enabled.

---

## 🛠️ Database & Migrations

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

---

## 🧪 Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🧪 Run Tests

```bash
python manage.py test
```

---

## 🖼️ Admin Panel

After creating the superuser, you can access the Django admin panel at:

```
http://127.0.0.1:8000/admin/
```

---

## 📌 Notes

* All HTML templates should be placed in the `templates/` directory.
* Static files (like custom CSS and JS) go under the `static/` directory.
* Uploaded media (images, documents) will be stored in the `media/` folder.
* Utility functions can be added to `utils.py`.

