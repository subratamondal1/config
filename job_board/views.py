from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) -> HttpResponse:
    return HttpResponse(content="<h1>Welcome to Job Board</h1>")
