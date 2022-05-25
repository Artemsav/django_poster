# Django poster

## Project description

The project of an interactive map of Moscow, which will mark the places of active recreation with detailed descriptions and comments.

![Example of project](image/ezgif.com-gif-maker_4nWhtfQ.gif)

You can find the project on [pythonanywhere.com](http://hisp.pythonanywhere.com)

## How to get admin panel

Create new user with admin permission:

```bash
$ python3 manage.py createsuperuser
```

Run the server:

```bash
$ python3 manage.py runserver
```

Go to via link [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).


## Instalation

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

Make migration:

```bash
python3 manage.py migrate
```

Run the server:

```bash
python3 manage.py runserver
```

## Enviroment variables

`SECRET_KEY` — secret key `Django`

`DEBUG` — debug mode, default `False`

`ALLOWED_HOSTS` — one or several hosts separeted by comma. [Documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

## Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org)
