FROM python:3.9.11
WORKDIR /pythonflask
ADD . /pythonflask/
EXPOSE 5005
RUN pip install --upgrade pip
RUN pip install PyMuPDF
RUN pip install -r requirements.txt
RUN pip  install Flask gunicorn
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]


