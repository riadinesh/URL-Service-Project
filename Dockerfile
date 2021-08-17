# syntax=docker/dockerfile:1

# public image used to create own image
FROM python:3.8-slim-buster

# sets the working directory
WORKDIR /app

#copies the req file with the dependencies to the new image url_lookup
COPY requirements.txt requirements.txt

# runs/installs the dependences 
RUN pip3 install -r requirements.txt

# copies everything in current directory into the new image url_lookup
COPY . /app
# tells Docker what command to run to execute image
ENTRYPOINT ["python"]

# tells Docker what command to run to execute image
CMD ["url_lookup.py"]


