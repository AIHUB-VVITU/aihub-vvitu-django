from django.db import models
from django.utils import timezone
import os

# Create your models here.
class Team(models.Model):
    s_id = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    img = models.ImageField(upload_to='team_images')
    git = models.URLField(max_length=255, blank=True, null=True)
    lkdn = models.URLField(max_length=255, blank=True, null=True)
    mail = models.EmailField(max_length=255, blank=True, null=True)
    
class Apps(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    desc = models.TextField(max_length=500, blank=True, null=True)
    img = models.ImageField(upload_to='apps_images', blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    s_id = models.CharField(max_length=15, blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
        
class Game(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    s_id = models.CharField(max_length=15, blank=True, null=True)
    desc = models.TextField(max_length=500, blank=True, null=True)
    img = models.ImageField(upload_to='game_images', blank=True, null=True)
    git_link = models.URLField(max_length=300, blank=True, null=True)
    play_url = models.URLField(max_length=300, blank=True, null=True)
    
class Event(models.Model):
    topic = models.CharField(max_length=100, blank=True, null=True)
    speaker = models.CharField(max_length=30, blank=True, null=True)
    speaker_details = models.TextField(max_length=500, blank=True, null=True)
    desc = models.TextField(max_length=500, blank=True, null=True)
    schedule = models.DateTimeField(blank=True, null=True)
    meet_url = models.URLField(max_length=500, blank=True, null=True)
    vid_url = models.URLField(max_length=500, blank=True, null=True)
    
    def is_upcoming(self):
        if self.schedule:
            return self.schedule > timezone.now()
        return False
    
class Hackathon(models.Model):
    event = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=60)
    venue = models.CharField(max_length=60)
    author = models.CharField(max_length=100)
    details = models.TextField(max_length=500)
    prizes = models.CharField(max_length=100)
    moderators = models.CharField(max_length=200)
    leaderboard_url = models.URLField(max_length=500, blank=True, null=True)
    discord_url = models.URLField(default="https://discord.gg/ChE5k7BNSe", max_length=500)
    schedule = models.DateTimeField(blank=True, null=True)

    def is_upcoming(self):
        if self.schedule:
            return self.schedule > timezone.now()
        return False


class JobGuide(models.Model):
    title = models.CharField(max_length=250)
    blog = models.FileField(upload_to='blogs', blank=True, null=True)
    def get_file_name(self):
        if self.blog and self.blog.url:
            base, ext = os.path.splitext(self.blog.url)
            return base
        return self.blog.url

class Blog(models.Model):
    title = models.CharField(max_length=250)
    blog = models.FileField(upload_to='blogs', blank=True, null=True)
    def get_file_name(self):
        if self.blog and self.blog.url:
            base, ext = os.path.splitext(self.blog.url)
            return base
        return self.blog.url
    
class CareerChoice(models.Model):
    section = models.CharField(max_length=20, null=False, blank=False)
    category = models.CharField(max_length=100)
    data = models.JSONField(null=False, default='')