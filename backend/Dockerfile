FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY docker-entrypoint.sh /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "docker-entrypoint.sh"]