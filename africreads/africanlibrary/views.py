from django.shortcuts import render, get_object_or_404, redirect
from .models import Story
from django.http import HttpResponse
from django.contrib import messages
from . import forms
from django.contrib.auth.models import User, AnonymousUser
from .forms import StoryAddForm
# Create your views here.
"""
Get Authur
"""
def get_author(user_id):
    author = User.objects.get(id=user_id)
    return author

"""
Index page
"""
def index(request):
    user = request.user
    context = {
        'user' : user,
    }
    return render(request, 'main.html', context)

"""
Fetch all stories
"""
def stories(request):
    """Gets all available stories and their contexts from the database and 
    displays them on the page
    """
    stories = Story.objects.all()
    # Convert numerics into author objects
    for story in stories:
        if story.author == -1:
            story.author = AnonymousUser
        else:
             story.author = get_author(story.author)
    context = {'stories': stories}
    return render(request, 'stories.html', context)

"""
View a story
"""
def story_detail(request, story_id):
    """
        Gets a specific story by id
    """
    story = get_object_or_404(Story, id=story_id)
    if story.author == -1:
         story.author = AnonymousUser
    else:
         story.author = get_author(story.author)

    context = {'story': story}
    return render(request, 'story_detail.html', context)
"""
Search for stories
"""
def search(request):
    """ Searches the database for a story by name"""
    query = request.GET.get('query', '')
    stories = Story.objects.filter(title__icontains=query)
    for story in stories:
        if story.author == -1:
            story.author = AnonymousUser
        else:
             story.author = get_author(story.author)

    context = {'stories': stories, 'query': query}
    count = len(stories.values())
    if int(count) is 0:
        messages.info(request, 'Your search {} did not match any stories'.format(query))
    return render(request, 'stories.html', context)

"""
Register new users
"""    
def register(request):
	if request.method == "POST":
		form = forms.NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			#login(request, user)
			return redirect("main:index")
	form = forms.NewUserForm
	return render (request, "registration/register.html", context={"form":form})

"""
Add story
"""
def add_story(request):
     story = request.POST.copy()   
     if request.user.is_authenticated:
          story['author'] = request.user.id
     else:
           story['author'] = -1
     request.POST = story
     form = StoryAddForm(request.POST)
     if form.is_valid():
          form.save()
          return redirect('main:stories')
     form = StoryAddForm()
     return render(request, 'add_post.html', context={'form' : form})