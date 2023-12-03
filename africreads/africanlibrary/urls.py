from django.urls import path
from .views import index, stories, story_detail, search

urlpatterns = [
    path('', index, name="index"),
    path('stories/', stories, name="stories"),
    path('stories/<uuid:story_id>/', story_detail, name='story_detail'),
    path('search/', search, name="search"),
]
