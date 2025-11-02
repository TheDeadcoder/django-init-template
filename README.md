# Running the Backend
![Django-supabase Logo](https://egtitleeeenycwyhbpik.supabase.co/storage/v1/object/public/statics/django_supabase.png)
## Virtual environment
Make a python virtual environment with the following command:
```bash
python3 -m venv .venv
```
Activate the virtual environment
```bash
source .venv/bin/activate
```

## Install dependencies
Install the required packages with the following command:
```bash
pip install -r requirements.txt
```

## Required Environment variables
- DEFAULT_DB_NAME=''
- DEFAULT_DB_USER=''
- DEFAULT_DB_PASSWORD=''
- DEFAULT_DB_HOST=''
- DEFAULT_DB_PORT=''
- SUPABASE_URL=''
- SUPABASE_KEY=''
- APP_SECRET_KEY=''
- ALLOWED_HOSTS='localhost:8000,127.0.0.1,your-frontend-url'

## Start the first migration
At first, create a superuser, (remember the pass you are giving)
```bash
python manage.py createsuperuser
```
Then create and make the migration
```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the backend
To run the backend server, use the following command:
```bash
python manage.py runserver
```

## Access the swagger API docs at
```bash
http://127.0.0.1:8000/swagger/
```


