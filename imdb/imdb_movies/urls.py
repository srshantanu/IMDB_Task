from django.urls import path, include

from . import views
from .api import api_urls

urlpatterns = [
    # path('', views.index, name='index'),
    path('api/movie/', include(api_urls), name='movie_api')

    #REST API urls

]