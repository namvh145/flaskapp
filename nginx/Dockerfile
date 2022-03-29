FROM alpine:latest

RUN apk --update add nginx &&\
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log &&\
    mkdir /etc/nginx/sites-enabled/ &&\
    mkdir -p /run/nginx &&\
    rm -rf /etc/nginx/conf.d/default.conf && \
    rm -rf /var/cache/apk/* && \
    rm -rf /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY conf.d/* /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx

EXPOSE 80

#VOLUME ./nginx/logs /var/log/nginx

CMD ["nginx", "-g", "daemon off;"]