FROM python:3.9.7-buster
ADD . ./flask
WORKDIR flask
RUN pip install flask
EXPOSE 3030

CMD python app.py