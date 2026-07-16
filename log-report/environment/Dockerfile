FROM python:3.12.8@sha256:e74938514dc67ad3eade8798aa929f5dd569e463758c83243636d4e1b54aa559

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
