## Instagram
 -Web clone of the Instagram app
 -June 15th, 2018
 -By Richard Waweru
## Description
 -This is a simple web clone of the instagram website. A user can create an account and sign into it. The site supports uploading images, and following other users. users can view photos uploaded by other users in the home page of app.

## Specifications
 - Find the specs here

## Set Up and Installations
## Prerequisites
 - Ubuntu Software
 - Python3.6
 - Postgres
 - python virtualenv
 - Clone the Repo
 - Run the following command on the terminal: git clone https://github.com/DevWaweru/Instagram.git && cd Instagram

 - Activate virtual environment
 - Activate virtual environment using python3.6 as default handler

 - virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
## Install dependancies
- Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

 - Create the Database
 - psql
 - CREATE DATABASE insta;
.- env file
 - Create .env file and paste paste the following filling where appropriate:

 - SECRET_KEY = '<Secret_key>'
 - DBNAME = 'insta'
 - USER = '<Username>'
 -PASSWORD = '<password>'
 - DEBUG = True

 - EMAIL_USE_TLS = True
 - EMAIL_HOST = 'smtp.gmail.com'
 - EMAIL_PORT = 587
 - EMAIL_HOST_USER = '<your-email>'
 - EMAIL_HOST_PASSWORD = '<your-password>'
 - Run initial Migration
 - python3.6 manage.py makemigrations gram
 - python3.6 manage.py migrate
##Run the app
 - python3.6 manage.py runserver
 - Open terminal on localhost:8000

## Known bugs
 - Like and Follow functionality do not work

## Technologies used
  - Python 3.6
  - HTML
  - Bootstrap 4
  - JavaScript
  - Heroku
  - Postgresql
## Support and contact details
  - Contact me on petermbaik@gmail.com for any comments, reviews or advice.

## License
  - Copyright (c) Peter Mbai Kuria  
