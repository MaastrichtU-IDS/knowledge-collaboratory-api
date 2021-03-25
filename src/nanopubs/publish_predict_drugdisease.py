import os
import sys
import subprocess
import ast
import connexion
import flask
import logging
import json
import csv
from datetime import datetime

# from SPARQLWrapper import SPARQLWrapper, TURTLE, XML

import pandas as pd 
from nanopub import Publication, NanopubClient
from rdflib import Graph, Namespace, URIRef, Literal, RDF, FOAF, RDFS

import requests
# import functools
# import shutil

BIOLINK = Namespace("https://w3id.org/biolink/vocab/")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
SCHEMA = Namespace("http://schema.org/")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
PROV = Namespace("http://www.w3.org/ns/prov#")
MLS = Namespace("http://www.w3.org/ns/mls#")


def create_drug_indic_nanopub(np_client, drug_id, disease_id):
    """Create a Nanopublication in RDF for a drug indication using the BioLink model
    """
    # Or: 1. construct a desired assertion (a graph of RDF triples)
    nanopub_rdf = Graph()
    nanopub_rdf.bind("biolink", URIRef('https://w3id.org/biolink/vocab/'))
    nanopub_rdf.bind("drugbank", URIRef('https://identifiers.org/DRUGBANK:'))
    nanopub_rdf.bind("pmid", URIRef('http://www.ncbi.nlm.nih.gov/pubmed/'))
    nanopub_rdf.bind("ro", URIRef('http://purl.obolibrary.org/obo/RO_'))
    nanopub_rdf.bind("omim", URIRef('https://identifiers.org/OMIM:'))
    # nanopub_rdf.bind("omim", URIRef('http://purl.obolibrary.org/obo/OMIM_'))

    ## Use BioLink JSON-LD context: https://github.com/biolink/biolink-model/blob/master/context.jsonld

    drug_uri = URIRef('https://identifiers.org/DRUGBANK:' + drug_id)
    disease_uri = URIRef('https://identifiers.org/OMIM:' + str(disease_id))
    # disease_uri = URIRef('http://purl.obolibrary.org/obo/OMIM_' + str(disease_id))

    # disease_uri = URIRef('https://identifiers.org/mim/' + str(disease_id))
    association_uri = URIRef('https://w3id.org/um/predict/reference/' + drug_id + '_OMIM' + str(disease_id))

    # BioLink do not require to define rdf:type, but come on...
    nanopub_rdf.add( (drug_uri, RDF.type, BIOLINK['Drug'] ) )
    nanopub_rdf.add( (drug_uri, BIOLINK['category'], BIOLINK['Drug'] ) )

    nanopub_rdf.add( (disease_uri, RDF.type, BIOLINK['Disease'] ) )
    nanopub_rdf.add( (disease_uri, BIOLINK['category'], BIOLINK['Disease'] ) )

    # Generate triples for the association
    nanopub_rdf.add( (association_uri, RDF.subject, drug_uri ) )
    nanopub_rdf.add( (association_uri, RDF.object, disease_uri ) )

    nanopub_rdf.add( (association_uri, RDF.predicate, BIOLINK['treats'] ) )
    nanopub_rdf.add( (association_uri, BIOLINK['association_type'], BIOLINK['ChemicalToDiseaseOrPhenotypicFeatureAssociation']) )

    nanopub_rdf.add( (association_uri, BIOLINK['provided_by'], URIRef("http://www.ncbi.nlm.nih.gov/pubmed/PMC3159979") ) )
    nanopub_rdf.add( (association_uri, BIOLINK['relation'], URIRef("http://purl.obolibrary.org/obo/RO_0002606") ) )
    

    # https://identifiers.org/drugbank/DB01148
    # https://identifiers.org/mim/231200

    publication = Publication.from_assertion(assertion_rdf=nanopub_rdf)
    publication_info = np_client.publish(publication)
    # publication_info = publication
    # print(nanopub_rdf.serialize('output/np_assertion.ttl', format='turtle'))
    return publication_info




# Create the client, that allows searching, fetching and publishing nanopubs
np_client = NanopubClient()

# Generate nanopubs from OpenPredict drug-disease gold standard
url = 'https://raw.githubusercontent.com/MaastrichtU-IDS/translator-openpredict/master/openpredict/data/resources/openpredict-omim-drug.csv'

data = pd.read_csv(url)

for index, row in data.iterrows(): 
    nanopub_uri = create_drug_indic_nanopub(np_client, row['drugid'], row['omimid'])
    print(nanopub_uri)



# global DATA_DIR
# DATA_DIR = os.getenv('TRAPI_DATA_DIR')
# if not DATA_DIR:
#     # Output data folder in current dir if not provided via environment variable
#     DATA_DIR = os.getcwd() + '/output/'
# else:
#     if not DATA_DIR.endswith('/'):
#         DATA_DIR += '/'

