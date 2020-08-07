**IMDB REST API**
----

 This documents gives the list of REST API uploaded on Heroku, used to make all GET and POST request according to user.
    
 * **Notes:**
 
   In Postman, request body use raw format with content-type = application/json
   
---

**ADMIN USER**

1. **Generate Token** : Used to Create, Update, Delete Movie
    
    * **URL**
    
      https://imdbfyndtask.herokuapp.com/api/movie/get_admin_token
    
    * **Method:**
      
      `POST`
    *  **URL Header**
        
        `None`
      
    *  **URL Params**
    
       `None`
    
    * **Data Params**
    
      `username`
      `password`
    
      **Required:**
         
       `username`
       `password`
       
      **Optional:**
        
      `None`
    
    * **Success Response:**
     
      * **Code:** 200 <br />
        **Content:**  `{"token": "4eba26e991f07175405ce3fc857fdd07c81d2354"}`
     
    * **Error Response:**
    
        
      * **Code:** 401 UNAUTHORIZED <br />
        **Content:** `{ error : "Un-authorized" }`
    
      OR
    
      * **Code:** 404 NOT FOUND <br />
        **Content:** `{ error : "Token Not Generated, Please Login!" }`
      
      OR
      
      * **Code:** 400 BAD REQUEST <br />
          **Content:** `{ error : "User DoesNot Exist" }`
      
    
    * **Sample Call:**
        
        Add above URL in Postman

2. **Create Movie** : Used to Create Single Movie
    
    * **URL**
    
      https://imdbfyndtask.herokuapp.com/api/movie/create
    
    * **Method:**
      
      `POST`
    
    *  **URL Header**
        
        `Authorization`
        * Key - "Token 7aXXXX3cd1c7f6feXXXX07e21ea4XXX23XXX960"
        
    *  **URL Params**
    
       `None`
    
    * **Data Params**
    
      `99popularity`
      `director`
      `genre`
      `imdb_score`
      `name`
    
      **Required:**
         
       `99popularity`
       `director`
       `genre`
       `imdb_score`
       `name`
       
      **Optional:**
        
      `None`
    
    * **Success Response:**
     
      * **Code:** 201 <br />
        **Content:**  `{
                           "success": {
                               "movie_Id": "b59bd2e7-bf97-4d97-b73a-e1a3e3bb4e68",
                               "name": "Cabiria",
                               "director": "Giovanni Pastrone",
                               "genre": "Adventure Drama War",
                               "imdb_score": 6.6,
                               "_99popularity": 66.0
                           }
                       }`
                       
     
    * **Error Response:**
    
        
      * **Code:** 401 UNAUTHORIZED <br />
        **Content:** `{ error : "Un-authorized" }`
      
      OR
      
      * **Code:** 400 BAD REQUEST <br />
          **Content:** `{
                            "failure": {
                                "name": [
                                    "This field is required."
                                ]
                            }
                        }`
      
    
    * **Sample Call:**
        
        Add above URL in Postman

3. **Create Bulk Movie** : Used to Create Bulk Movie
    
    * **URL**
    
      https://imdbfyndtask.herokuapp.com/api/movie/bulk_create
    
    * **Method:**
      
      `POST`
    
    *  **URL Header**
        
        `Authorization`
        * Key - "Token 7aXXXX3cd1c7f6feXXXX07e21ea4XXX23XXX960"
        
    *  **URL Params**
    
       `None`
    
    * **Data Params**
    
      `data`
    
      **Required:**
         
       `data`
       
      **Optional:**
        
      `None`
    
    * **Success Response:**
     
      * **Code:** 201 <br />
        **Content:**  `{
                           "The Wizard of Oz": "Create Successful!",
                           "Star Wars": "Create Successful!",
                           "Cabiria": "Create Successful!",
                           "Psycho": "Create Successful!",
                           "King Kong": "Create Successful!",
                           "Metropolis": "Create Successful!",
                           "Star Trek": "Create Successful!",
                           "Casablanca": "Create Successful!"
                       }`
     
    * **Error Response:**
    
        
      * **Code:** 401 UNAUTHORIZED <br />
        **Content:** `{ error : "Un-authorized" }`
      
      OR
      
      * **Code:** 500 INTERNAL SERVER ERROR <br />
          **Content:** `{"error" : "Data List Empty"}`
      
    
    * **Sample Call:**
        
        Add above URL in Postman
    
   * **Note :**
        
        * Sample Data format :
            `{
                 "data": [
                     {
                         "99popularity": 83,
                         "director": "Victor Fleming",
                         "genre": [
                             "Adventure",
                             " Family",
                             " Fantasy",
                             " Musical"
                         ],
                         "imdb_score": 8.3,
                         "name": "The Wizard of Oz"
                     },
                     {
                         "99popularity": 88,
                         "director": "George Lucas",
                         "genre": [
                             "Action",
                             " Adventure",
                             " Fantasy",
                             " Sci-Fi"
                         ],
                         "imdb_score": 8.8,
                         "name": "Star Wars"
                     }
                 ]
            }`
            
4. **Update Movie** : Used to Update Single Movie
    
    * **URL**
    
      https://imdbfyndtask.herokuapp.com/api/movie/<movie_Id>/update
      
      * e.g : `https://imdbfyndtask.herokuapp.com/api/movie/6dd3c9e5823841a18a81f2b5f5eacc26/update`
    
    * **Method:**
      
      `PUT`
    
    *  **URL Header**
        
        `Authorization`
        * Key - "Token 7aXXXX3cd1c7f6feXXXX07e21ea4XXX23XXX960"
        
    *  **URL Params**
    
       `None`
    
    * **Data Params**
    
      `99popularity`
      `director`
      `genre`
      `imdb_score`
      `name`
    
      **Required:**
         
       `99popularity`
       `director`
       `genre`
       `imdb_score`
       `name`
       
      **Optional:**
        
      `None`
    
    * **Success Response:**
     
      * **Code:** 200 <br />
        **Content:**  `{
                           "success": "Update Successful!"
                       }`
     
    * **Error Response:**
    
        
      * **Code:** 401 UNAUTHORIZED <br />
        **Content:** `{ "error" : "Un-authorized" }`
      
      OR
      
      * **Code:** 400 BAD REQUEST <br />
          **Content:** `{ "error" : "User DoesNot Exist" }`
      
      OR
      
      * **Code:** 404 NOT FOUND <br />
          **Content:** `{ "error" : "Movie Does Not Exist" }`
      
    
    * **Sample Call:**
        
        Add above URL in Postman

5. **Delete Movie** : Used to Delete Single Movie
    
    * **URL**
    
      https://imdbfyndtask.herokuapp.com/api/movie/<movie_Id>/delete
      *e.g : `https://imdbfyndtask.herokuapp.com/api/movie/6dd3c9e5823841a18a81f2b5f5eacc26/delete`
    
    * **Method:**
      
      `DELETE`
    
    *  **URL Header**
        
        `Authorization`
        * Key - "Token 7aXXXX3cd1c7f6feXXXX07e21ea4XXX23XXX960"
        
    *  **URL Params**
    
       `None`
    
    * **Data Params**
        
      `None`
    
    * **Success Response:**
     
      * **Code:** 200 <br />
        **Content:**  `{
                           "success": "Delete Successful!"
                       }`
     
    * **Error Response:**
    
        
      * **Code:** 401 UNAUTHORIZED <br />
        **Content:** `{ "error" : "Un-authorized" }`
      
      OR
      
      * **Code:** 404 NOT FOUND <br />
          **Content:** `{ "error" : "Movie DoesNot Exist" }`
      
      OR
      
      * **Code:** 500 INTERNAL SERVER ERROR <br />
                **Content:** `{ "error" : "Delete Unsuccessful!"}`
      
    
    * **Sample Call:**
        
        Add above URL in Postman
----

**ALL USER**

1. **All Movie list** : This is used to get all movies in DB using Pagination.
    
    * **URL**
    
      https://imdbfyndtask.herokuapp.com/api/movie/all
    
    * **Method:**
      
      `GET`
      
    *  **URL Header**
        
        `None`
      
    *  **URL Params**
    
       `page`
       
       * note : Used If result is paginated
    
    * **Data Params**
        
      **Required:**
        `None`
           
      **Optional:**
            
        `page`
    
    * **Success Response:**
     
      * **Code:** 200 <br />
        **Content:**  `{
                           "count": 248,
                           "next": "http://127.0.0.1:8000/api/movie/all?page=2",
                           "previous": null,
                           "results": [
                               {
                                   "movie_Id": "6dd3c9e5-8238-41a1-8a81-f2b5f5eacc26",
                                   "name": "The Wizard of Oz update",
                                   "director": "Giovanni Pastrone update",
                                   "genre": "Adventure Drama War",
                                   "imdb_score": 6.6,
                                   "_99popularity": 66.0
                               },
                               {
                                   "movie_Id": "28c33c21-6f16-45f8-b6e7-04e351a08b49",
                                   "name": "Star Wars",
                                   "director": "George Lucas",
                                   "genre": "Action Adventure Fantasy Sci-Fi",
                                   "imdb_score": 8.8,
                                   "_99popularity": 88.0
                               }
                           ]
                       }`
     
    * **Error Response:**
    
      * **Code:** 404 NOT FOUND <br />
        **Content:** `{ error : "Movie Not Found" }`
      
    * **Sample Call:**
        
        Add above URL in Postman

3. **Search & Filter Movies** : This is used to search and filter movies according the text given,
                                Paginated if result is large.
    
    * **URL**
    
      https://imdbfyndtask.herokuapp.com/api/movie/search?search=&ordering=
      
      * e.g: `https://imdbfyndtask.herokuapp.com/api/movie/search?search=Wizard&ordering=-imdb_score`
    
    * **Method:**
      
      `GET`
      
    *  **URL Header**
        
        `None`
      
    *  **URL Params**
    
       `search` 
       `ordering`
       `page`
       
       **Required:**
       
       `None`
       
       **Optional**
       
       `search`
       `ordering`
       `page`
      
    * **Data Params**
        `None`
    
    * **Success Response:**
     
      * **Code:** 200 <br />
        **Content:**  `{
                           "count": 2,
                           "next": null,
                           "previous": null,
                           "results": [
                               {
                                   "movie_Id": "c0f8bb65-acc9-4e74-bb05-a4258c6cc138",
                                   "name": "The Wizard of Oz",
                                   "director": "Victor Fleming",
                                   "genre": "Adventure Family Fantasy Musical",
                                   "imdb_score": 8.3,
                                   "_99popularity": 83.0
                               },
                               {
                                   "movie_Id": "c2a6a7a2-40b1-40b0-8913-52e0de8f25d4",
                                   "name": "The Wizard of Oz",
                                   "director": "Larry Semon",
                                   "genre": "Comedy Family Fantasy Adventure",
                                   "imdb_score": 5.3,
                                   "_99popularity": 53.0
                               }
                           ]
                       }`
     
    * **Error Response:**
    
      * **Code:** 404 NOT FOUND <br />
        **Content:** `{ error : "Movie DoesNot Exist" }`
      
    * **Sample Call:**
        
        Add above URL in Postman

1. **All Movie list** : This is used to get all movies in DB using Pagination.
    
    * **URL**
    
      https://imdbfyndtask.herokuapp.com/api/movie/all
    
    * **Method:**
      
      `GET`
      
    *  **URL Header**
        
        `None`
      
    *  **URL Params**
    
       `page`
       
       * note : Used If result is paginated
    
    * **Data Params**
        
      **Required:**
        `None`
           
      **Optional:**
            
        `page`
    
    * **Success Response:**
     
      * **Code:** 200 <br />
        **Content:**  `{
                           "count": 248,
                           "next": "http://127.0.0.1:8000/api/movie/all?page=2",
                           "previous": null,
                           "results": [
                               {
                                   "movie_Id": "6dd3c9e5-8238-41a1-8a81-f2b5f5eacc26",
                                   "name": "The Wizard of Oz update",
                                   "director": "Giovanni Pastrone update",
                                   "genre": "Adventure Drama War",
                                   "imdb_score": 6.6,
                                   "_99popularity": 66.0
                               },
                               {
                                   "movie_Id": "28c33c21-6f16-45f8-b6e7-04e351a08b49",
                                   "name": "Star Wars",
                                   "director": "George Lucas",
                                   "genre": "Action Adventure Fantasy Sci-Fi",
                                   "imdb_score": 8.8,
                                   "_99popularity": 88.0
                               }
                           ]
                       }`
     
    * **Error Response:**
    
      * **Code:** 500 INTERNAL SERVER ERROR <br />
        **Content:** `{ "error" : "Error Message" }`
      
    * **Sample Call:**
        
        Add above URL in Postman