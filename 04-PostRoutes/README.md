# Adding a Post Route


This example adds a simple Post Route the `/products`.  Right now, all it does is print out the JSON payload of the http request object and return a success string.  

In Thunder Client, I added a new Collection for this example.  A Collection is a grouping of requests.  It helps with organization.  Additionally, you can run all requests that are part of a collection at the same time without having to click on each of them individually.  

In the new request, note that the HTTP method has been changed to POST.  Usually, POST routes contain information in the body of the request object. In Thunderclient, click on `Body` tab under the URI field.  Then choose the Json tab under that.  You should see some basic JSON for Sharp Cheddar.  That JSON will be sent along to the server (app.py) when you hit send.  

## Testing This Example

1. Start the app.py with `python app.py`
1. Open Thunder Client in VsCode
1. Choose Collections
1. Expand `Test for Ex 04` Collection
1. Click on **New Product request POST** request
1. Check out the JSON in Body of the request
1. Click send
1. You should see the JSON printed in the terminal running app.py. 