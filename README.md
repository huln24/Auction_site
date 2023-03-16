# Commerce

## CS50 Web: Project 2

An eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

### Getting Started

Install Django

```
pip3 install Django
```

Create Django project

```
django-admin startproject PROJECT_NAME
```

Files created:

- manage.py (executable file - to execute commands on the Django project)
- settings.py (contains important configuration settings for Django app - can modify settings to add features to the app)
- urls.py (table of contents for the app - contain all the urls of the app)

Each project can consist of multiple apps which are separate services within the website

Create app

```
python manage.py startapp APP_NAME
```

Files created:

- views.py (To describe what user sees when the visit a particular route/page - rendering of pages)
  Example:

```
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world!")
```

To Install the app

1. Go to Project folder
2. Go to settings.py -> INSTALLED_APPS = [...]
3. Add `'APP_NAME'`

Make migrations for the app

```
python manage.py makemigrations APP_NAME
```

Apply migrations to the database

```
python manage.py migrate
```

Run server

```
python manage.py runserver
```
