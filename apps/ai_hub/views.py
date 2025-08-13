from django.shortcuts import render
from django.conf import settings
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'Projects.html')

def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)

def blog_viewer(request, pk):
    return render(request, 'blog_viewer.html', {'pk': pk})

def apps(request):
    apps = Apps.objects.all()
    context = {'apps': apps}
    return render(request, 'Apps.html', context)

def career(request):
    articles = JobGuide.objects.all()
    articles = [article for article in articles]
    articles = articles[-1 : -4 : -1]
    context = {'articles': articles}
    return render(request, 'Career.html', context)

def games(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'Game.html', context)

def courses(request):
    return render(request, 'courses.html')

def job_guide(request):
    articles = JobGuide.objects.all()
    context = {'articles': articles}
    return render(request, 'job_guide.html', context)

def events(request):
    meetups = Event.objects.all()
    hackathons = Hackathon.objects.all()

    event_upcoming = [event for event in meetups if event.is_upcoming()]
    if len(event_upcoming) == 0:
        event_upcoming = None 
    event_past = [event for event in meetups if not event.is_upcoming()]

    hackathon_upcoming = [hackathon for hackathon in hackathons if hackathon.is_upcoming()]
    if len(hackathon_upcoming) == 0:
        hackathon_upcoming = None
    hackathon_past = [hackathon for hackathon in hackathons if not hackathon.is_upcoming()]

    context = {
        'event_upcoming': event_upcoming, 
        'event_past': event_past[-2:], 
        'hackathon_upcoming': hackathon_upcoming,
        'hackathon_past': hackathon_past[-1 : : -1]
    }
    return render(request, 'Events.html', context)

def meetups(request):
    meetups = Event.objects.all()
    context = {'meetups': meetups}
    return render(request, 'Meetups.html', context)

def about(request):
    team_members = Team.objects.all()
    context = {'team_members': team_members}
    return render(request, 'about.html', context)

def career_choice( request, pk ):
    section_content = CareerChoice.objects.filter(section=pk)
    categories = section_content.values_list('category', flat=True).distinct()
    selected_category = request.GET.get('category')
    if selected_category:
        section_content = section_content.filter(category=selected_category)

    context = {'pk': pk, 'categories': categories, 'selected_category': selected_category, 'data': section_content}
    return render(request, 'career_content.html', context)