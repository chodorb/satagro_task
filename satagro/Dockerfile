FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install GDAL dependencies
RUN apt-get update -y && apt-get install -y binutils libproj-dev gdal-bin

# Set GDAL_LIBRARY_PATH environment variable
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so

RUN apt-get install netcat -y
WORKDIR /satagro

COPY requirements.txt /satagro/
RUN pip install -r requirements.txt
COPY . /satagro
