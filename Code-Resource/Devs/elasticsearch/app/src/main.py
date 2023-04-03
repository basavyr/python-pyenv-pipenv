from elasticsearch import Elasticsearch

from configs import config


es = Elasticsearch(
    hosts=config.ES_HOST,
    api_key=(config.ES_API_KEY['id'], config.ES_API_KEY['key']),
    ca_certs=config.CERT_PATH
)

response = es.info()

print(response)
