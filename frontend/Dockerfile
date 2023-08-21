# syntax=docker/dockerfile:1
FROM nginx

# ENV DEBIAN_FRONTEND=noninteractive
ENV default-time-zone=America/Recife
ENV SET_CONTAINER_TIMEZONE=true
ENV CONTAINER_TIMEZONE="America/Recife"
ENV TZ="America/Recife"
RUN ln -snf /usr/share/zoneinfo/America/Recife /etc/localtime && echo America/Recife > /etc/timezone

RUN --network=default

COPY build /usr/share/nginx/html

EXPOSE 80
