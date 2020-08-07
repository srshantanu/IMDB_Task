from django.urls import path, include

from .api.api_movies_view import SearchMovieListView
from .api import api_urls

urlpatterns = [
    path('',SearchMovieListView, name='movie_list'),
    path('api/movie/', include(api_urls), name='movie_api')

    #REST API urls

]