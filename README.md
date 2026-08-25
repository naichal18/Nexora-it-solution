# Nexora IT Solution

A Django website for an IT solution and training business. The site includes pages for services, gallery, blog, contact, and login.

## Features

- Django backend
- Login page
- Services, gallery, blog, and contact pages
- SQLite database for local development
- Static CSS and image assets

## Run Locally

1. Clone the repository and open the project directory:

   ```powershell
   cd myfirstproject1
   ```

2. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Start the development server:

   ```powershell
   python manage.py runserver
   ```

4. Open http://127.0.0.1:8000/ in a browser.

## Demo Login

The current demonstration login is:

- Username: `admin`
- Password: `123`

Replace this hardcoded login with Django authentication before using the site in production.

## Deployment

The project can be deployed on Render with:

```text
Build command: pip install -r requirements.txt && python manage.py collectstatic --no-input
Start command: gunicorn myfirstproject.wsgi:application
```

Set these environment variables in the hosting provider:

```text
DEBUG=False
SECRET_KEY=<your-private-secret-key>
ALLOWED_HOSTS=<your-hostname>
```

Do not commit private keys, passwords, or user data to the repository.