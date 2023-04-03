import os

ES_HOME = ''
if (os.environ['ES_HOME'] != ""):
    ES_HOME = os.environ['ES_HOME']

ES_CERT = "http_ca.crt"
ES_HOST = "https://localhost:9200"
ES_API_KEY = {
    "id": "",
    "key": ""}

CERT_PATH = os.path.join(ES_HOME, 'config/certs', ES_CERT)
