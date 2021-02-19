FROM python:3

COPY . /

RUN pip3 install -r ./requirements.txt

EXPOSE 3000

ENTRYPOINT ["python3"]
CMD ["./app.py"]
