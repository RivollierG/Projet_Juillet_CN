FROM alpine


RUN apk add py3-pip python3
    
COPY ./dist/app-1.0-py3-none-any.whl /

WORKDIR /

RUN pip install app-1.0-py3-none-any.whl --force-reinstall --no-cache


