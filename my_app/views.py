from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) -> HttpResponse:
    return HttpResponse(content="Hello World")

def greet_user(request, first_name:str) -> HttpResponse:
    return HttpResponse(content=f"Hello! {first_name}")

def about(request) -> HttpResponse:
    return HttpResponse(content="About Me")

def articles_year(request, year:int) -> HttpResponse:
    return HttpResponse(content=f"Article Year: {year}")

def add(request, a, b) -> HttpResponse:
    return HttpResponse(content=f"{a} + {b} = {a+b}")