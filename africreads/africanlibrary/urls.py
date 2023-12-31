from django.urls import path
from .views import index, stories, story_detail, search, register, add_story

app_name = "main"

urlpatterns = [
    path('', index, name="index"),
    path('stories/', stories, name="stories"),
    path('stories/<uuid:story_id>/', story_detail, name='story_detail'),
    path('search/', search, name="search"),
    path("auth/register/", register, name = "register"),
    path('add_post/', add_story, name="add_post"),
]
