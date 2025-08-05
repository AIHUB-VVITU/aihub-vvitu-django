from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MatlabMaterial)
admin.site.register(MatlabExperiment)
admin.site.register(ExperimentOutput)