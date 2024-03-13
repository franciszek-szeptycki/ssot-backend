FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY server /app
COPY .env /app/.env

RUN python manage.py collectstatic --noinput
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

CMD ["/app/entrypoint.sh"]
