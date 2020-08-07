from django.contrib import admin

from .models import *

# this is used to list the models in django default admin panel
admin.site.register(Movies)
admin.site.register(Review)
admin.site.register(Playlist)
admin.site.register(MoviePlaylist)
admin.site.register(MovieReview)