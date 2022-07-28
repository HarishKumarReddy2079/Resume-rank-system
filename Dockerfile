FROM python:3.9.11
ADD . /pythonflask
WORKDIR /pythonflask
EXPOSE 5005
RUN pip3 install --upgrade pip
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]


