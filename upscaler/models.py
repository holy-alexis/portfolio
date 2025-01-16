from django.db import models
import time
from main.settings import MEDIA_URL


class Image(models.Model):
    image = models.ImageField(upload_to=f'{MEDIA_URL}upscaler/{time.time()}')

    def __str__(self):
        return self.image
