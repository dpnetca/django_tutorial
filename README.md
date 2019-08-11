# Django Tutorial

Repository to store my progress learning Django web framework, and proper techniques to secure and deploy to production.  

## Projects:
### Local Library:
roughly based on this tutorial:
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website

### MySite:
roughly based on this tutorial:
https://docs.djangoproject.com/en/2.2/intro/tutorial01/

### django_docker
experimenting with creating a 3 tier docker deployment  for a simple django app

roughly based on a few guides (can't remember which all I sed components from for sure)
https://blog.devartis.com/django-development-with-docker-a-completed-development-cycle-7322ad8ba508
https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
and / or:
various youtube videos

.env, .env.db files normally should be kept out of git repo, included here for example purposes
secret.env and secret.env.db used in "prod" docker images contain more secure information and are excluded
