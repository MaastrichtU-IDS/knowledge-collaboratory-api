from nanopub import Publication, NanopubClient
from rdflib import Graph, Namespace, URIRef, Literal, RDF, FOAF, RDFS, XSD

# Create the client, that allows publishing nanopubs
def publish_edge_comment(edge_to_comment, comment, negated, evidence, dryrun=True):
  np_client = NanopubClient()
  BIOLINK = Namespace("https://w3id.org/biolink/vocab/")
  NP = Namespace("http://purl.org/nanopub/temp/mynanopub#")
  nanopub_rdf = Graph()
  nanopub_rdf.bind("biolink", URIRef('https://w3id.org/biolink/vocab/'))

  # Add edge data
  edge_uri = NP['edge']
  # nanopub_rdf.add( (edge_uri, RDF.type, RDF.Statement ) )
  for prop, value in edge_to_comment.items():
      nanopub_rdf.add( (edge_uri, BIOLINK[prop], Literal(value) ) )

  # Add user comment
  comment_uri = NP['comment']
  nanopub_rdf.add( (comment_uri, RDF.type, RDF.Statement ) )
  nanopub_rdf.add( (comment_uri, RDFS.comment, Literal(comment) ) )
  nanopub_rdf.add( (comment_uri, BIOLINK['source'], edge_uri ) )
  nanopub_rdf.add( (comment_uri, BIOLINK['negated'], Literal(negated,datatype=XSD.boolean) ) )
  nanopub_rdf.add( (comment_uri, BIOLINK['has_evidence'], URIRef(evidence) ) )

  # print(nanopub_rdf.serialize(format='turtle'))
  publication = Publication.from_assertion(assertion_rdf=nanopub_rdf)
  if dryrun == False:
    publication_info = np_client.publish(publication)
  else:
    print("Dry run, not publishing the Nanopub. Add dryrun=False to the function args to publish")
  return publication