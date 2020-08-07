from django.urls import path, include

from .api.api_movies_view import api_all_movies_list
from .api import api_urls

urlpatterns = [
    path('',api_all_movies_list, name='movie_list'),
    path('api/movie/', include(api_urls), name='movie_api')

    #REST API urls

]