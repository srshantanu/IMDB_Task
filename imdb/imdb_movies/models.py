from django.db import models
import uuid
from django.contrib.auth.models import User

# added the base model, thus it can be used to add other models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# This Model is used to save all the info of the movies
class Movies(BaseModel):
    movie_Id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=50)
    imdb_score = models.FloatField(max_length=10, default=0.0)
    genre = models.TextField(null=True)
    movie_99popularity = models.FloatField(max_length=100, default=0.0)

    def __str__(self):
        return self.name

# This Model is used to save reviews given of movie
class Review(BaseModel):
    review_Id = models.UUIDField(default=uuid.uuid4, editable=False)
    review_comment = models.TextField(null=True)
    review_stars = models.FloatField(max_length=10, default=0.0)

    def __str__(self):
        return self.review_Id

# This Model is used to save movie playlist created by the user.
class Playlist(BaseModel):
    playlist_Id = models.UUIDField(default=uuid.uuid4, editable=False)
    playlist_name = models.CharField(max_length=200)
    playlist_movie_count = models.IntegerField(default=0)

    def __str__(self):
        return self.playlist_name

# This Model is used to save the relation between movie and playlist
class MoviePlaylist(BaseModel):
    movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    playlist_Id = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('movie_Id', 'playlist_Id')

# This Model is used to save the relation between movie and review
class MovieReview(BaseModel):
    movie_Id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    review_Id = models.ForeignKey(Review, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('movie_Id', 'review_Id')

# This Model is used to save the relation between user and playlist
class UserPlaylist(BaseModel):
    user_Id = models.OneToOneField(User, on_delete=models.CASCADE)
    playlist_Id = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_Id', 'playlist_Id')
