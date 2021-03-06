FROM python:3.8-slim-buster as builder
ARG PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
FROM builder
COPY . /test
WORKDIR /test
ENTRYPOINT ["python"]
CMD ["run.py","run2.py"]
