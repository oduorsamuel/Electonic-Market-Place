
# AWS EC2 PRODUCTION SETUP

- [x] sudo apt-get update && sudo apt-get upgrade -y

# INSTALL PYTHON
- [x] sudo apt install build-essential checkinstall //dependencies
- [x] sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev //dependencies

# DOWNLOAD ZIP FILE AND MANUALLY INSTALL

- [x] cd /opt && sudo wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tar.xz
- [x] sudo tar -xvf Python-3.7.9.tar.xz
- [x] cd Python-3.7.9/
- [x] sudo ./configure
- [x] sudo make && sudo make install
- [x] cd /home/ubuntu/

# CREATE DJANGO APP

- [x] mkdir hello_django && cd hello_django
- [x] git clone https://github.com/oduorsamuel/python_init.git

#ACTIVATE VIRTUAL ENV
- [x] python3.6 -m venv .
- [x] source bin/activate

- [x] cd to project settings and set allowed host to * python_init/pyshop/settings.py

#RUN TEST ON DEV MODE
- [x] python manage.py runserver 0.0.0.0:8000 //on root folder(python_init)

# GUNICORN
Where virtual environment was activated install gunicorn (hello_django/)
- [x] pip install gunicorn

# CD TO PROJECT
- [x] cd python_init
- [x] gunicorn pyshop.wsgi:application --bind 0.0.0.0:8000

# CREATE GUNICORN FILE ON PROJECT DIRECTORY
- [x] sudo nano bin/gunicorn_start

- [x] add the following
#!/bin/bash
# Name of the application
NAME="hello_app"
# Django project directory
DJANGODIR=/home/ubuntu/hello_django/python_init
# we will communicte using this unix socket
SOCKFILE=/home/ubuntu/hello_django/run/gunicorn.sock
# the user to run as
USER=ubuntu
# the group to run as
GROUP=ubuntu
# how many worker processes should Gunicorn spawn
NUM_WORKERS=3
# which settings file should Django use
DJANGO_SETTINGS_MODULE=pyshop.settings
# WSGI module name
DJANGO_WSGI_MODULE=pyshop.wsgi
echo "Starting $NAME as `whoami`"
# Activate the virtual environment
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=-

#ADDING PERMISSON
- [x] sudo chmod u+x bin/gunicorn_start

test
- [x] bin/gunicorn_start

- [x] mkdir logs on project folder


# NGINX

- [x] sudo apt-get install nginx
- [x] sudo service nginx start


- [x] sudo rm -rf /etc/nginx/sites-available/default
- [x] sudo rm -rf /etc/nginx/sites-enabled/default

- [x] sudo nano /etc/nginx/sites-available/hello

# paste the following

upstream hello_app_server {
# fail_timeout=0 means we always retry an upstream even if it failed
# to return a good HTTP response (in case the Unicorn master nukes a
# single worker for timing out).
server unix:/home/ubuntu/hello_django/run/gunicorn.sock fail_timeout=0;
}
server {
listen   80;
server_name example.com;
client_max_body_size 4G;
access_log /home/ubuntu/hello_django/logs/nginx-access.log;
error_log /home/ubuntu/hello_django/logs/nginx-error.log;
location / {
# an HTTP header important enough to have its own Wikipedia entry:
#   http://en.wikipedia.org/wiki/X-Forwarded-For
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
# enable this if and only if you use HTTPS, this helps Rack
# set the proper protocol for doing redirects:
# proxy_set_header X-Forwarded-Proto https;
# pass the Host: header from the client right along so redirects
# can be set properly within the Rack application
proxy_set_header Host $http_host;
# we don't want nginx trying to do something clever with
# redirects, we set the Host: header above already.
proxy_redirect off;
# set "proxy_buffering off" *only* for Rainbows! when doing
# Comet/long-poll stuff.  It's also safe to set if you're
# using only serving fast clients with Unicorn + nginx.
# Otherwise you _want_ nginx to buffer responses to slow
# clients, really.
# proxy_buffering off;
# Try to serve static files from nginx, no point in making an
# *application* server like Unicorn/Rainbows! serve static files.
if (!-f $request_filename) {
proxy_pass http://hello_app_server;
break;
}
}
# Error pages
error_page 500 502 503 504 /500.html;
location = /500.html {
root /home/ubuntu/hello_django/static/;
}
}

# create symbolic link
- [x] sudo ln -s /etc/nginx/sites-available/hello /etc/nginx/sites-enabled/hello

- [x] bin/gunicorn_start
- [x] sudo service nginx restart

# ADD SSL CERTIFICATE
Follow the below steps to add ssl
- [x] https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx.html