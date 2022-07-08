FROM alpine


RUN apk add py3-pip python3
    
COPY ./dist/monitor-0.1.0-py3-none-any.whl /

WORKDIR /

RUN pip install numpy==1.19.3
RUN pip install monitor-0.1.0-py3-none-any.whl

