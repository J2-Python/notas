### instalar django y DRF
```
pip install django
pip install djangorestframework
```
### instalar driver de postgres
```
pip install psycopg2
```

### Crear usuario y BD
````
psql -U postgres
postgres=# CREATE DATABASE notasdb;
postgres=# CREATE USER notasdbadmin;
postgres=# \c notasdb;
You are now connected to database "notasdb" as user "postgres".
notasdb=# ALTER USER notasdbadmin WITH password 'notasdbadmin123';
notasdb=# \c postgres
You are now connected to database "postgres" as user "jota".
postgres=# ALTER DATABASE notasdb OWNER TO notasdbadmin;
````

### crear superuser
```
python3 manage.py createsuperuser
email: admin@gmail.com
password: notasdbadmin123
```

### Instalar JWT
```
pip install djangorestframework-simplejwt
```