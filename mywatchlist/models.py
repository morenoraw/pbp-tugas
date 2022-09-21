from django.db import models

class WatchlistItem(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.CharField(max_length=255)
    review = models.TextField()
    watched = models.TextField()