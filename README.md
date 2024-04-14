<h1 align="center">Django</h1>

<p align="center">
<img src="https://skillicons.dev/icons?i=python,django,git,github&perline=6"/>
</p>

<h2 align="left">Django Start Project</h2>

```bash
# pwd: .../config
django-admin startproject config .

# boilerplate folder structure created
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
```

<h2 align="left">Django Start Appt</h2>

```bash
# pwd: .../config
python3 manage.py startapp my_app

# boilerplate folder structure created
my_app
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```
<h2 align="left">Creating 'Views' in App</h2>

**1. Create A view in `views.py` module of your Django App**

```python
# pwd: .../my_app/views.py
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) -> HttpResponse:
    return HttpResponse(content="Hello World")
```

**2. Map your app's 'View' with the project's 'Url'.**

app's **'View'** is in `.../my_app/views.py`</br>
project's **'Url'** is in `.../config/urls.py`

```python
# pwd: .../config/urls.py
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path(route="admin/", view=admin.site.urls),
    path(route="/", view=views.index), # mysite.com/ => index() => Hello World
]
```