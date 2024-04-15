from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) -> HttpResponse:
    return render(request=request, template_name="movies/index.html")