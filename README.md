## Deployment Details
FastAPI applications can be deployed using the `uvicorn` ASGI in combination with `gunicorn` WSGI.
This could be setup to run in a container. The port could then be forwarded publicly using Nginx.
