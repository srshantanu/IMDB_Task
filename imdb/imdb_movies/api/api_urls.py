from django.urls import path

from .api_movies_view import api_movies_detail_by_name

app_name = "imdb_movies"

urlpatterns = [
    path('<name>',api_movies_detail_by_name,name='movie_name'),
]