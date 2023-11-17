# same base container as the frontend to save traffic and space 
FROM python:3.12-slim-bookworm
RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip
WORKDIR /srv/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_PASSWORD
ARG DJANGO_SUPERUSER_USERNAME
RUN chmod +x startapp.sh
EXPOSE 7654
CMD ["sh", "startapp.sh"]