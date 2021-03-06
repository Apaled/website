from django.db import models


# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=1000)
    album_title = models.CharField(max_length=1000)
    genre = models.CharField(max_length=1000)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + " by " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=1000)
    song_title = models.CharField(max_length=1000)
