FROM python:3.8-alpine
RUN mkdir /apps
ADD index.html /apps
RUN rm -rf /tmp/* /var/cache/apk/*
WORKDIR /apps
EXPOSE 9999
ENTRYPOINT ["python3","-m","http.server","9999"]