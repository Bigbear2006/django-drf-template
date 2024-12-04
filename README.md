# Django + Django REST Framework template

## CI/CD badges
[![pipeline Status](https://github.com/Bigbear2006/django-drf-template/actions/workflows/check.yml/badge.svg)](https://github.com/Bigbear2006/django-drf-template/actions/workflows/check.yml/badge.svg)
[![pipeline Status](https://github.com/Bigbear2006/django-drf-template/actions/workflows/deploy.yml/badge.svg)](https://github.com/Bigbear2006/django-drf-template/actions/workflows/deploy.yml/badge.svg)

## Languages
![Languages](https://img.shields.io/badge/Languages-3-blue?logo=github)
![Python](https://img.shields.io/badge/Python-3.11-FFD343?logo=python&logoColor=blue)
![Dockerfile](https://img.shields.io/badge/Dockerfile-Docker-2496ED?logo=docker&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-Script-4EAA25?logo=shell&logoColor=white)

## Clone repository
`git clone https://github.com/Bigbear2006/django-drf-template.git`

## Generate Django SECRET_KEY
```shell
python -m venv myenv
venv\Scripts\activate
pip install -r .\backend\requirements\dev.txt
django-admin shell
```

```python
from django.core.management.utils import get_random_secret_key
print('django-insecure-' + get_random_secret_key())
exit()
```

## Create .env file
```
SECRET_KEY=YOUR_GENERATED_SECRET_KEY
ALLOWED_HOSTS=127.0.0.1,0.0.0.0,localhost

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_complex_password
```

## Run
`docker-compose up --build -d`

## Make migrations and migrate
```shell
docker-compose exec backend python manage.py makemigrations jwt_auth
docker-compose exec backend python manage.py migrate
```

## See the logs
`docker-compose logs`