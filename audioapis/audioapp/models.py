from django.db import models

# Audiofile - Song

class Song(models.Model):
    def __str__(self):
        return self.songname
    songname = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_on = models.DateTimeField(auto_now_add=True)

class Podcast(models.Model):
    def __str__(self):
        return self.podcastname
    podcastname = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)

class Participant(models.Model):
    def __str__(self):
        return self.participant_name
    participant_name = models.CharField(max_length=100)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

class Audiobook(models.Model):
    def __str__(self):
        return self.bookname
    bookname = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    