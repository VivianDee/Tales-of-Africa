from django.shortcuts import render, get_object_or_404
from .models import Story

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("African Library coming soon")

def stories(request):
    """Gets all available stories and their contexts from the database and 
    displays them on the page
    """
    stories = Story.objects.all()
    context = {'stories': stories}
    return render(request, 'stories.html', context)

def story_detail(request, story_id):
    """
        Gets a specific story by id
    """
    story = get_object_or_404(Story, id=story_id)
    context = {'story': story}
    return render(request, 'story_detail.html', context)
