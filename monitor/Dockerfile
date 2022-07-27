FROM python:3.8

RUN apt-get install libc-dev

RUN apt-get install g++ 
RUN pip install -U pip

COPY ./requirements.txt ./requirements.txt
COPY ./monitor /app/monitor

RUN pip3 install -r requirements.txt

WORKDIR app
ENTRYPOINT ["streamlit", "run"]