#FROM python:3-onbuild
FROM python:3
COPY . /app
EXPOSE 5000
CMD python ./server.py