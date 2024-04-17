import os
import django
from django.db import models

os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='config.settings')
django.setup()

# Create your models here.
# models => python classes
# model reprsents a table in the database
class JobPost(models.Model):
    # by default we have the 'id' field that auto-increments from 1
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()

# CRUD OPERATIONS
# Create Read Update Delete

# model manager => objects
# JobPost.objects.all() 
# JobPost.objects.get(id=1)
# JobPost.objects.filter(title="Machine Learning")

# # CREATE
# new_job:JobPost = JobPost.objects.create(
#     title='Software Engineer',
#     description='We are looking for a software engineer...',
#     company='TechCompany',
#     salary=80000
# )
# new_job.save()
# print("...Create...")

# # READ
# # Get all job posts
# all_jobs = JobPost.objects.all()
# print(all_jobs)

# # Get a single job post by id
# job:JobPost = JobPost.objects.get(id=1)
# print(job)

# # Filter job posts by title
# se_jobs = JobPost.objects.filter(title='Software Engineer')
# print(se_jobs)
# print("...READ...")

# # UPDATE
# # Get the job post
# job = JobPost.objects.get(id=1)

# # Change the title
# job.title = 'Senior Software Engineer'

# # Save the changes
# job.save()
# print("...UPDATE...")

# # DELETE
# # Get the job post
# job = JobPost.objects.get(id=1)

# # Delete the job post
# job.delete()
# print("...DELETE...")



