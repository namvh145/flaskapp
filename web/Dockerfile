FROM python:3
RUN apt-get update && apt-get install -y nginx

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ../app/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY nginx.conf /etc/nginx/sites-enabled/default

RUN python3 StudentDB.py

CMD ["/bin/bash", "start.sh"]
EXPOSE 80
