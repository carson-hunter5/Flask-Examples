# Flask Example 02 - Simple Routes

Example 2 contains a few more routes. 

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