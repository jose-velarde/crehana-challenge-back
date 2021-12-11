# Challenge

https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cb4a988c-f014-4156-a3ef-389d5dbd0fda/Reto_Crehana.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211020T130913Z&X-Amz-Expires=86400&X-Amz-Signature=b13c5c44d7433c5e680e0a56252ed8f24dc024410bf00d05f6fa2805bc906499&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Reto_Crehana.pdf%22

# Setup
py -m venv venv
.\venv\Scripts\activate
pip install django
pip install psycopg2

django-admin startproject core .
py manage.py startapp crehana_store
pip install black
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver