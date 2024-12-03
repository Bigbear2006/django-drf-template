FROM python:alpine

WORKDIR app

COPY requirements/prod.txt requirements/prod.txt
RUN pip install --upgrade pip && pip install -r requirements/prod.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]