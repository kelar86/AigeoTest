FROM python:3-onbuild
ENV PYTHONUNBUFFERED 1
ADD . /map_service/
WORKDIR /map_service


ADD requirements.txt /map_service/
RUN pip install -r requirements.txt

