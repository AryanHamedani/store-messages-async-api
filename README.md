# store-messages-async-api
This is a Flask project with three endpoints. The first endpoint generates a JWT token, powered by Flask-JWT. The second endpoint retrieves messages from a MongoDB database, and the third endpoint uses Celery and async to add new messages to the database. Redis is used as a message broker for this project.
