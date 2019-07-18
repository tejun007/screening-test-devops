# Docker for server
FROM python:3.6.5
MAINTAINER tejunlee007@gmail.com

# working directory
WORKDIR /backend

# copy current directory to /server in docker container
ADD ./ /backend

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 5000 for the Flask app to run on
EXPOSE 5000

# execute the Flask app
CMD python -u run.py
