from django.urls import path

from .api_movies_view import *

app_name = "imdb_movies"

urlpatterns = [
    path('<id>/',api_movies_detail_by_id,name='movie_id'),
    path('<id>/update',api_movie_update,name='movie_update'),
    path('<id>/delete',api_movie_delete,name='movie_delete'),
    path('create',api_movie_create,name='create_movie'),
    path('bulk_create',api_movie_create_bulk,name='bulk_create_movie'),
    path('get_admin_token',get_admin_token,name='get_admin_token'),
    path('all',api_all_movies_list,name='all_movies'),

    # Search of the movie is implemented using class based view
    path('search',SearchMovieListView.as_view(),name='search_movies'),
]