# B6.13
  1. The web server accepts GET requests for /albums/<artist> and displays a message on the screen with the number of albums by artist artist and a list of those album titles. 
  
  2. The web server accepts POST requests to /albums/ and stores the user's submitted album data. 
The data is transmitted in web form format. If the user tries to submit data about an album that is already in the database, the request handler responds with an HTTP 409 error and displays a message accordingly. 
To form a POST request to the server, you can use the already familiar http utility. Let's say we started the server at http://localhost:8080. 
Then the requests will look like this:  http -f POST http://localhost:8080/albums artist = "New Artist" genre = "Rock" album = "Super" Complete the list of passed parameters, if necessary.  

  3. The set of fields in the transmitted data fully corresponds to the schema of the album table of the database.
  4. Use the albums.sqlite3 file as a source database. 
  5. Before trying to save the data submitted by the user, you need to validate it. 
Check, for example, that the actual year is passed in the "year of manufacture" field.
