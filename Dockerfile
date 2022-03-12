FROM python:slim
ENV PYTHONUNBUFFERED 1
RUN apt-get update

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate --noinput
# CMD ["python","manage.py","runserver"]

