# from openpredict.predict_utils import get_predictions

# import nanopub
from SPARQLWrapper import SPARQLWrapper, POST, JSON

get_nanopubs_select_query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX biolink: <https://w3id.org/biolink/vocab/>
PREFIX np: <http://www.nanopub.org/nschema#>
PREFIX npx: <http://purl.org/nanopub/x/>
SELECT *
WHERE {
  graph ?np_assertion {
    ?association
      biolink:association_type ?association_type ;
      rdf:subject ?subject ;
      rdf:predicate ?_predicate_category ;
      rdf:object ?object ;
      biolink:relation ?relation ;
      biolink:provided_by ?provided_by .
  }
  ?subject biolink:category ?_subject_category .
  ?object biolink:category ?_object_category .
  graph ?np_head {
    ?np_uri np:hasAssertion ?np_assertion .
  }
  FILTER NOT EXISTS { ?creator npx:retracts ?np_uri }
}"""

SPARQL_ENDPOINT_URL = 'http://virtuoso.np.dumontierlab.137.120.31.101.nip.io/sparql'

def reasonerapi_to_sparql(reasoner_query):
    """Convert an array of predictions objects to ReasonerAPI format
    Run the get_predict to get the QueryGraph edges and nodes
    {disease: OMIM:1567, drug: DRUGBANK:DB0001, score: 0.9}

    :param: reasoner_query Query from Reasoner API
    :return: Results as ReasonerAPI object
    """
    query_graph = reasoner_query["message"]["query_graph"]
    if len(query_graph["edges"]) != 1:
        return {'error': len(query_graph["edges"]) + """ edges have been provided. 
            This API currently only implements 1 hop queries (with 1 edge query_graph). 
            Contact us if you are interested in running multiple hop queries"""}
    
    sparql_query_get_nanopubs = get_nanopubs_select_query
    predicate_category = ''
    subject_category = ''
    object_category = ''
    predicate_edge_id = ''
    subject_node_id = ''
    object_node_id = ''
    # TODO: improve to support multiple edges query (aka. hops)
    for edge_id in query_graph['edges'].keys():
        edge_props = query_graph['edges'][edge_id]
        predicate_category = edge_props['predicate']
        subject_category = query_graph['nodes'][edge_props['subject']]['category']
        object_category = query_graph['nodes'][edge_props['object']]['category']
        predicate_edge_id = edge_id
        subject_node_id = edge_props['subject']
        object_node_id = edge_props['object']
        sparql_query_get_nanopubs = sparql_query_get_nanopubs.replace('?_predicate_category', predicate_category)
        sparql_query_get_nanopubs = sparql_query_get_nanopubs.replace('?_subject_category', subject_category)
        sparql_query_get_nanopubs = sparql_query_get_nanopubs.replace('?_object_category', object_category)


    knowledge_graph = {'nodes': {}, 'edges': {}}
    query_results = []
    kg_edge_count = 0

    print('Running the following SPARQL query to retrieve nanopublications from ' + SPARQL_ENDPOINT_URL)
    print(sparql_query_get_nanopubs)
    sparql = SPARQLWrapper(SPARQL_ENDPOINT_URL)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(sparql_query_get_nanopubs)
    sparqlwrapper_results = sparql.query().convert()
    sparql_results = sparqlwrapper_results["results"]["bindings"]

    # Check current official example of Reasoner query results: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/examples/Message/simple.json
    # Now iterates the Nanopubs SPARQL query results
    for edge_result in sparql_results:
        edge_uri = edge_result['association']['value']
        # Create edge object in knowledge_graph
        knowledge_graph['edges'][edge_uri] = {
            'predicate': predicate_category,
            'subject': edge_result['subject']['value'],
            'object': edge_result['object']['value'],
            'provided_by': edge_result['provided_by']['value'],
            'association_type': edge_result['association_type']['value'],
            'relation': edge_result['relation']['value']
        }
        knowledge_graph['nodes'][edge_result['subject']['value']] = {
            'category': subject_category
        }
        knowledge_graph['nodes'][edge_result['object']['value']] = {
            'category': object_category
        }

         # Add the bindings to the results object
        result = {'edge_bindings': {}, 'node_bindings': {}}
        result['edge_bindings'][predicate_edge_id] = [
            {
                "id": edge_uri
            }
        ]
        result['node_bindings'][subject_node_id] = [
            {
                "id": edge_result['subject']['value']
            }
        ]
        result['node_bindings'][object_node_id] = [
            {
                "id": edge_result['object']['value']
            }
        ]
        query_results.append(result)

        kg_edge_count += 1
    
    return {'knowledge_graph': knowledge_graph, 'query_graph': query_graph, 'results': query_results}