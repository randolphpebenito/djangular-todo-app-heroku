# Overview

A simple RESTFUL API (CRUD functionality) using Django/Django Rest Framework. This repository is intended for the backend of any Todo application.

## Demo API via cURL
CRUD functionality: 
```sh
#Create Todo
$ curl -v -XPOST -H "Content-Type: application/json" -d '{"title": "This is my task.", "note": "This is a note"}' http://intellij-todo-randolph.herokuapp.com/api/todo  
#Delete Todo
$ curl -v -XDELETE http://intellij-todo-randolph.herokuapp.com/api/todo/<id>
#List All Todo
$ curl -v -XGET http://intellij-todo-randolph.herokuapp.com/api/todo
#Update Todo
$ curl -v -XPATCH -H "Content-Type: application/json" -d '{"title": "This is my updated task.", "note": "Updated note", "completed": true}' http://intellij-todo-randolph.herokuapp.com/api/todo/<id>

```

## Quickstart

### Running Locally

```sh
$ git clone https://github.com/randolphpebenito/simple-hacker-new-clone.git
$ cd simple-hacker-new-clone
$ virtualenv <venv name>
$ source <venv name>/bin/activate
$ pip install -r requirements.txt
$ ./manage.py test #Run the tests
$ ./manage.py collectstatic

Via Heroku
$ heroku local

Via Django’s built in web server
$ ./manage.py runserver
```

Your app should now be running on [localhost:5000](http://localhost:5000/). or [localhost:8000](http://localhost:8000/)

### Deploying to Heroku

```sh
$ heroku create #Run this if first time to deploy
$ fab deploy_to_heroku
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
