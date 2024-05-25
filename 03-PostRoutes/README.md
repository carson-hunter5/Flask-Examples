# Adding a Post Route


This example adds adds a route to return an HTML form from the `templates` folder.  That form send the form data back as a POST request to `/userInfo`.  Right now, all it does is print out the JSON payload of the http request object and return a success message in JSON.  
    

## Testing This Example

1. Start the app.py with `python app.py`
1. Open a browser and go to `http://127.0.0.1:4000/userForm`
1. Fill out the form and click the Submit Button.
1. You should see a Success message under the Submit Button. 
1. Check the terminal where you ran `app.py` and you should see the values you typed in.