# shall_we_meet_app
Web app that helps to finally figure out perfect time and place for all friends to meet.

## Getting Started

Install dependencies to your virtualenv, using requirements.txt

```
pip install -r requirements.txt
```

Create new database in PostgreSQL.

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



### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

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

* [Django](https://www.djangoproject.com/)  - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* Bootstrap4
* PostgreSQL - Used to generate relational databases

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Author

[ZuzannaP](https://github.com/ZuzannaP)

## License

This project is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE - see the [LICENSE.md](https://github.com/ZuzannaP/shall_we_meet_app/blob/master/LICENSE) file for details

