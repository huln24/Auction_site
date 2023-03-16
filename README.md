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
