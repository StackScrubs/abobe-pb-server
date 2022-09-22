FROM python:alpine

WORKDIR /app

EXPOSE 5000
ENV FLASK_APP=app.py

COPY ./app.py /app
COPY ./requirements.txt /app
#COPY . /app
RUN pip install -r requirements.txt

ENTRYPOINT [ "flask" ]
CMD [ "run", "--host", "0.0.0.0" ]
