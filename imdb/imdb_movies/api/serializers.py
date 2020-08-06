from rest_framework import serializers

from imdb_movies.models import Movies


class MoviesSerializer(serializers.ModelSerializer):

    _99popularity = serializers.FloatField(source='movie_99popularity')


    class Meta:
        model = Movies
        fields = ['movie_Id', 'name', 'director', 'genre', 'imdb_score','_99popularity']

    # This is written to exclude or include the fields while doing serializer operations
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        add_fields = kwargs.pop('add_fields', None)
        super(MoviesSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            # for multiple fields in a list
            for field_name in remove_fields:
                self.fields.pop(field_name)

        if add_fields:
            # for multiple fields in a list
            for field_name in add_fields:
                self.fields.append(field_name)
