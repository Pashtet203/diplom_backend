from django.db import models

class recognize_song(models.Model):
    name = models.TextField()
    data_song = models.BinaryField()


