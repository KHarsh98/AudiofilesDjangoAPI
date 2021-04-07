from django.forms import ModelForm
from audioapp.models import Song, Participant, Podcast, Audiobook

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields= '__all__'

class PodcastForm(ModelForm):
    class Meta:
        model = Podcast
        fields= '__all__'

class AudiobookForm(ModelForm):
    class Meta:
        model = Audiobook
        fields = '__all__'