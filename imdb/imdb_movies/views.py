from django.http import HttpResponse
from .models import Movies

def index(request):
    movies = Movies.objects.all()
    print("Movies Printed==>",movies)
    return HttpResponse("Hello, world. You're at the polls index.")
