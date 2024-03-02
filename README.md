# Store Server

The project for study Django.

#### Stack:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.9 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Install PostgreSQL, create user and databse:
   ```bash
   sudo apt-get update
   ```
   ```bash
   sudo apt-get install postgresql postgresql-contrib
   ```
   ```bash
   sudo service postgresql start
   ```
   ```bash
   sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'admin';"
   ```
   ```bash
   sudo -u postgres createdb store
   ```
   
5. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   python ./manage.py migrate
   ```
   ```bash
   python ./manage.py loaddata <path_to_fixture_files>
   ```
   ```bash
   python ./manage.py runserver 
   ```
   
6. Run [Redis Server](https://redis.io/docs/getting-started/installation/):
   ```bash
   redis-server
   ```
   
7. Run Celery:
   ```bash
   celery -A store worker --loglevel=INFO
   ```
