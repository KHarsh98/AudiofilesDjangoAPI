from .models import Song, Podcast, Participant, Audiobook
from .forms import SongForm, PodcastForm, AudiobookForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import UnreadablePostError, Http404, HttpResponse


# INDEX
@login_required
def index(request):
    return render(request, 'audioapp/index.html')

#CREATE API
def create_new(request, filetype):

    form = None
    if request.method == 'POST':
        if filetype == "song":
            form = SongForm(request.POST)
        elif filetype == "audiobook":
            form = AudiobookForm(request.POST)
        elif filetype == "podcast":
            form = PodcastForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        if filetype == "song":
            form = SongForm()
        elif filetype == "audiobook":
            form = AudiobookForm()
        elif filetype == "podcast":
            form = PodcastForm()
        
    context = {'form':form}
    return render(request, 'audioapp/form.html', context)


# UPDATE API
def update(request, filetype, fileid):
    form = None
    data_obj = None
    if request.method == 'POST':
        if filetype == "song":
            data_obj = Song.objects.get(pk=fileid)
            form = SongForm(request.POST, instance=data_obj)
        elif filetype == "audiobook":
            data_obj = Audiobook.objects.get(pk=fileid)
            form = AudiobookForm(request.POST, instance=data_obj)
        elif filetype == "podcast":
            data_obj = Podcast.objects.get(pk=fileid)
            form = PodcastForm(request.POST, instance=data_obj)

        if form.is_valid():
            form.save()

    else:
        if filetype == "song":
            form = SongForm()
        elif filetype == "audiobook":
            form = AudiobookForm()
        elif filetype == "podcast":
            form = PodcastForm()
    

    context = {'form':form}
    return render(request, 'audioapp/form.html', context)
            


# GET API
def get(request, filetype, fileid):
    if filetype=="song":
        try:
            song = Song.objects.get(pk=fileid)
        except Song.DoesNotExist:
            raise Http404("Song doesn't exist.")
        return render(request, 'audioapp/song-detail.html',{'song': song})
    
    elif filetype=="audiobook":
        try:
            audiobook = Audiobook.objects.get(pk=fileid)
        except Audiobook.DoesNotExist:
            raise Http404("Audiobook doesn't exist.")
        return render(request, 'audioapp/audiobook-detail.html',{'audiobook': audiobook})

    if filetype=="podcast":
        try:
            podcast = Podcast.objects.get(pk=fileid)
        except Podcast.DoesNotExist:
            raise Http404("Podcast doesn't exist.")
        return render(request, 'audioapp/podcast-detail.html',{'podcast': podcast})

def get_all(request, filetype):
    if filetype=="song":
        try:
            songs = Song.objects.all()
        except Song.DoesNotExist:
            raise Http404("Song doesn't exist.")
        return render(request, 'audioapp/song-all.html',{'songs': songs})
    
    elif filetype=="audiobook":
        try:
            audiobooks = Audiobook.objects.all()
        except Audiobook.DoesNotExist:
            raise Http404("Audiobook doesn't exist.")
        return render(request, 'audioapp/audiobook-all.html',{'audiobooks': audiobooks})

    if filetype=="podcast":
        try:
            podcasts = Podcast.objects.all()
        except Podcast.DoesNotExist:
            raise Http404("Podcast doesn't exist.")
        return render(request, 'audioapp/podcast-all.html',{'podcasts': podcasts})


#DELETE API

def delete(request, filetype, fileid):
    if filetype=="song":
        try:
            song = Song.objects.get(pk=fileid)
        except Song.DoesNotExist:
            raise Http404("Song doesn't exist.")
        else:
            song.delete()
        
    
    elif filetype=="audiobook":
        try:
            audiobook = Audiobook.objects.get(pk=fileid)
        except Audiobook.DoesNotExist:
            raise Http404("Audiobook doesn't exist.")
        else:
            audiobook.delete()
        

    if filetype=="podcast":
        try:
            podcast = Podcast.objects.get(pk=fileid)
        except Podcast.DoesNotExist:
            raise Http404("Podcast doesn't exist.")
        else:
            podcast.delete()
    return render(request, 'audioapp/deleted.html')


    