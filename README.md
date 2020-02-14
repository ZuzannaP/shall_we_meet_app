# shall_we_meet_app
Web app that helps to finally figure out perfect time and place for all friends to meet.

## How does it work?

1. You create event, invite guests and propose a few time slots for the meeting
2. App shows you the area where all your guests reside, so that you can find a meeting spot convenient to all
![alt text](shall_we_meet/perfect_slot/static/img/choose_meeting_location_view.png
 "Photo finding location")
3. Your guests vote for each time slot
4. When most of them voted, you see the results and which time slot is preferred amongst your guests
![alt text](shall_we_meet/perfect_slot/static/img/organizers_detailed_event_view.png
 "Photo finding location")
5. You finalize the meeting by choosing winning time slot
6. Your guests see meeting details plus a map with location, so they won't be lost :)

## How to get it up and running

### Before you start

Create virtualenv

If you don't have the below installed, install them:

[Install PostgreSQL and create a user](https://www.postgresql.org/download/)

[Install PostGIS](https://postgis.net/install/)

[Install QGIS](https://www.qgis.org/en/site/forusers/alldownloads.html)


### Getting Started

Install dependencies to your virtualenv, using requirements.txt

```
pip install -r requirements.txt
```

Create new database in PostgreSQL

Create new .py file in shall_we_meet/shall_we_meet folder and name it local_settings.py

Paste there the below:

```
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '',
        'HOST': '',
        'PASSWORD': '',
        'USER': '',
    }
}

```
Fill in missing parameteres with your secret key and your database credentials.

#### Add PostGIS extention to PostgreSQL

Open psql
```
sudo -u postgres psql
```
Connect to your PostgreSQL database

```
postgres=# \c DATABASE_NAME
```

Run the following

```
CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;
```

Exit from psql


#### Installing

While in directory:

```
shall_we_meet/perfect_slot
```

Run migrations:

```
python3 manage.py migrate
```
Run server

```
python3 manage.py runserver
```

## Built With

* [Python 3.6](https://www.python.org/)
* [Django 3.0](https://www.djangoproject.com/)  - high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) - lets you control the rendering behavior of your Django forms in a very elegant and DRY way 
* [django-tempus-dominus](https://pypi.org/project/django-tempus-dominus/) - Django widget for the Tempus Dominus Bootstrap 4 DateTime picker
* [Bootstrap4](https://getbootstrap.com/) - open source toolkit for developing with HTML, CSS, and JS.
* [PostgreSQL](https://www.postgresql.org/) -  open source object-relational database system
* [PostGIS](https://postgis.net/) - spatial database extender for PostgreSQL object-relational database.
* [Leaflet 1.6](https://leafletjs.com/) - leading open-source JavaScript library for mobile-friendly interactive maps

## Author

[ZuzannaP](https://github.com/ZuzannaP)

## License

This project is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE - see the [LICENSE.md](https://github.com/ZuzannaP/shall_we_meet_app/blob/master/LICENSE) file for details

