FROM python:latest

COPY stockroom/requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /usr/app

COPY ./docker/stockroom/docker-entrypoint.sh ./docker/stockroom/wait-for-command.sh ./docker/stockroom/runserver.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh /runserver.sh

COPY stockroom /usr/app

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["sh /runserver.sh"]

