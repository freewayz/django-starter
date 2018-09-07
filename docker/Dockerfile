FROM python:3.6-alpine3.6
MAINTAINER Edache Peter

ENV DOCKYARD_HOME=/src
ENV DOCKYARD_SRC=/src/webapp/{{ project_name | lower }}
ENV DJANGO_SETTINGS_MODULE={{ project_name | lower }}.settings.prod

WORKDIR $DOCKYARD_HOME

COPY {{ project_name | lower }}-0.0.1.tar.gz $DOCKYARD_SRC/


RUN pip install $DOCKYARD_SRC/{{ project_name | lower }}-0.0.1.tar.gz
EXPOSE 8000

WORKDIR $DOCKYARD_SRC
COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]
