import pytest
import json
import requests

PROD_API_URL = 'https://api.collaboratory.semanticscience.org'

def test_post_trapi():
    """Test Translator ReasonerAPI query POST operation to get predictions"""
    trapi_query = {
        "message": {
            "n_results": 42,
            "query_graph": {
            "edges": {
                "e01": {
                    "object": "n1",
                    "predicate": "biolink:treats",
                    "subject": "n0"
                }
            },
            "nodes": {
                "n0": {
                    "category": "biolink:Drug"
                },
                "n1": {
                    "category": "biolink:Disease"
                }
            }
            }
        }
    }
    headers = {'Content-type': 'application/json'}
    trapi_results = requests.post(PROD_API_URL + '/query',
                        data=json.dumps(trapi_query), headers=headers).json()

    edges = trapi_results['knowledge_graph']['edges'].items()
    assert len(edges) == 42
    # assert edges[0]['object'] == 'OMIM:246300'
