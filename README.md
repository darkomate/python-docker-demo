# Python Docker Demo
Python Docker Demo is used with the bare essentials for a Python Docker project.

This will build a webserver in Python and display a simple message.
````bash
docker build -t --python-docker-demo:1.0.0 .
````

To run the Docker build image.
````bash
docker run -d -p 8003:8003 python-docker-demo:1.0.0
````
