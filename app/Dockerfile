FROM python:3.6.8-alpine3.9
ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

RUN pip install --upgrade pip

ADD . /var/www/
RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 9001 9002

CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:9001", "wsgi"]
#CMD ["flask", "run", "-p", "9001"]
#CMD ["gunicorn", "-w", "4", "--bind", "127.0.0.1:9002", "wsgi"]