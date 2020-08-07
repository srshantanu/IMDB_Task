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
          **Content:** `{ error : "User DoesNot Exist" }`
      
    
    * **Sample Call:**
        
        Add above URL in Postman