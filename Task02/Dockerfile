FROM python:3.11-slim
RUN apt-get update && apt-get -y install \
    vim \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN pip install faker
RUN pip install requests
ADD . /app
WORKDIR /app
CMD python etl.py