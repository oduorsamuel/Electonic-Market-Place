
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

NAME="hello_app"
DJANGODIR=/home/ubuntu/hello_django/python_init
SOCKFILE=/home/ubuntu/hello_django/run/gunicorn.sock
USER=ubuntu
GROUP=ubuntu
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=pyshop.settings
DJANGO_WSGI_MODULE=pyshop.wsgi
echo "Starting $NAME as `whoami`"
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=-

#ADDING PERMISSON
- [x] sudo chmod u+x bin/gunicorn_start

#TEST
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
server unix:/home/ubuntu/hello_django/run/gunicorn.sock fail_timeout=0;
}
server {
listen   80;
server_name example.com;
client_max_body_size 4G;
access_log /home/ubuntu/hello_django/logs/nginx-access.log;
error_log /home/ubuntu/hello_django/logs/nginx-error.log;
location / {
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header Host $http_host;
proxy_redirect off;
if (!-f $request_filename) {
proxy_pass http://hello_app_server;
break;
}
}
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