from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('blogs', views.blogs, name='blogs'),
    path('about', views.about, name='about'),
    path('apps', views.apps, name='apps'),
    path('events', views.events, name='events'),
    path('career', views.career, name='career'),
    path('career/job-guide', views.job_guide, name='job_guide'),
    path('courses', views.courses, name='courses'),
    path('projects/games', views.games, name='games'),
    path('events/meetups', views.meetups, name='meetups'),
    re_path(r'blog_viewer/media/blogs/(?P<pk>.+)', views.blog_viewer, name='blog_viewers'),
    path('career/<str:pk>', views.career_choice, name='career_choice')
]