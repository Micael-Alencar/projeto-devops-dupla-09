FROM python:3.12-slim 
ARG APP_VERSION=v0
ENV APP_VERSION=$APP_VERSION
WORKDIR /app 
COPY app/requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
COPY app/ . 
EXPOSE 5009 
CMD ["python", "app.py"] 