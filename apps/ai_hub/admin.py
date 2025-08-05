from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Team)
admin.site.register(models.Apps)
admin.site.register(models.Game)
admin.site.register(models.Event)
admin.site.register(models.Blog)
admin.site.register(models.CareerChoice)
admin.site.register(models.Hackathon)
admin.site.register(models.JobGuide)