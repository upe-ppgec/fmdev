# syntax=docker/dockerfile:1
FROM ubuntu:18.04

COPY backend /root/fmdev/backend
COPY start.sh /root/fmdev

# ENV DEBIAN_FRONTEND=noninteractive
ENV default-time-zone=America/Recife
ENV SET_CONTAINER_TIMEZONE=true
ENV CONTAINER_TIMEZONE="America/Recife"
ENV TZ="America/Recife"
RUN ln -snf /usr/share/zoneinfo/America/Recife /etc/localtime && echo America/Recife > /etc/timezone

ENV VIRTUAL_ENV=/root/fmdev/backend/venv
ENV PATH="${PATH}:${VIRTUAL_ENV}/bin"

RUN --network=default

RUN apt-get update -y && apt-get install -y build-essential checkinstall libbz2-dev libc6-dev libffi-dev libgdbm-dev liblzma-dev libncursesw5-dev libreadline-gplv2-dev libsqlite3-dev libssl-dev software-properties-common tk-dev tzdata wget zlib1g-dev

RUN cd /usr/src && wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz
RUN cd /usr/src && tar xzf Python-3.7.6.tgz
RUN cd /usr/src/Python-3.7.6 && ./configure --enable-optimizations
RUN cd /usr/src/Python-3.7.6 && make altinstall

RUN cd /root/fmdev && wget https://bootstrap.pypa.io/get-pip.py
RUN cd /root/fmdev && python3.7 get-pip.py

RUN cd /root/fmdev/backend && python3.7 -m venv ${VIRTUAL_ENV}
# RUN cd /root/fmdev/backend && source /root/fmdev/backend/venv/bin/activate
RUN cd /root/fmdev/backend && pip install -r requirements.txt
RUN cd /root/fmdev/backend && pip install flask flask_migrate flask_script python-dotenv

RUN cd /root/fmdev/backend && python3.7 /root/fmdev/backend/migrate.py db stamp head
RUN cd /root/fmdev/backend && python3.7 /root/fmdev/backend/migrate.py db migrate
RUN cd /root/fmdev/backend && python3.7 /root/fmdev/backend/migrate.py db upgrade

RUN /bin/chmod +x /root/fmdev/start.sh
CMD ["/root/fmdev/start.sh"]

EXPOSE 5000

# STOPSIGNAL SIGKILL
