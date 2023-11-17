# project setup documentation

## django basic setup

- create conda environment:
  - ``conda create -n dj5py312 python=3.12``

- install django 5 with pip:
  - ``pip install django==5.0a1``

- start django project:

  ```bash
  mkdir app
  django-admin startproject dj5py312project app
  cd app
  python manage.py startapp api
  ```

- add app to project settings.py:

  ```python
  INSTALLED_APPS = [
      "api",
      ...
  ]
  ```

- migrate and run local dev server:

  ```bash
  python manage.py migrate
  ```

## docker setup

- target image to use is ``3.12-slim-bookworm``
- ...
