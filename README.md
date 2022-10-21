# Django-api-star-wars

#### Github:
<https://github.com/ja95aricapa/Django-api-star-wars>

#### Postman:
<https://www.getpostman.com/collections/b5c4b7f4033c2b695d08>

#### SWAPI:
<https://swapi.dev/>

#### Description:
Django-api-star-wars is an API created to create, get, edit and delete records related to the Star Wars saga. Mainly powered by Star Wars API (SWAPI)

#### Environment:
This project is interpreted/tested on Ubuntu 22 LTS using python3.9

#### Installation:
* Clone this repository: `git@github.com:ja95aricapa/Django-api-star-wars.git"`
* Access Postigram: `cd Django-api-star-wars`
* Activate virtualenv: `source venv/bin/activate`
* Activate local server: `python3 manage.py runserver`
* Open the web app in a browser: `http://127.0.0.1:8000/`

#### Authentication:
The endpoint for creating tokens is called "api-token-auth".

Receive a body parameter like the following:

{
  "username": "string",
  "password": "string"
}

Currently, you can use:

{
  "username": "admin",
  "password": "admin"
}

#### Examples of use:
interact with the API using Postman, remember to use the token in the header of the request.

#### Bugs:
No known bugs at this time.

#### Authors:
Jaime Aricapa - [Github](https://github.com/ja95aricapa)

#### License:
Public Domain. No copy write protection.