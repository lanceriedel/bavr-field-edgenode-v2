FROM docker.io/library/python:3.9-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install pip wheel --upgrade && \
    python -m pip install -r requirements.txt

RUN apt-get update && apt-get install -y udev
RUN apt-get update && apt-get install -y \
   autoconf \
   autoconf-archive \
   automake \
   build-essential \
   git \
   libtool \
   pkg-config \
   python3 \
   python3-dev \
   python3-setuptools \
   swig3.0 \
   wget \
   python3-libgpiod
RUN python3 -m pip install -U --user pip gpiod

COPY . .
CMD ["python", "edgenode.py"]
