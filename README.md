# SSOT Backend - backend for [SSOT app](https://github.com/rafal-rybicki/ssot)

# Installation guide 
***(for development environment)***
1. Clone the repository: `git clone`
2. Install the required packages: `pip install -r requirements.txt`
3. Create **.env** file: `cp .env.example .env`
4. Go into the `server/` directory: `cd server/`
5. Run migrations: `python manage.py migrate`
6. Generate random data: `python manage.py load_factories`(or `python manage.py seed_admin` only for admin user)
7. Run the server: `python manage.py runserver 0.0.0.0:8000`
