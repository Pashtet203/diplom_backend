from django.db import models

class Composition(models.Model):
    name = models.TextField()
    song_path = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Author(models.Model):
    name = models.TextField()
    years_of_life = models.TextField()
    img_path = models.ImageField()
    author_info = models.TextField(default='Информация скоро появится')
    listCompositions = models.ManyToManyField(Composition)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


