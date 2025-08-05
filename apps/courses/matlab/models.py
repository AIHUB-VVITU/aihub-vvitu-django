from django.db import models

# Create your models here.
class MatlabExperiment(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to='courses/matlab/exp_imgs')
    blog_file = models.FileField(upload_to='courses/matlab/exp_detail')
    exp_data = models.JSONField()

class MatlabMaterial(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='courses/matlab/materials')

class ExperimentOutput(models.Model):
    exp_no = models.CharField(max_length=2)
    slide_no = models.CharField(max_length=2)
    img = models.ImageField(upload_to='courses/matlab/exp_outputs')