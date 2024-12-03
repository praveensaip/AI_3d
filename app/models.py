from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image.name
    
class UploadedMusic(models.Model):
    music = models.FileField(upload_to='music/')
    def __str__(self):
        return self.music.name

class FashionShowSettings(models.Model):
    theme = models.CharField(max_length=50, choices=[
        ('runway', 'Runway'),
        ('garden', 'Garden'),
        ('futuristic', 'Futuristic City'),
    ])
    music = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
