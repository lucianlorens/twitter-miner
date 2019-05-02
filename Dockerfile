FROM nickgryg/alpine-pandas:3.6.6

RUN apk add gcc libev-dev musl-dev

ENV ENV=${ENV}
ENV PORT=${PORT}
ENV HOST=${HOST}

WORKDIR /code

ADD requirements.txt /code 
RUN pip install -r requirements.txt
ADD . /code

EXPOSE 5000
CMD ["python", "app/app_server.py"]

#CMD ['python','twitter_mining.py']