FROM python:3.6.6-slim
LABEL maintainer="NoCLin"

RUN set -ex && \
    apt-get update -yqq && \
	apt-get install -yqq \
	    git \
	    curl \
	     && \
    pip install pipenv  -i https://pypi.doubanio.com/simple/
#postgresql-dev \

COPY Pipfile* /app
WORKDIR /app
RUN set -ex && \
    pipenv install --system

COPY . /app
RUN set -ex && \
    chmod +x "/app/docker-entrypoint.sh"

ENTRYPOINT ["/app/docker-entrypoint.sh"]