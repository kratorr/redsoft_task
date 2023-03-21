FROM python:3.10.10-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --upgrade pip && \
     pip3 install -r requirements.txt --no-cache-dir

COPY . /app/

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]