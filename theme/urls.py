from django.urls import path

from .views import index

urlpatterns = [
    path(route="theme/", view=index, name="theme index")
]