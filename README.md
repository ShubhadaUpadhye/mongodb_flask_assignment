# mongodb_flask_assignment

#Setup
1. Create a new Python virtual environment and activate it.
2. Install Flask, Flask-RESTful, and PyMongo libraries using pip
3. Create a new MongoDB database and collection for the application by following the given procedure:
•	Sign in to your MongoDB Atlas online or install MongoDB locally.
•	Set the MongoDB URI and database name in the Flask application configuration.
•	Create a new database with any name of your choice.
•	Within the new database created, create a collection with any name of your choice.
4. Install Postman for testing the REST API endpoints.

#Application 
Now, let's set up a Flask application with Flask-RESTful and Flask-Blueprint, integrating MongoDB
1. Create a new Python file, e.g., app.py.
2. Import the necessary libraries and modules
3. Create a Flask application instance
4. Configure the MongoDB connection using the Flask application configuration using your MongoDB connection string.
5. Initialize the Flask-PyMongo extension with your Flask application instance.
6. Create Blueprint , Flask-RESTful Resource and register the resource.
7. Run the Flask application.

##Testing part
1. Open Postman and test the API endpoint.
2. Create a new HTTP request for each of the REST API endpoints.
3. Send requests to the endpoints to test the CRUD operations on the User resource.

4. Monitor database to check if the data is updated correctly.


