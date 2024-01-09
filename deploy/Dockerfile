FROM python:3.9.16-slim

LABEL maintainer="bensong2017@gmail.com"

#COPY ./deploy/ /start.sh
#RUN chmod +x /start.sh
#
#COPY ./deploy/gunicorn_conf.py /app/gunicorn_conf.py

COPY ./ /app
RUN chmod +x /app/deploy/start.sh \
    && pip install --no-cache-dir -r /app/requirements.txt
WORKDIR /app

ENV PYTHONPATH=/app

EXPOSE 9000

# And start Gunicorn with Uvicorn
CMD ["/app/deploy/start.sh"]