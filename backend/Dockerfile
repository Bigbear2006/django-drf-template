FROM python:alpine

WORKDIR app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]