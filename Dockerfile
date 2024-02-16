# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9.13

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD apt-get update && apt-get install -y --no-install-recommends git mercurial openssh-client subversion procps && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --upgrade pip


RUN mkdir /travels
WORKDIR /travels
COPY . /travels/

RUN python -m pip install -r requirements.txt
#COPY ./entrypoint.sh .
#ENTRYPOINT ["sh", "/app/entrypoint.sh"]



