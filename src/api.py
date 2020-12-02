import os
import subprocess
import ast
import connexion
import flask
import logging
import json
from datetime import datetime

from SPARQLWrapper import SPARQLWrapper, TURTLE, XML
from rdflib import Graph
from kgx import RdfTransformer, PandasTransformer
import zipfile

def start_api(port=8808, server_url='/', debug=False):
    """Start the Translator OpenPredict API using [zalando/connexion](https://github.com/zalando/connexion) and the `openapi.yml` definition

    :param port: Port of the OpenPredict API, defaults to 8808
    :param debug: Run in debug mode, defaults to False
    :param start_spark: Start a local Spark cluster, default to true
    """
    print("Starting the \033[1mTranslator OpenPredict API\033[0m 🔮🐍")

    if debug:
        # Run in development mode
        deployment_server='flask'
        logging.basicConfig(level=logging.DEBUG)
        print("Development deployment using \033[1mFlask\033[0m 🧪")
        print("Debug enabled 🐞 - The API will reload automatically at each change 🔃")
    else:
        # Run in productiom with tornado (also available: gevent)
        deployment_server='tornado'
        logging.basicConfig(level=logging.INFO)
        print("Production deployment using \033[1mTornado\033[0m 🌪️")
    
    api = connexion.App(__name__, options={"swagger_url": ""})

    api.add_api('openapi.yml', arguments={'server_url': server_url})
    # api.add_api('openapi.yml', arguments={'server_url': server_url}, validate_responses=True)

    print("Access Swagger UI at \033[1mhttp://localhost:" + str(port) + "\033[1m 🔗")
    api.run(port=port, debug=debug, server=deployment_server)


def get_kgx():
    """Query the Nanopubs SPARQL endpoint using CONSTRUCT queries 
    to retrieve BioLink nodes and edges (associations)
    Then convert the RDF to kgx TSV format
    And return the files in a zip file  
    """
    sparql = SPARQLWrapper("http://nanopub-sparql.137.120.31.102.nip.io/sparql")

    print('Read SPARQL query')
    with open('src/construct_pskg_from_nanopubs.rq') as f:
        sparql_query = f.read()

    sparql.setQuery(sparql_query)

    # CONSTRUCT query to Nanopubs SPARQL endpoint
    sparql.setReturnFormat(TURTLE)
    results = sparql.query().convert().decode('utf-8')
    print('Run SPARQL query')

    # Write RDF to file
    with open('output/rdf_for_kgx.ttl', 'w') as f:
        f.write(results)
    # print(results)

    # Initialize turtle transformer
    t = RdfTransformer()
    t.parse('output/rdf_for_kgx.ttl')

    # Transform turtle to KGX TSV
    kgx_dir = 'output/kgx/'
    pt = PandasTransformer(t.graph)
    pt.save(kgx_dir + 'pskg_nanopubs', output_format='tsv')

    # Zip nodes and edges files 
    with zipfile.ZipFile('output/pskg_nanopubs_kgx.zip', 'w') as zip_file:
        for tsv_file in os.listdir(kgx_dir):
            zip_file.write(kgx_dir + tsv_file)
        # zip_file.close()

    # resp = flask.send_file(zip_file,
    resp = flask.send_from_directory(os.getcwd() + '/output', 'pskg_nanopubs_kgx.zip',
        as_attachment=True, 
        mimetype='application/zip',
        attachment_filename='pskg_nanopubs_kgx.zip'
    )
    return resp


# def get_sparql(query, endpoint="http://ldf.nanopubs.lod.labs.vu.nl/np"):
#     """Get associations for a given entity CURIE.
    
#     :param entity: Search for predicted associations for this entity CURIE
#     :return: Prediction results object with score
#     """
#     time_start = datetime.now()

#     # prediction_json = get_predictions(entity, classifier, score, n_results)
    
#     ldf_url = 'http://ldf.nanopubs.lod.labs.vu.nl/np'
#     sparql_query = 'SELECT * WHERE { ?s ?p <https://w3id.org/biolink/vocab/Association> . } LIMIT 10'

#     # Built comunica-sparql command to execute query
#     comunica_cmd = 'comunica-sparql ' + endpoint + ' "' + query + '"'
#     print(comunica_cmd)

#     sparql_results = str(subprocess.check_output(comunica_cmd, shell=True))

#     # print(sparql_results.stdout) 
#     print(sparql_results)
#     # Parse shell output output as dict 
#     results_dict = eval(sparql_results)

#     relation = "biolink:treated_by"
#     logging.info('Runtime: ' + str(datetime.now() - time_start))
#     results_json = json.loads(results_dict)
#     return {'results': results_json, 'relation': relation, 'count': len(results_json)} or ('Not found', 404)

def get_predicates():
    """Get predicates and entities provided by the API
    
    :return: JSON with biolink entities
    """
    openpredict_predicates = {
        "disease": {
            "drug": [
            "treated_by"
            ]
        }
    }
    return openpredict_predicates

def post_reasoner_query(request_body):
    """Get associations for a given ReasonerAPI query.
    
    :param request_body: The ReasonerStdAPI query in JSON
    :return: Results as a ReasonerStdAPI Message
    """
    query_graph = request_body["message"]["query_graph"]
    print(query_graph)
    if len(query_graph["edges"]) == 0:
        return ({"status": 400, "title": "Bad Request", "detail": "No edges", "type": "about:blank" }, 400)
    if len(query_graph["edges"]) > 1:
        return ({"status": 501, "title": "Not Implemented", "detail": "Multi-edges queries not yet implemented", "type": "about:blank" }, 501)

    # reasonerapi_response = typed_results_to_reasonerapi(request_body)
    reasonerapi_response = request_body

    # TODO: populate edges/nodes with association predictions    
    #  Edge: {
    #     "id": "e50",
    #     "source_id": "MONDO:0021668",
    #     "target_id": "ChEMBL:CHEMBL560511",
    #     "type": "treated_by"
    #   }
    # Node: {
    #     "id": "ChEMBL:CHEMBL2106966",
    #     "name": "Piketoprofen",
    #     "type": "chemical_substance"
    #   },

    return reasonerapi_response or ('Not found', 404)

server_url = "/"
debug = True
# Start API in debug mode 
start_api(8808, server_url, debug)
