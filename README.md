# Twitter Miner #

## Disclaimer ##

_This API was created for experimenting and portfolio only, checkout the [INSTRUCTIONS.md](./docs/INSTRUCTIONS.md)_

_There are some features who still need to be implemented: you can check it out [here](https://github.com/Lorensov/twitter-miner/issues)_

## Description ##

The application is a conjuction between an Interface to serve a Twitter Mining Job which will return a dataset limited by a 100 tweets filtered by "bieber" keyword. [future parameterization will be implemented here](https://github.com/Lorensov/twitter-miner/issues/26)

You can manipulate and access the mining job through the diverse routes.
This API is powered by [Swagger](https://swagger.io/)
_With the application running you can access it (for example on [localhost/swagger/](http://localhost:5000/swagger/))_

Please read the following instructions carefully and make sure that you fulfill all the requirements listed.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Running with Docker-compose

* Create on the project root directory your `.env` file according to the `template.env`

* Run the command below on the project root directory :

```
docker-compose up
```


## Running on your local machine ##

### Prerequisites

What things you need to install the software and how to install them

* You'll need Python3 and `pip install` command;
* You'll need to be capable of running [Bjoern](https://github.com/jonashaag/bjoern/wiki/Installation)
  * _obs: Checkout first the installation method and requirements!_
* Also you will need a MongoDB to persist


### Installing


1. Run the command below:

```
pip install -r requirements.txt
```

2. Start a `Mongod` service or change the MONGODB variables

```
sudo service mongod start
```

* _You can check it using the command `mongo` to interact with the database_

## Running

Fulfilling the Installing steps

* Start the API from the project root directory

```
python api/app_server.py
```

# List of routes

_obs: remember to put the IP address before the route (e.x. [http://localhost:5000/healthcheck](http://localhost:5000/healthcheck/)) )_

* `/healthcheck`
  * Route to check if the API is online.

* `/trigger`
  * Route to trigger the Twitter Mining Job.

* `/status`
  * Route to check the status of the Twitter Mining Job

* `/stop`
  * Route to stop the Twitter Mining Job

* `/download`
  * Route to download the *output.tsv* created from the Job.

## Extras

There's also a folder called `notebooks` where you can use [Jupyter Notebook](https://jupyter.org/) and see the step-by-step of the Twitter Mining Job.

## Built With

* [Python 3](https://www.python.org/) - Main programming language used for this application
* [Bjoern](https://github.com/jonashaag/bjoern/wiki/Installation) - used Web Server to contain the Flask Application
* [Swagger](https://swagger.io/) - Live Documentation framework
* [Docker](https://www.docker.com/) - "Enterprise Container Platform for High-Velocity Innovation"
* [Jupyter Notebook](https://jupyter.org/) - "An open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text."
* [MongoDB](https://www.mongodb.com/) - "A cross-platform document-oriented database program."

## Authors

* **Lucian Lorens** - [Lorensov](https://github.com/Lorensov)

## References ##

* [README.md example](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [Gitmoji commits pattern](https://gitmoji.carloscuesta.me/)

## Acknowledgments
* Gratitude for my family and friends who always are there supporting and caring;
* Great thanks to the awesome team [".zip Team"](https://github.com/equipepontozip/) working with me;
* And [Helio](https://github.com/hmajr) who was there on the most difficult moments cheering me up.