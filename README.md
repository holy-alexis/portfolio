# holy_alexis site

Site is working under Django framework for Python

To start this site follow the steps below:

Download:<br>
>Python3<br>
>Git CLI<br>
>PostgreSQL

Open console and input next lines: <br>
>git clone https://github.com/holy-alexis/portfolio <br>
>cd portfolio<br>

[WINDOWS]
> pip install -r requirements.txt<br>

[LINUX]
> pip3 install -r requirements.txt<br>

In folder "main" in file "setting.py" make sure that user password host port of variable DATABASES set to yours PostgreSQL properties
(you can use site without it, just comment full variable DATABASES, but page "Towns" won't work properly)<br>
Create database through PostgreSQL console using commang
>CREATE DATABASE towns WITH OWNER postgres ENCODING 'utf-8';<br>
Note: change "postgres" to your username to PostgreSQL

If you use PostgreSQL make sure to execute make.py, it would load "Towns" data from folder dumps


To start server<br>
[WINDOWS]
> python manage.py runserver

[LINUX]
> python3 manage.py runserver


To access "Admin" page you can use django superuser login & pass<br>
Just create one using<br>
[WINDOWS]
> python manage.py createsuperuser

[LINUX]
> python3 manage.py createsuperuser
