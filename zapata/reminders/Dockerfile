FROM python:3

COPY . /reminders
WORKDIR /reminders

RUN pip3 install -r ./requirements.txt

ENTRYPOINT ["python3"]
CMD ["./reminders.py"]
