FROM python:latest
COPY shop/requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /usr/app

COPY ./docker/shop/docker-entrypoint.sh ./docker/shop/wait-for-command.sh ./docker/shop/runserver.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh /runserver.sh

COPY shop /usr/app

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["sh /runserver.sh"]

