from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.index, name="home"),
    path(route="job/<int:id>/", view=views.job_detail, name="job_detail")
]
