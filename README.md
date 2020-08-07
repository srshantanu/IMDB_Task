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
 
----
* **Question:**
    `Once deployed suppose this application became very famous and started to receive a ton of traffic. 
    Your application now contains metadata about 5M movies and receives 15M API hits per day both from anonymous 
    as well as authenticated users. 
    Suggest an architecture to scale up this system to 5x of these specs. 
    You can also think of potential bottlenecks at all layers of the stack and how will you solve for these.`
    
    **Answer**
    
    * Load Balancer
    
        It is needed if we have so many requests which can not be handled by one web server. 
        Typically 10-15k requests per second i.e Million of requests per day can be handled by one web server for a dynamic website, 
        but it depends totally on complexity of website/web application. 
        Load balancer contains multiple web servers and just forwards incoming requests to one of them to distribute.
    
    * Web Server
    
        we can tune the configuration of web server according to your use case. 
        Set number of threads, connections, network buffer size, open file descriptor etc. 
        Different servers have different configuration files to tune the performance.
    
    * MySql/database
    
        Each web server must serve same content, hence should talk to same database. 
        If many web server talking to one db server, it will become bottle neck. 
        Even if there is one web server, sometimes db server may become bottle neck. 
        mysql server supports master-slave and master-master configuration.
    
        * In master-slave one server is master where data is written and it is replicated to multiple slave servers. 
        In this case write is done on master and read from slaves. 
        This is useful when very few write happens on database but many reads. 
        typically less than 10-15% of write but depends on the use case.
    
        * In master-master is similar to above but all are masters, any data written to any server gets replicated to other servers. 
        Read and write can be done on any server. This is useful for applications which have high writes.
        Above is for mysql but similar kind of scalability is supported by other database servers too.
    
    * Caching Server
    
        Reading from disk(db) is expensive(high latency). Here caching server comes to help you. They cache fraction of 
        data(recently accessed) to the memory(low latency). If data is there in cache(hit), then disk read is saved, 
        if it is not(miss) then read from disk and save it in cache for next time. 
        If you get 70-80% hit ratio then it will help in scaling.
        Also keep all of above servers in same LAN close to each other in high speed LAN so that when they communicate, 
        netword doesn't become bottle neck.
    
    * Separate cdn server
    
        To server static content(js, css, images) setup a cdn server which is optimized to serve static content. 
        This will reduce load from web server.

**Note** Image Representation of above explanation I'll attach in sometime.