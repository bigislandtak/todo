from django.db import models

# Create your models here.
class Task(models.Model):
    """docstring for Task"""
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)  # noqa: E101, W191
    created = models.DateTimeField(auto_now_add=True)  # noqa: E101, W191

    def __str__(self):
    	return self.title