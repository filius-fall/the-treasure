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



### Run the app

--------------------

To run the app make sure you are in the main directory 

```
$ python3 run.py
```

