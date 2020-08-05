from rest_framework import serializers

from imdb_movies.models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['movie_Id','movie_name', 'movie_director', 'movie_genre','movie_imdb_score','movie_99popularity']