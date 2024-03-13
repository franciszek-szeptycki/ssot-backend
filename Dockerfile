FROM python:3.10-alpine

WORKDIR /app

COPY server/requirements.txt /app
RUN pip install -r requirements.txt

COPY django_web_app /app

RUN python manage.py collectstatic --noinput
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

CMD ["/app/entrypoint.sh"]