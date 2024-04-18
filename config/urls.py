"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from my_app import views as base_views
from movies import views as movies_views
from theme import views as theme_views

urlpatterns = [
    # TailwindCSS Setup
    path("__reload__/", include("django_browser_reload.urls")),
    # URL for BASE APP
    path(route="admin/", view=admin.site.urls),
    path(route="base/", view=base_views.index), # mysite.com/ => index() => Hello World
    path(route="base/greet/<str:first_name>", view=base_views.greet_user),
    path(route="base/about/", view=base_views.about),
    path(route="base/articles/<int:year>/", view=base_views.articles_year),
    path(route="base/add/<int:a>/<int:b>/", view=base_views.add),

    # URL for MOVIES APP
    path(route="movies/", view=movies_views.index, name="index"),
    path(route="movies/about/", view=movies_views.about, name="about"),

    # URL for JOB BOARD APP
    path(route="", view=include(arg="job_board.urls")),

    # URL for THEME APP
    path(route="theme/", view=include(arg="theme.urls")),
    path(route="theme/", view=theme_views.index)
]
