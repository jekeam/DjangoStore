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
   cd DjangoStore/store/
   ```

   ```bash
   python3.9 -m venv ../venv
   ```

   ```bash
   source ../venv/bin/activate
   ```   
3. Install packages:
   ```bash
   pip install --upgrade pip
   ```
   ```bash
   pip install -r requirements.txt
   ```
   
4. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   ./manage.py migrate
   ```
   ```bash   
   ./manage.py loaddata <path_to_fixture_files>
   ```
   ```bash
   ./manage.py runserver 
   ```
   
5. Run [Redis Server](https://redis.io/docs/getting-started/installation/):
   ```bash
   redis-server
   ```
   
6. Run Celery:
   ```bash
   celery -A store worker --loglevel=INFO
   ```
