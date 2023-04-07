from elasticsearch import Elasticsearch, AsyncElasticsearch
import asyncio

from configs import config


async def get_all_docs():
    async_es = AsyncElasticsearch(
        ['https://localhost:9200/'], verify_certs=True, ca_certs=config.CERT_PATH)

    response = await async_es.async_search(
        index='gicu-test',
        body={
            'query': {
                'match_all': {}
            }
        }
    )

    await async_es.close()

    return response['hits']['hits']

es = Elasticsearch(
    ['https://localhost:9200/'],
    verify_certs=True, ca_certs=config.CERT_PATH)

if es.indices.exists(index='gicu-test'):
    docs = asyncio.run(get_all_docs())
    print(docs)
else:
    print("Index 'gicu-test' does not exist")
