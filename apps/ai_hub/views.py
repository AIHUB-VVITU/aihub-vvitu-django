import requests
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from datetime import datetime, timedelta
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import AuthorizedSession, Request
from google.oauth2.credentials import Credentials
from google.auth.exceptions import RefreshError

# Create your views here.
def index(request):
    return render(request, 'index.html')

def socialGPT(request):
    return render(request, "socialGPT.html")

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

def ml(request):
    ml_projects = Ml.objects.all()
    context = {'ml_projects': ml_projects}
    return render(request, 'ml.html', context)

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

def ask_llama(request):
    response = None
    if request.method == "POST":
        question = request.POST.get("question")
        if question:
            try:
                llama_api_url = "http://localhost:11434/api/chat"
                payload = {
                    "model": "llama3.3:70b",   # change to your model
                    "messages": [
                        {"role": "user", "content": question}
                    ],
                    "stream": False           # important: disables streaming
                }
                api_response = requests.post(llama_api_url, json=payload)

                if api_response.status_code == 200:
                    data = api_response.json()
                    # Extract content safely
                    if "message" in data and "content" in data["message"]:
                        response = data["message"]["content"]
                    else:
                        response = "No response from Llama"
                else:
                    response = f"Error: {api_response.status_code} - {api_response.text}"

            except Exception as e:
                response = f"Error: {str(e)}"

    return render(request, "llm_query.html", {"response": response})

CLIENT_SECRETS_FILE = os.path.join(os.path.dirname(__file__), "client_secret.json")

def google_login(request):
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=settings.GOOGLE_SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_SIGNIN,
    )
    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",
    )
    request.session["state"] = state
    return redirect(authorization_url)


def sign_in_callback(request):
    state = request.session["state"]
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=settings.GOOGLE_SCOPES,
        state=state,
        redirect_uri=settings.GOOGLE_REDIRECT_SIGNIN,
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    creds = flow.credentials

    # Store tokens
    request.session["google_creds"] = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "expiry": creds.expiry.isoformat() if creds.expiry else None,
        "scopes": list(creds.scopes),
    }

    authed = AuthorizedSession(creds)
    profile = authed.get("https://openidconnect.googleapis.com/v1/userinfo").json()

    return HttpResponse(f"Welcome {profile['email']}! ✅")

def sign_out_callback(request):
    request.session.flush()
    return HttpResponse("Signed out successfully ❌")

def refresh_google_token(request):
    creds_data = request.session.get("google_creds")
    if not creds_data or not creds_data.get("refresh_token"):
        return HttpResponse("No refresh token available. Please sign in again.")

    try:
        creds = Credentials(
            token=None,
            refresh_token=creds_data["refresh_token"],
            token_uri="https://oauth2.googleapis.com/token",
            client_id=settings.GOOGLE_CLIENT_ID,
            client_secret=settings.GOOGLE_CLIENT_SECRET,
        )

        creds.refresh(Request())
        request.session["google_creds"]["token"] = creds.token
        request.session["google_creds"]["expiry"] = creds.expiry.isoformat() if creds.expiry else None

        return HttpResponse("Token refreshed successfully!")
    except RefreshError as e:
        return HttpResponse(f"Failed to refresh token: {str(e)}")

def google_logout(request):
    request.session.flush()
    return redirect("https://accounts.google.com/Logout")

def handle_google_errors(request):
    try:
        # Example logic to demonstrate error handling
        creds_data = request.session.get("google_creds")
        if not creds_data:
            raise ValueError("User not authenticated.")

        creds = Credentials(token=creds_data["token"])
        authed = AuthorizedSession(creds)
        profile = authed.get("https://openidconnect.googleapis.com/v1/userinfo").json()

        return JsonResponse(profile)
    except ValueError as ve:
        return HttpResponse(f"Error: {str(ve)}")
    except Exception as e:
        return HttpResponse(f"An unexpected error occurred: {str(e)}")
