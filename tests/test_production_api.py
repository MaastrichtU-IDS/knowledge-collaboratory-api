import pytest
import json
import requests

PROD_API_URL = 'https://api.collaboratory.semanticscience.org'

def test_post_trapi():
    """Test Translator ReasonerAPI query POST operation to get predictions"""
    headers = {'Content-type': 'application/json'}
    tests_list = [
        {'limit': 1, 'class': 'drug'},
        {'limit': 'no', 'class': 'drug'},
        {'limit': 1, 'class': 'anydrugdisease'},
        {'limit': 'no', 'class': 'anydrugdisease'},
    ]

    for trapi_test in tests_list:
        trapi_filename = 'tests/queries/trapi_' + trapi_test['class'] + '_limit' + str(trapi_test['limit']) + '.json'
        with open(trapi_filename,'r') as f:
            trapi_query = f.read()
        trapi_results = requests.post(PROD_API_URL + '/query',
                            data=trapi_query, headers=headers).json()

        edges = trapi_results['message']['knowledge_graph']['edges'].items()

        if trapi_test['limit'] == 'no':
            assert len(edges) >= 2
        else:
            assert len(edges) == trapi_test['limit']

        # assert edges[0]['object'] == 'https://identifiers.org/MONDO:0001158'
