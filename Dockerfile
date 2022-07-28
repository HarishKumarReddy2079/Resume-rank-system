FROM python:3.9.11
ADD . /pythonflask
WORKDIR /pythonflask
EXPOSE 5005
RUN pip3 install --upgrade pip
RUN pip3 install PyMuPDF
RUN pip3 install -r requirements.txt
RUN pip3 install Flask gunicorn
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]


