from elasticsearch import Elasticsearch
import json
from datetime import datetime

from configs import config


class MyElasticsearch:
    """
    - class that handles any connection to the local instance of Elasticsearch
    """

    def __init__(self) -> None:
        es = Elasticsearch(
            hosts=config.ES_HOST,
            api_key=(config.ES_API_KEY['id'], config.ES_API_KEY['key']),
            ca_certs=config.CERT_PATH
        )
        self.es_instance = es


def index_test(es: Elasticsearch):
    """
    - function that adds a document to an index
    - [debug] just for testing purposes
    """
    doc = {
        'author': 'Elastic',
        'text': 'Elasticsearch',
        'timestamp': datetime.now(),
    }
    resp = es.index(index="test-index", id=1, document=doc)
    print(resp['result'])


def import_test_mr():
    with open('../data/local-conmod-ppe.json') as reader:
        raw_data = reader.readlines()
    mr_data = []
    for raw_mr in raw_data:
        mr_data.append(json.loads(raw_mr))
    return mr_data


def main():
    es_instance = MyElasticsearch()
    es = es_instance.es_instance

    data = import_test_mr()
    index_name = 'test-conmod'

    for idx in range(len(data)):
        mr = data[idx]
        try:
            mr['timestamp'] = datetime.now()
            resp = es.index(index=index_name, id=idx+1, document=mr)
            print(resp['result'])
        except Exception:
            print('Cannot send the MR to Elasticsearch')
            print('Check logs at')
        idx = idx+1


if __name__ == '__main__':
    main()
