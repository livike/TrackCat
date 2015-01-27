from django.db import models
from django.utils import timezone
# Create your models here.

class Projects(models.Model):
	PROJECT_STATUS = (
		('open', 'Opened'),
		('progress', 'In progress'),
		('closed', 'Closed'),
		)
	project_name = models.CharField(max_length=50)
	project_description = models.CharField(max_length=150, blank=True)
	status_id = models.CharField(max_length=8, choices=PROJECT_STATUS, default=open)
	project_deadline = models.DateTimeField(blank=True)
	repository_link = models.CharField(max_length=300, blank=True)
	website_prod = models.CharField(max_length=300, blank=True)
	website_test = models.CharField(max_length=300, blank=True)
	# project_owner = models.ForeignKey(Users)
	date_created = models.DateTimeField(auto_now_add=True, default=timezone.now)
	date_modified = models.DateTimeField(auto_now=True)
