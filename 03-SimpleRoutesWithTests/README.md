# Flask Example 03 - Simple Routes with Tests

Example 3 contains the same routes as Example 2.  The difference is the inclusion of `testRoutes.http` containing tests for the routes. To execute these, you'll need to add the `REST Client` extension in VS Code. 

## Prerequisites
- Install REST Client in VS Code
  - Click the Extensions icon on the left ![the extension icon](images/ext-icon.png)
  - In the search bar at the top, type `rest client`. 
  - As long as results are sorted by popularity/installs, `REST Client` should be at the top of the list. The author is Huachao Mao.  It should show > 3M installs. 
  - Click on the extension, then choose `Install`.  A restart of VS Code may be required after install to load the extension. 

## To Run the Flask App
- `python app.py`

## To Test The Routes
- Make sure the REST Client extension is installed and activated
- Open the `testRoutes.http` file
- Above each test, you should see a clickable `Send Request` message

## Routes
- `GET /`
  - returns a Hello World message
- `GET /bigHello`
  - returns a greeting to the user
- `GET /users/<idNumber>`
  - includes a variable in the route (`<idNumber>`) 
  - notice the variable also appears as a parameter to the function `handle_user_with_id`
  - `idNumber` is accessed with curly braces (`{}`) in the handler

## Prerequisites
- Flask must be installed

## To Run:
`python app.py`