from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):  # overriding the save method of the parent class
        super().save()

        img = Image.open(self.image.path)  # opens the image of the current instance

        if img.height > 300 or img.width > 300:  # if the image is larger than 300x300
            output_size = (300, 300)
            img.thumbnail(output_size)  # resize the image
            img.save(self.image.path)