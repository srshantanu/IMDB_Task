# IMDB Task

● Problem Description:

. Create a RESTful API for movies(something similar to IMDB). For this we would like you to use:

1. MySql or SQLlite to store data
2. Any Python Framework for implementing the APIs.

There need to be 2 levels of access:
admin = who can add, remove or edit movies.
users = who can just view the movies.

. There should also be a decent implementation to search for movies.

. Document your code well so that we can test the API with ease.

. For your convenience I have attached some data that you can use to populate your database

. Try and deploy this on Heroku. Ensure that you parse the JSON file and ingest it into the application deployed on Heroku.

. Feel free to add features!

------------------------------------------------------------------------------------------------------------------------
Implementation as Follows :

Framework for API :

    . Django
    . Django REST Framework

Database for API :
    
    .SQLlite (for Heroku server, as it doesn't support MySQL)
    .MySQL   (Locally as it gives better read and write speed)

    Note : I have attached basic DB schema named :  imdb_db_schema.pdf
 
List of API :
    
    . Admin User :
        
            https://imdbfyndtask.herokuapp.com/api/movie/get_admin_token
