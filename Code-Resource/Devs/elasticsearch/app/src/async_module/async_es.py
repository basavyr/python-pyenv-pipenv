import json
import uuid

import asyncio
from elasticsearch import Elasticsearch, AsyncElasticsearch

from configs import config


def create_async_es_client() -> AsyncElasticsearch:
    """
    - creates an asynchronous Elasticsearch connection to an existing client
    """
    async_es_client = AsyncElasticsearch(
        hosts='https://localhost:9200/', api_key=(config.ES_API_KEY['id'], config.ES_API_KEY['key']),
        ca_certs=config.CERT_PATH)

    return async_es_client


async def get_all_docs(es_client: AsyncElasticsearch, es_index: str) -> dict:
    response = await es_client.async_search(
        index=es_index,
        body={
            'query': {
                'match_all': {}
            }
        }
    )

    # await es_client.close()
    return response


async def get_fixed_docs(es_client, n_docs):
    resp = await es_client.search(
        index="debug_index",
        body={
            "query":
                {"match_all": {}}
        },
        size=n_docs,
    )
    print(resp)


async def index_document(es_client):
    """
    - update or create a document on the Elasticsearch index
    """
    def doc(): return {
        "extra-info": 367218,
        "my-field": 356218,
        'unique-identified': 'yes',
        'unique-hash': str(uuid.uuid4()),
    }
    docs = [doc() for _ in range(20)]
    test_index = "debug_index"
    resp = await es_client.index(index=test_index, body=doc())
    print(resp)


async def get_es_indices(es_client):
    # Get Document API
    # this is a test document, which already exists in the Elasticsearch index
    test_id_debug = 'ax-XaYcB_ivX9fnUxzlV'
    # the id was automatically generated when the POST command was executed from Kibana Dev Tools
    id_1 = await es_client.get(index="debug_index", id=test_id_debug)
    # print(id_1)

    # Get Index API
    test_index = "debug_index"
    indices = await es_client.indices.get(index=test_index)

    for k, v in indices.items():
        if k == test_index:
            print(v['mappings'])


async def print_info(es_client):
    info = await es_client.info()
    print(info)
