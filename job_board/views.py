from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import JobPost

# Create your views here.
def index(request) -> HttpResponse:
    active_jobs = JobPost.objects.filter(is_active=True)
    return render(request=request, template_name="job_board/index.html", context={"active_jobs":active_jobs})

def job_detail(request, id) -> HttpResponse:
    job_post = get_object_or_404(JobPost, id=id, is_active=True)
    return render(request=request, template_name="job_board/details.html", context={"job_post_detail":job_post})