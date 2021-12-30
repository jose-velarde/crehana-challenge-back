# Challenge

https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cb4a988c-f014-4156-a3ef-389d5dbd0fda/Reto_Crehana.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211020T130913Z&X-Amz-Expires=86400&X-Amz-Signature=b13c5c44d7433c5e680e0a56252ed8f24dc024410bf00d05f6fa2805bc906499&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Reto_Crehana.pdf%22

# Setup

Config local env and install dependencies
```bash
py -m venv venv
.\venv\Scripts\activate
pip install black
pip install django
pip install psycopg2
pip install sqlalchemy
```
Start django project and app
```bash
django-admin startproject core .
py manage.py startapp crehana_store
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```
Fix cors error
https://dzone.com/articles/how-to-fix-django-cors-error
```bash 
pip install django-cors-headers
```

# Deploying to Heroku

https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Deployment

* create Procfile with projectname.wsgi (core.wsgi)
* create Procfile.windows: web: python manage.py runserver

Install heroku dependencies and env variable package 
```bash
pip install django-heroku
pip install gunicorn 
pip install dj-database-url
pip install whitenoise
pip install django-environ
```
secret key as env variable
https://medium.com/@natmakesthings/hiding-secret-key-in-django-deployment-on-heroku-59b9640819a

*check that .env is utf-8

After sucessful deploy to heroku:
Delete local migrations if there are database errors
```bash
heroku local:run python manage.py makemigrations
heroku local:run python manage.py migrate
git push heroku master
```
Migrate on heroku
```bash
heroku run python manage.py migrate
heroku run python load_courses.py
```
