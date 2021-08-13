from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

class ProjectDetailView(DetailView):
    model = Project

class ProjectListView(ListView):
    model = Project