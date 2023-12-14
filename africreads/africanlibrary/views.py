from django.shortcuts import render, get_object_or_404, redirect
from .models import Story
from django.http import HttpResponse
from django.contrib import messages
from . import forms

# Create your views here.
def index(request):
    user = request.user
    context = {
        'user' : user,
    }
    return render(request, 'main.html', context)

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

def search(request):
    """ Searches the database for a story by name"""
    query = request.GET.get('query', '')
    stories = Story.objects.filter(title__icontains=query)

    context = {'stories': stories, 'query': query}
    count = len(stories.values())
    if int(count) is 0:
        messages.info(request, 'Your search {} did not match any stories'.format(query))
    return render(request, 'stories.html', context)
def register(request):
	if request.method == "POST":
		form = forms.NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			#login(request, user)
			return redirect("main:index")
	form = forms.NewUserForm
	return render (request, "registration/register.html", context={"form":form})
