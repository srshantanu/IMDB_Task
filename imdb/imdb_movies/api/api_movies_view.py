
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from imdb_movies.models import Movies

from .serializers import MoviesSerializer

class SearchMovieListView(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    pagination_class = PageNumberPagination
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('name', 'director', 'genre','imdb_score','movie_99popularity')

@api_view(['GET',])
@permission_classes((AllowAny,))
def api_all_movies_list(request):
    paginator = PageNumberPagination()
    data = {}
    try:

        movies = Movies.objects.all()
        result_page = paginator.paginate_queryset(movies, request)
        serializer = MoviesSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    except Movies.DoesNotExist:

        data["error"] = "Movie DoesNot Exist"
        response_status = status.HTTP_404_NOT_FOUND

        return Response(data=data, status=response_status)



@api_view(['GET',])
@permission_classes((AllowAny,))
def api_movies_detail_by_id(request, id):
    data = {}
    try:

        movies = Movies.objects.get(movie_Id=id)
        serializer = MoviesSerializer(movies)
        data["success"] = serializer.data
        response_status = status.HTTP_200_OK

    except Movies.DoesNotExist:

        data["Error"] = "Movie DoesNot Exist"
        response_status = status.HTTP_404_NOT_FOUND


    return Response(data=data,status=response_status)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def api_movie_update(request, id):
    data = {}
    request_data = {}

    try:
        movies = Movies.objects.get(movie_Id=id)

        user = request.user

        if user.is_superuser:

            # This is done because input json has 99popularity as key which cannot be a var in python,thus added
            # _99popularity.

            request_data["_99popularity"] = request.data["99popularity"]
            request_data.update(request.data)

            # Using Sqllite3 in which we can't store array so have convert list as string
            request_data["genre"] = ''.join(request.data["genre"])

            serializer = MoviesSerializer(movies, remove_fields=['movie_Id'], data=request_data)
            if serializer.is_valid():
                serializer.save()
                data["success"] = "Update Successful!"
                response_status = status.HTTP_200_OK
            else:
                data["Error"] = serializer.errors
                response_status = status.HTTP_400_BAD_REQUEST
        else:
            data["Error"] = "Un-authorized"
            response_status = status.HTTP_401_UNAUTHORIZED

    except Movies.DoesNotExist:
        data["Error"] = "Movie Does Not Exist"
        response_status = status.HTTP_404_NOT_FOUND

    return Response(data=data, status=response_status)


@api_view(['Delete',])
@permission_classes((IsAuthenticated,))
def api_movie_delete(request, id):
    data = {}

    try:
        movies = Movies.objects.get(movie_Id=id)

        user = request.user

        if user.is_superuser:
            action = movies.delete()
            if action:
                data["success"] = "Delete Successful!"
                response_status = status.HTTP_200_OK
            else:
                data["failure"] = "Delete Unsuccessful!"
                response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            data["Error"] = "Un-authorized"
            response_status = status.HTTP_401_UNAUTHORIZED

    except Movies.DoesNotExist:
        data["Error"] = "Movie Does Not Exist"
        response_status = status.HTTP_404_NOT_FOUND

    return Response(data=data, status=response_status)



@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_movie_create(request):
    data = {}
    request_data = {}

    user = request.user

    if user.is_superuser:

        # This is done because input json has 99popularity as key which cannot be a var in python,thus added _99popularity.
        request_data["_99popularity"] = request.data["99popularity"]
        request_data.update(request.data)

        # Using Sqllite3 in which we can't store array so have convert list as string
        request_data["genre"] = ''.join(request.data["genre"])

        serializer = MoviesSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            data["success"] = serializer.data
            response_status = status.HTTP_201_CREATED
        else:
            data["failure"] = serializer.errors
            response_status = status.HTTP_400_BAD_REQUEST

    else:
        data["Error"] = "Un-authorized"
        response_status = status.HTTP_401_UNAUTHORIZED

    return Response(data=data,status= response_status)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_movie_create_bulk(request):
    bulk_data = request.data['data']

    data = {}

    response_status = status.HTTP_500_INTERNAL_SERVER_ERROR

    user = request.user

    if user.is_superuser:

        for single_data in bulk_data:

            # This is done because input json has 99popularity as key which cannot be a var in python,thus added _99popularity.
            single_data["_99popularity"] = single_data["99popularity"]

            # Using Sqllite3 in which we can't store array so have convert list as string
            single_data["genre"] = ''.join(single_data["genre"])

            serializer = MoviesSerializer(data=single_data)
            if serializer.is_valid():
                serializer.save()
                data[single_data["name"]] = "Create Successful!"
            else:
                data[single_data["name"]] = "Create Unsuccessful!"

            response_status = status.HTTP_200_OK

    else:
        data["Error"] = "Un-authorized"
        response_status = status.HTTP_401_UNAUTHORIZED

    return Response(data=data,status=response_status)


@api_view(["POST"])
@permission_classes((AllowAny,))
def get_admin_token(request):
    data = {}

    print(request.data)

    if request.content_type == "application/json":
        username = request.data["username"]
        password = request.data["password"]
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user:
        if user.is_superuser:
            try:

                token, created = Token.objects.get_or_create(user=user)
                data["token"] = token.key
                response_status = status.HTTP_200_OK

            except Token.DoesNotExist:
                data["Error"] = "Token Not Generated, Please Login!"
                response_status = status.HTTP_404_NOT_FOUND

        else:
            data["Error"] = "Un-authorized"
            response_status = status.HTTP_401_UNAUTHORIZED


    else:
        data["Error"] = "User DoesNot Exist"
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(data=data, status=response_status)
