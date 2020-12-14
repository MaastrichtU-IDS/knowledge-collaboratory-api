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
    query_plan = {}
    if len(query_graph["edges"]) != 1:
        return {'error': len(query_graph["edges"]) + """ edges have been provided. 
            This API currently only implements 1 hop queries (with 1 edge query_graph). 
            Contact us if you are interested in running multiple hop queries"""}
    # Parse the query_graph to build the query plan
    sparql_query_get_nanopubs = get_nanopubs_select_query
    # query_graph_edge = query_graph['edges']
    # query_graph_edge = query_graph['nodes']

    # query_graph_edge['subject']
    # query_graph_edge['object']
    # query_graph_edge['predicate']

    predicate_category = ''
    subject_category = ''
    object_category = ''
    predicate_edge_id = ''
    subject_node_id = ''
    object_node_id = ''
    for edge_id in query_graph['edges'].keys():
        edge_props = query_graph['edges'][edge_id]
        # Build dict with all infos of associations to predict 
        # query_plan[qg_edge['id']] = {
        #     'association_type': qg_edge['type'],
        #     'qg_source_id': qg_edge['source_id'],
        #     'qg_target_id': qg_edge['target_id']
        # }
        predicate_category = edge_props['predicate']
        subject_category = query_graph['nodes'][edge_props['subject']]['category']
        object_category = query_graph['nodes'][edge_props['object']]['category']
        predicate_edge_id = edge_id
        subject_node_id = edge_props['subject']
        object_node_id = edge_props['object']
        sparql_query_get_nanopubs = sparql_query_get_nanopubs.replace('?_predicate_category', predicate_category)
        sparql_query_get_nanopubs = sparql_query_get_nanopubs.replace('?_subject_category', subject_category)
        sparql_query_get_nanopubs = sparql_query_get_nanopubs.replace('?_object_category', object_category)

        # # Get the nodes infos in the query plan object
        # for node in query_graph['nodes']:
        #     # sparql_query_get_nanopubs = sparql_query_get_nanopubs.replace('?_subject_category', ff)
        #     # sparql_query_get_nanopubs = sparql_query_get_nanopubs.replace('?_object_category', node['type'])

        #     if node['id'] == qg_edge['source_id']:
        #         sparql_query_get_nanopubs = sparql_query_get_nanopubs.replace('?_subject_category', node['type'])
        #         # TODO: check if still useful
        #         if 'curie' in node:
        #             # The node with curie is the association's "from"
        #             query_plan[qg_edge['id']]['from_kg_id'] = node['curie']
        #             query_plan[qg_edge['id']]['from_qg_id'] = node['id']
        #             query_plan[qg_edge['id']]['from_type'] = node['type']
        #         else:
        #             # The node without curie is the association's "to"
        #             query_plan[qg_edge['id']]['to_qg_id'] = node['id']
        #             query_plan[qg_edge['id']]['to_type'] = node['type']

        #     if node['id'] == qg_edge['target_id']:
        #         sparql_query_get_nanopubs = sparql_query_get_nanopubs.replace('?_object_category', node['type'])
        #         # TODO: check if still useful
        #         if 'curie' in node:
        #             # The node with curie is the association's "from"
        #             query_plan[qg_edge['id']]['from_kg_id'] = node['curie']
        #             query_plan[qg_edge['id']]['from_qg_id'] = node['id']
        #             query_plan[qg_edge['id']]['from_type'] = node['type']
        #         else:
        #             # The node without curie is the association's "to"
        #             query_plan[qg_edge['id']]['to_qg_id'] = node['id']
        #             query_plan[qg_edge['id']]['to_type'] = node['type']

        # TODO: edge type should be required??

    knowledge_graph = {'nodes': {}, 'edges': {}}
    node_dict = {}
    query_results = []
    kg_edge_count = 0

    # TODO: SPARQLWrapper query to the nanopub Virtuoso
    # 1. SPARQL builder to build the SPARQL SELECT query from TRAPI query (cf. above)
    # 2. Run SELECT query here
    # 3. Build the TRAPI response by iterating the results of the SELECT query below

    print('RUNNING sparql_query_get_nanopubs')
    print(sparql_query_get_nanopubs)
    sparql = SPARQLWrapper(SPARQL_ENDPOINT_URL)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(sparql_query_get_nanopubs)
    sparqlwrapper_results = sparql.query().convert()
    print('SPARQLWrapper Results:')
    print(sparqlwrapper_results["results"]["bindings"])
    sparql_results = sparqlwrapper_results["results"]["bindings"]
    # sparql_query_get_nanopubs

    # Now iterates the Nanopubs SPARQL query results
    # for edge_qg_id in query_plan.keys():
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

        # Check current official example: https://github.com/NCATSTranslator/ReasonerAPI/blob/master/examples/Message/simple.json
    


        # TODO: pass score and limit from Reasoner query
        # prediction_json = get_predictions(query_plan[edge_qg_id]['from_kg_id'])
        # np_results_json = {}
        # for association in np_results_json:
        #     edge_kg_id = 'e' + str(kg_edge_count)
        #     # Get the ID of the predicted entity in result association
        #     # based on the type expected for the association "to" node
        #     # node_dict[query_plan[edge_qg_id]['from_kg_id']] = query_plan[edge_qg_id]['from_type']
        #     # node_dict[association[query_plan[edge_qg_id]['to_type']]] = query_plan[edge_qg_id]['to_type']
            
        #     # id/type of nodes are registered in a dict to avoid duplicate in knowledge_graph.nodes
        #     # Build dict of node ID : label
        #     node_dict[association['source']['id']] = {
        #         'type': association['source']['type']
        #     }
        #     if 'label' in association['source'] and association['source']['label']:
        #         node_dict[association['source']['id']]['label'] = association['source']['label']

        #     node_dict[association['target']['id']] = {
        #         'type': association['target']['type']
        #     }
        #     if 'label' in association['target'] and association['target']['label']:
        #         node_dict[association['target']['id']]['label'] = association['target']['label']

        #     edge_dict = {
        #         'id': edge_kg_id,
        #         'type': query_plan[edge_qg_id]['association_type'] }

        #     # Map the source/target of query_graph to source/target of association
        #     if association['source']['type'] == query_plan[edge_qg_id]['from_type']:
        #         edge_dict['source_id'] = association['source']['id']
        #         edge_dict['target_id'] = association['target']['id']    
        #     else: 
        #         edge_dict['source_id'] = association['target']['id']
        #         edge_dict['target_id'] = association['source']['id']    

        #     # Add the association in the knowledge_graph as edge
        #     # Use the type as key in the result association dict (for IDs)
        #     knowledge_graph['edges'].append(edge_dict)

        #     # Add the bindings to the results object
        #     result = {'edge_bindings': [], 'node_bindings': []}
        #     result['edge_bindings'].append(
        #         {
        #             "kg_id": edge_kg_id,
        #             'qg_id': edge_qg_id
        #         }
        #     )
        #     result['node_bindings'].append(
        #         {
        #             "kg_id": association['source']['id'],
        #             'qg_id': query_plan[edge_qg_id]['from_qg_id']
        #         })
        #     result['node_bindings'].append(
        #         {
        #             "kg_id": association['target']['id'],
        #             'qg_id': query_plan[edge_qg_id]['to_qg_id']
        #         })
        #     query_results.append(result)
        #     kg_edge_count += 1

    # Generate kg nodes from the dict of nodes + result from query to resolve labels
    # for node_id, properties in node_dict.items():
    #     node_to_add = {
    #         'id': node_id,
    #         'type': properties['type'],
    #         }
    #     if 'label' in properties and properties['label']:
    #         node_to_add['name'] = properties['label']

    #     knowledge_graph['nodes'].append(node_to_add)
    return {'knowledge_graph': knowledge_graph, 'query_graph': query_graph, 'results': query_results}

## Sample Reasoner query
# https://github.com/broadinstitute/molecular-data-provider/blob/master/reasonerAPI/python-flask-server/openapi_server/controllers/molepro.py#L30
# https://smart-api.info/ui/912372f46127b79fb387cd2397203709#/0.9.2/post_query
# "query_graph": {
#   "edges": [
#     {
#       "id": "e00",
#       "source_id": "n00",
#       "target_id": "n01",
#       "type": "treated_by"
#     }
#   ],
#   "nodes": [
#     {
#       "curie": "MONDO:0021668",
#       "id": "n00",
#       "type": "disease"
#     },
#     {
#       "id": "n01",
#       "type": "drug"
#     }
#   ]
# }

#   "results": [
#     {
#     "edge_bindings": [
#         {
#         "kg_id": "e0",
#         "qg_id": "e00"
#         }
#     ],
#     "node_bindings": [
#         {
#         "kg_id": "MONDO:0021668",
#         "qg_id": "n00"
#         },
#         {
#         "kg_id": "ChEMBL:CHEMBL2106966",
#         "qg_id": "n01"
#         }
#     ]
#     }
#   ]