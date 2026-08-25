# Nexora IT Solution

A Django website for an IT solution and training business. The site includes pages for services, gallery, blog, contact, and login.

## Features

- Django backend
- Login page
- Services, gallery, blog, and contact pages
- SQLite database for local development, with PostgreSQL support for production
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

## Create a Login User

Create a Django user locally with:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

Use the username and password you create at `/login/`. Do not commit credentials to GitHub.

## Deployment

The project can be deployed on Render with:

```text
Build command: pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
Start command: gunicorn myfirstproject.wsgi:application
```

Set these environment variables in the hosting provider:

```text
DEBUG=False
SECRET_KEY=<your-private-secret-key>
ALLOWED_HOSTS=<your-hostname>
DATABASE_URL=<your-postgresql-connection-string>
```

Do not commit private keys, passwords, or user data to the repository.