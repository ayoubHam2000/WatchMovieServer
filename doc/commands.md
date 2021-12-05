py -m pip install vertualenv
vertualenv env
py -m pip install django


py -m pip freeze //see installed packages in python
py -m pip install django //for server
py -m pip install pillow //for images


## django ##
django-admin startproject [projectName] [path] //start the project

py manage.py migrate => sync the models with the data base
py manage.py startapp appName
py manage.py makemigrations => create the schema for latter use with the data base
py manage.py createsuperuser
py manage.py makemigrations <app-name>

py manage.py migrate your_app zero
py manage.py migrate <app-name>

## extra ##
py manage.py migrate --run-syncdb
py manage.py dbshell
py manage.py shell
py manage.py migrate --fake <app-name> zero
pip install -r  requirement.txt
