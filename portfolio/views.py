from django.shortcuts import render,  get_object_or_404
from .models import Project
# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render (request, 'home.html', {'projects' : projects})

#def layout( request):
 #   project = get_object_or_404(project):
  #  return render(request, 'layout.html')