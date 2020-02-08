from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #Establishes one to one relation with existing User model
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    #To use ImageField method we need to install pillow
    #You can add other fields like bio, current city, etc as well

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()


        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            #This is to resize the lagre size images into rounded ones
