FROM alpine:pandas
ENV ENV=${ENV}

WORKDIR /code

ADD requirements.txt /code 
RUN pip install -r requirements.txt
ADD . /code

EXPOSE 5000
CMD ["python", "app/app_server.py"]


#CMD ['python','bieber_scrapping.py']