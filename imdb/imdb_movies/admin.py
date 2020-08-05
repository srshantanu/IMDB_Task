from django.contrib import admin

from .models import *

admin.site.register(Movies)
admin.site.register(Review)
admin.site.register(Playlist)
admin.site.register(MoviePlaylist)
admin.site.register(MovieReview)