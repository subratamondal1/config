from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) -> HttpResponse:
    data:dict = {"movies":["Gladiator","Pushpa", "KGF", "RRR"]}
    return render(request=request, template_name="movies/index.html", context=data)

def about(request) -> HttpResponse:
    return render(request=request, template_name="movies/about.html")