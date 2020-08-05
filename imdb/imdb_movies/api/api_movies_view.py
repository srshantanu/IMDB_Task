from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from imdb_movies.models import Movies

from .serializers import MoviesSerializer


@api_view(['GET'])
def api_movies_detail_by_name(request,name):
    try:
        movies = Movies.objects.get(movie_name=name)
        print("Movies Printed in API ==>", movies)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MoviesSerializer(movies)
    return Response(serializer.data)



