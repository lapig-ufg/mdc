FROM debian:buster-slim

LABEL maintainer="Renato Gomes <renatogomessilverio@gmail.com>"

ENV URL_TO_APPLICATION_GITHUB="https://github.com/lapig-ufg/mdc.git"
ENV BRANCH="master"

WORKDIR /APP/mdc

COPY ./requirements.txt /tmp 
RUN apt-get update && apt-get install   -y apt-transport-https ca-certificates wget dirmngr gnupg software-properties-common \
                                        sudo unzip python2 procps python-gdal python-pip gdal-bin net-tools vim redis-server git && \
                                        pip install -U pip setuptools && \
                                        wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add - && \
                                        add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/ && \
                                        apt-get update && apt-get install -y adoptopenjdk-8-hotspot && \
                                        mkdir -p /APP && cd /APP && git clone -b ${BRANCH} ${URL_TO_APPLICATION_GITHUB}
ADD ./dockerfiles/redis.conf /etc/redis
ADD ./dockerfiles/start.sh   /APP 

RUN chown redis:redis /etc/redis/redis.conf && \
    pip install -r /tmp/requirements.txt && \
    chmod +x /APP/start.sh && \
    cd /APP/mdc && mv MRT.zip /tmp && cd /tmp && unzip MRT.zip && \
    cd MRT/ && mv MRT/ /APP/mdc && mkdir -p /APP/sits-workdir/ && \
    rm -rf /tmp/* && rm -rf /var/lib/apt/lists/*  

CMD [ "/bin/bash", "-c", "/APP/start.sh; tail -f /dev/null"]
