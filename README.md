## The Treasure

----------------------



### Description

This application will have individually working containers each container will have its own feature and its own api.

The main features will be we will be able to add data to this sites containers from 

1. Linux Shell
2. Discord Bot





##### Disclaimer 

-----------------

This app is still under development and I am still learning some things like how to use API's with Flask and some things so some of the code will be irrelevant.



At current I am trying to learn login and logout features and using redis with Flask "app" package is for that

and "api_app" is learning and implementing API's in Flask and will integrate them future



### Installation

1. If you are using Linux there is a high chance python will be pre-installed into your system

To check for python version do this.

```
$ python3 --versrion
```

If you dont have python install it 

```
$ sudo apt-get update
$ sudo apt-get install python3.6
```

2. Install virtual environment

```
$ python3 -m pip install --user virtualenv
```

3. Create Virtualenv

```
$ python3 -m venv <name-of-your-venv>
```

4. Activate Venv

```
$ source env/bin/activate
```

5. Install required packages using requirements.txt

```
$ pip install -r requirements.txt
```

6. Install Redis

```
$ pip install redis
```



## Prerequisites

1. Run Redis-server in the background.

```
$ redis-server
```



### Run the app

--------------------

To run the app make sure you are in the main directory 

```
$ python3 run.py
```



## Usage

------------------------------

For now this app has two API's, one for publishing all data and other for adding data to redis

Primary API 

```
< IP-Address you are running server on >/api/v2/til_page
```

This has "password" Param, this acts as authentication key which you can set in .env file when the given param matches with your env only the site accepts requests

You have to POST the data in json format and should be in format

```
{"title":"Your title here","url":"Your url here","descryption":"Your descryption here"}
```

Remember the double quotes. You have to send data in above format using POST method



For testing you can use "Postman" believe me it save you time
