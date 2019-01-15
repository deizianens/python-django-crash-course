# Python Django Crash Course

Available at: https://www.youtube.com/watch?v=D6esTdOLXh4

## On Windows:
Create a virtual environment:
> mkvirtualenv [name]

Use a virtual environment:
> workon [name]

Installing Django:
> pip install Django

To start a project:
> django-admin startproject [name_of_project]

Enter project folder. Work on it!

### Using MySQL instead of sqlite3
Install Mysql Client (for me on Python 3.7, downloaded wheel at: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient):
> pip install mysqlclient-1.3.13-cp37-cp37m-win32.whl

Change setting.py database and run migrate:
> python manage.py migrate

## Some other commands
Create super user (after that, write the password - at least 8 characters):
> python manage.py createsuperuser --user=[user] --email=[email]

Create an app:
> python manage.py startapp [name_of_app]
After creating an app, it has to be added to setting.py INSTALLED_APPS and to urls.py urlpatterns using "include" command (include has to be imported).
