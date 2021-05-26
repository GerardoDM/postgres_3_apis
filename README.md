# postgres_3_apis
Creación de 3 APIS, con 3 diferentes framework (laravel, AdonisJS, y Flask), conectados a PostgreSQL

Instrucciones

1. Crear bd vacía en PostgreSQL

<h2>Flask</h2>

1. Acceder a consola dentro de proyecto e instalar Flask, SQLAlchemy y Flask-Migrate

$ pip install flask
<br>
$ pip install psycopg2-binary
<br>
$ pip install flask-sqlalchemy
<br>
$ pip install Flask-Migrate

2. Cambiar credenciales en linea 8

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/demodb"

3. Correr siguientes comandos

$ export FLASK_APP=app.py
<br>
$ flask run
<br>
<br>
$ flask db init
<br>
$ flask db migrate
<br>
$ flask db upgrade

Con esto podremos ver nuestro modelo en la base de datos vacía.

<h2>Laravel</h2>

1. Levantar servidor con comando "php artisan serve"

<h2>Adonis</h2>

1. Levantar servidor con comando "adonis serve --dev"

<h2>Insomnia/Postman</h2>

1. Hacer una petición POST con cuerpo de JSON a la ruta "http://127.0.0.1:5000/robots"

"id" : numero,
<br>
"nombre" : "string" 

2. Hacer 3 requests con método GET

http://127.0.0.1:5000/robots (Flask)
<br>
http://127.0.0.1:8000/api/robots (Laravel)
<br>
http://127.0.0.1:3333/robots (Adonis)


