from elasticsearch import Elasticsearch
import asyncio

import json
from datetime import datetime

from async_module import async_es
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

    def check_index_exists(self, index_name: str) -> bool:
        """
        - returns True if the index exists on the Elasticsearch cluster
        """
        return self.es_instance.indices.exists(index=index_name)


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


async def main_async():
    # create an async client
    async_es_client = async_es.create_async_es_client()

    # run testing async functions
    await async_es.print_info(async_es_client)
    # await async_es.get_es_indices(async_es_client)
    await async_es.get_fixed_docs(async_es_client, 20)

    # close the async client connection
    await async_es_client.transport.close()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()  # use new keyword to create the event loop
    loop.run_until_complete(main_async())
    loop.close()
