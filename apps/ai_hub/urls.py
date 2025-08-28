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
    path('projects/ml', views.ml, name='ml'),
    path('events/meetups', views.meetups, name='meetups'),
    re_path(r'blog_viewer/media/blogs/(?P<pk>.+)', views.blog_viewer, name='blog_viewers'),
    path('career/<str:pk>', views.career_choice, name='career_choice'),
    path('socialGPT/about', views.socialGPT, name='socialGPT'),
    path("ask-llama/", views.ask_llama, name="ask_llama"),
    path("google/login", views.google_login, name="google_login"),
    path("sign-in-callback", views.sign_in_callback, name="sign_in_callback"),
    path("sign-out-callback", views.sign_out_callback, name="sign_out_callback"),
    path('refresh-token/', views.refresh_google_token, name='refresh_google_token'),
    path('handle-errors/', views.handle_google_errors, name='handle_google_errors'),
]