# Python Django Crash Course

Available at: https://www.youtube.com/watch?v=D6esTdOLXh4

## On Windows:
Creating a virtual environment:
> mkvirtualenv [name]

Using a virtual environment:
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
