# start by pulling the python image
FROM python:3.9.13
WORKDIR /app
COPY . /app

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y python3-pip
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
EXPOSE 5005
EXPOSE 80
EXPOSE 8080

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["app.py" ]
