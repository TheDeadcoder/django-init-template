# Running the Backend

## Virtual environment
Make a python virtual environment with the following command:
```bash
python3 -m venv .venv
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
