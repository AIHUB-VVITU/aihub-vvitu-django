import os
import shutil
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

class Game(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def get_file_path(self, title):
        return f'games/{title}'
    html = models.FileField(upload_to=get_file_path, help_text="")
    apk = models.FileField(upload_to=get_file_path)
    icon = models.ImageField(upload_to=get_file_path)

    def __str__(self):
        return self.title    

@receiver(post_save, sender=Game)
def game_post_save(sender, instance, **kwargs):
    # Create a unique directory for this game
    game_dir = os.path.join('media', 'games', instance.title)
    template_dir = os.path.join('apps', 'games', 'templates')
    
    # Create directories if they don't exist
    os.makedirs(game_dir, exist_ok=True)
    
    # Move files to their respective directories
    for field in ['html', 'apk', 'icon']:
        file_field = getattr(instance, field)
        if file_field and hasattr(file_field, 'path') and os.path.exists(file_field.path):
            # Get the filename from the path
            filename = os.path.basename(file_field.path)
            
            # Determine target directory based on file type
            if field == 'html':
                target_dir = template_dir
            else:
                target_dir = game_dir
                
            # Create the target path
            target_path = os.path.join(target_dir, filename)
            
            # Move the file if it's not already in the correct location
            if file_field.path != target_path and os.path.exists(file_field.path):
                shutil.move(file_field.path, target_path)
                # Update the model's file path
                relative_path = os.path.relpath(target_path, os.path.join(os.getcwd(), 'media'))
                file_field.name = relative_path
                
    # Save the instance if any paths were updated
    instance.save(update_fields=['html', 'apk', 'icon'])

@receiver(post_delete, sender=Game)
def game_post_delete(sender, instance, **kwargs):
    if instance.html and instance.html.path and os.path.exists(instance.html.path):
        os.remove(instance.html.path)
    # Delete APK file
    if instance.apk and instance.apk.path and os.path.exists(instance.apk.path):
        os.remove(instance.apk.path)
    # Delete Icon file
    if instance.icon and instance.icon.path and os.path.exists(instance.icon.path):
        os.remove(instance.icon.path)