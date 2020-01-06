FROM python:3.7

COPY ./django_practice  app/django_practice
COPY ./templates app/templates
COPY ./manage.py app/

RUN pip install -r app/django_practice/requirements.txt

WORKDIR /app

EXPOSE 8000

CMD python manage.py runserver 0:8000

