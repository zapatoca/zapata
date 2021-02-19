FROM certbot/certbot

COPY . /

RUN pip3 install --upgrade pip && \
    pip3 install -r /requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "/generateCerts.py"]
