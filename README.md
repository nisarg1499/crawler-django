# crawler-django 

## Environment Setup
1. Create virtual environemt using `python3 -m venv venv` command
2. Activate command using `source venv/bin/activate`
3. Install requirements.txt file using `pip3 install -r requirements.txt`

Database is : PostgreSQL
Steps to configure postgresql
1. Install PostregSQL
2. Create user using command : `CREATE USER crawler WITH SUPERUSER PASSWORD 'password';`
3. Then login with the created user : `psql -U crawler -d postgres;`
4. Create database : `CREATE DATABASE medium;`

Keep the values same as this are configured in settings.py file of django

Now you are all set, run the commands `python3 manage.py makemigrations` -> `python3 manage.py migrate` -> `python3 manage.py runserver`. Just make sure you are in the main folder of django project. 