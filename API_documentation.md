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
      
    *  **URL Params**
    
       `None`
    
       **Required:**
     
       `None`
    
       **Optional:**
     
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