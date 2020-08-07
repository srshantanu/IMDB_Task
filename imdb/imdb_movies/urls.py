from django.urls import path, include

from .api.api_movies_view import api_all_movies_list
from .api import api_urls

urlpatterns = [

    # added the defult list of movies when comes on website
    path('',api_all_movies_list, name='movie_list'),


    # REST API urls
    path('api/movie/', include(api_urls), name='movie_api')



]