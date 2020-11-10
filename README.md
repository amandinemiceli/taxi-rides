# taxi-rides

This Flask Api/Vue.js application gives an overview of taxi rides with their costs.

### Installation
##### Before you start

Before getting started, you should have the following installed and running:

- npm
- Vue Cli 4
- Python 3.9

##### Dependencies

1 . Clone this repository:

```
$ git clone https://github.com/amandinemiceli/taxi-rides.git
```
 
2 . Setup virtual environment, install dependencies, and activate it:

```
$ cd taxi-rides  
$ python3 -m venv . 
$ source bin/activate
```
   
3 . Install JS dependencies

```
$ cd client
$ npm install
```

## Development Server

1 . Start the Flask Api server-side application:

```
$ cd api
$ python app.py
```

It will be served from **localhost:5000**.


2 . In a different terminal window, start the Vue.js client-side server:

```
$ cd client
$ npm run serve
```

It will be served from **localhost:8080**.
