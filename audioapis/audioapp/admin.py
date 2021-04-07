from django.contrib import admin
from .models import Audiobook, Participant, Podcast, Song

class ParticipantInLine(admin.TabularInline):
    model=Participant

class PodcastAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['podcastname']}),
    ('Upload date', {'fields': ['uploaded_on']}),
    ('Host', {'fields': ['host']}),
    ('Duration', {'fields':['duration']}),
    ]
    readonly_fields = ['uploaded_on']
    inlines = [ParticipantInLine]
admin.site.register(Audiobook)
admin.site.register(Song)
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Participant)




