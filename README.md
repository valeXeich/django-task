# Django registration via telegram

Deployed: https://django-backend-production.up.railway.app/

STACK:

1. Djnago
2. aiogram
3. PostgreSQL

To run locally you need:

1. Create django-variables.env and aiogram-variables.env files in the project root folder and fill with their values

django-variables.env
```python
SECRET_KEY= ...
POSTGRES_USER= ...
POSTGRES_PASSWORD= ...
POSTGRES_DB= ...
POSTGRES_HOST= ...
POSTGRES_PORT= ...
```

aiogram-variables.env
```python
TOKEN= ...
```

2. Start containerization of the project

  ```bash
   $ docker-compose up
  ```


