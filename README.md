# rest_api_demo

This repository contains boilerplate code for a RESTful API based on Flask and Flask-RESTPlus.

The code of this demo app is described in an article on my blog:
<http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/>

## Quick Start

```bash
docker stop rest-api-demo
docker rm rest-api-demo
docker run -d -p 9999:8888 --name=rest-api-demo maodouzi/rest-api-demo:3.9.6
```

Open the URL <http://localhost:9999/api/>

## Development

Create a virtual Python environment in a directory named venv, activate the virtualenv and install required dependencies using pip:

```console
$ virtualenv -p `which python3` venv
$ source venv/bin/activate

(venv) $ pip install -r requirements.txt
Now let’s set up the app for development and start it:

(venv) $ python setup.py develop
(venv) $ python rest_api_demo/app.py
```

OK, everything should be ready. In your browser, open the URL <http://localhost:8888/api/>

## Build Image

```bash
docker build --tag=maodouzi/rest-api-demo:3.9.6 .
```
