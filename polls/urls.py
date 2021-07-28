from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
path('',views.index,name="index"), # we use attribiute name for action's url in templates
path('blog/',views.text,name="text"),
path('homepage/', views.homePage,name='home'),
path('story/<int:pk>',views.storyTellerGeneric.as_view(),name='story_datail'),
path('story/',views.storyListsGeneric.as_view(),name='lists_of_stories'),
path('like/<id>',views.storyLike,name='storylike'),
path('unlike/<id>',views.storyUnlike,name='storyunlike'),


]
