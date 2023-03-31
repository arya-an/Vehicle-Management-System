# **Vehicle-Management-System**
A simple website for _vehicle management_ using **python** and **django**.For the database **SQLite** is used.

This Vehicle Management System includes 2 models
- User model
- Vehicle model

for **User** Model we used the default django user model and created one **vehiclemodel** model
The vehicle model has the following fields
- Vehicle Number (Alpha numeric)
- Vehicle Type (options:- Two, There, Four wheelers)
- Vehicle Model (Text)
- Vehicle Description (Text)

## About the Project
This is a project for management of different types of vehicles.This project will have the CRUD operations for the vehicle model.This includes 3 different types of users and each type of users will different access to the vehicle management.
- Super Admin (will have complete access to the vehicle management.Can perform create,retrieve,update and delete)
- Admin (can perform edit and view operations)
- User (can perform view operation)

## Instructions to download the project

Please follow the below steps to download and run the project

- create a folder in local system 
- open command prompt in that location
- install virtual environment (pip install virtualenv)
- create a virtual environment named **env** (virtalenv env)
- activate the virtual environment (env\Scripts\activate)
- open github in the given link and you can find a option named **code**,under the code option you can find a option name **Download ZIP**.(remember to download the zip from **master** branch)
- on command prompt move to the location of the folder using **cd Vehicle-Management-System-master**
- you can find the requirements in the **requirements.txt** file using **pip install -r requirements.txt**
- now you can migrate the models using the following commands one by one

```bash
python manage.py makemigrations
python manage.py migrate
```
- run the project using 
```bash
python manage.py runserver
```
- copy paste the url **http://127.0.0.1:8000/**
- you can open the link in browser and you can find the login page, if the user is not registered you can register the user using the **register** link.
- register the user using email, username and password. If the user is in **Admin** Category then please don't forget to select the **Staff status**.If the user is in **SuperAdmin** Category then please don't forget to select the **Superuser status**.
- you can login using the username and password.
