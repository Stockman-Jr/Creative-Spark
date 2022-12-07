from django.shortcuts import render
from django.views import generic
from .models import Challenge


class ChallengeList(generic.ListView):
    model = Challenge
    template_name = 'index.html'
    ordering = ['-date_created']
    paginate_by = 6
    

