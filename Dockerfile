FROM python:3.10-alpine

LABEL author="Meysam Azad <meysam@licenseware.io>"

RUN apk add --update curl && \
    curl -Lso dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.5/dumb-init_1.2.5_x86_64 && \
    mv dumb-init /usr/local/bin/ && \
    chmod +x /usr/local/bin/dumb-init && \
    pip install -U pip

WORKDIR /service

COPY . .
RUN pip install .

ENTRYPOINT [ "/usr/local/bin/dumb-init", "--" ]
CMD [ "python", "main.py" ]
