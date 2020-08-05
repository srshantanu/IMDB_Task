# Generated by Django 3.1 on 2020-08-05 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('movie_Id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('movie_name', models.CharField(max_length=200)),
                ('movie_director', models.CharField(max_length=50)),
                ('movie_imdb_score', models.FloatField(default=0.0, max_length=10)),
                ('movie_genre', models.TextField(null=True)),
                ('movie_99popularity', models.FloatField(default=0.0, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('playlist_Id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('playlist_name', models.CharField(max_length=200)),
                ('playlist_movie_count', models.IntegerField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('review_Id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('review_comment', models.TextField(null=True)),
                ('review_stars', models.FloatField(default=0.0, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPlaylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('playlist_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_movies.playlist')),
                ('user_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_Id', 'playlist_Id')},
            },
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('movie_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_movies.movies')),
                ('review_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_movies.review')),
            ],
            options={
                'unique_together': {('movie_Id', 'review_Id')},
            },
        ),
        migrations.CreateModel(
            name='MoviePlaylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('movie_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_movies.movies')),
                ('playlist_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_movies.playlist')),
            ],
            options={
                'unique_together': {('movie_Id', 'playlist_Id')},
            },
        ),
    ]