FROM nginx:alpine

RUN rm -f /etc/nginx/conf.d/*

COPY nginx.conf /etc/nginx/conf.d/

RUN mkdir -p /usr/share/nginx/html/static
