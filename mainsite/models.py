from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.CharField(max_length=200)
    movie_image = models.ImageField()
    movie_name = models.TextField()
    movie_date = models.CharField(max_length=200)
    movie_rating = models.DecimalField(max_digits=4, decimal_places=3)

class User(models.Model):
    username = models.CharField(max_length=200)

class Favorite(models.Model):
    user = models.ForeignKey('User', related_name='favorites', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return self.user