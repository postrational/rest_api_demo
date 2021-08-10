FROM python:3.9.6

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
RUN python setup.py install

EXPOSE 8888
CMD ["python", "/app/rest_api_demo/app.py"]