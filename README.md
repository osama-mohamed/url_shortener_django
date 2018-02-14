# [URL Shortener](https://url-osama-mohamed-django.herokuapp.com) By Django

[<img src="https://www.djangoproject.com/s/img/logos/django-logo-negative.png" width="200" title="Django Projects" >](https://github.com/OSAMAMOHAMED1234/django_projects)
[<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="150" title="Django Projects" >](https://github.com/OSAMAMOHAMED1234/django_projects)


## For live preview :
> [URL Shortener](https://url-osama-mohamed-django.herokuapp.com)


## Usage :
### Run project by :

``` python

# change database connection information in settings.py DATABASES default values with your info then run 

1. python manage.py migrate

2. python manage.py runserver

# if you want to manage to project just create super user account by :

3. python manage.py createsuperuser

```

That's it.

## Done :

Now the project is running at `http://localhost:8000` and your routes is:


| Route                 | HTTP Method 	 | Description                           	      |
|:----------------------|:--------------:|:---------------------------------------------|
| {host}       	        | POST       	   | Paste original link to be shortened          |
| {host}/<short_url>  	| GET       	   | Redirect to the original link           	    |
| {host}/admin/  	      | GET      	     | Admin control panel                     	    |



For detailed explanation on how project work, read the [Django Docs](https://docs.djangoproject.com/en/1.11/) and [MySQLDB Docs](https://dev.mysql.com/doc/)

## Developer
This project made by [Osama Mohamed](https://www.facebook.com/osama.mohamed.ms)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)

