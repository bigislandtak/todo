from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import models
from . import forms
# Create your views here.

def index(request):
	tasks = models.Task.objects.all()
	form = forms.TaskForm()

	if request.method == 'POST':
		form = forms.TaskForm(request.POST)
		if form.is_valid:
			form.save()
		return HttpResponseRedirect('/')

	context = {'tasks':tasks, 'form':form}
	return render(request, 'tasks/list.html', context)


def update_task(request, pk):
	task = models.Task.objects.get(pk=pk)
	form = forms.TaskForm(instance=task)

	if request.method == 'POST':
		form = forms.TaskForm(request.POST, instance=task)
		if form.is_valid:
			form.save()
		return HttpResponseRedirect('/')

	context = {'form':form}
	return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
	task = models.Task.objects.get(pk=pk)
	context = {'task':task}

	if request.method == 'POST':
		task.delete()
		return HttpResponseRedirect('/')

	return render(request, 'tasks/delete_task.html', context)