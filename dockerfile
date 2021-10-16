FROM python:3.9.7-buster
ADD . ./flask
WORKDIR flask
RUN pip install -r req.txt
EXPOSE 3333

CMD python app.py