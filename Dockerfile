FROM python:3.8-alpine

WORKDIR /home/app

COPY . .

RUN python -m venv venv

RUN pip install -e .
RUN pip install gunicorn

RUN chmod +x boot.sh

EXPOSE 2000

ENTRYPOINT ["./boot.sh"]
