import os

import requests
import flask
import logging
# import json
from datetime import datetime

from SPARQLWrapper import SPARQLWrapper, TURTLE, XML
from rdflib import Graph
from kgx import RdfTransformer, PandasTransformer
import zipfile


class KgxTransformer:
  
  def __init__(self, data_dir):
    self.data_dir = data_dir

  def get_dir(self, file=''):
    """Return the full path to the directory used to store the API data 
    concatenated with the provided file path
    """
    return self.data_dir + file

  def run_sparql_query(self, sparql_endpoint, sparql_query, output_file):
    sparql = SPARQLWrapper(sparql_endpoint)
    sparql.setQuery(sparql_query)

    # CONSTRUCT query to Nanopubs SPARQL endpoint
    sparql.setReturnFormat(TURTLE)
    results = sparql.query().convert().decode('utf-8')
    print('Run SPARQL query')

    # Write RDF to file
    with open(self.get_dir(output_file), 'w') as f:
        f.write(results)

    return results


  def transform_rdf_to_kgx(self, from_kg):
      """Query the Nanopubs SPARQL endpoint using CONSTRUCT queries 
      to retrieve BioLink nodes and edges (associations)
      Then convert the RDF to kgx TSV format
      And return the files in a zip file  
      """
      # Initialize kgx turtle transformer
      rdf_transformer = RdfTransformer()

      if from_kg == 'NeuroDKG':
        ## Get NeuroDKG drug indications
        r = requests.get('https://raw.githubusercontent.com/MaastrichtU-IDS/neuro_dkg/master/convert2biolink.rq')
        neurodkg_sparql_query = r.content
        self.run_sparql_query('https://graphdb.dumontierlab.com/repositories/NeuroDKG', 
                          neurodkg_sparql_query, 'neurodkg_rdf.ttl')
        rdf_transformer.parse(self.get_dir('neurodkg_rdf.ttl'))
      else:
        ## Get drug indications from Nanopublications
        with open('src/construct_pskg_from_nanopubs.rq') as f:
            nanopubs_sparql_query = f.read()

        self.run_sparql_query('http://virtuoso.np.dumontierlab.137.120.31.101.nip.io/sparql', 
                              nanopubs_sparql_query, 'nanopubs_rdf.ttl')
        rdf_transformer.parse(self.get_dir('nanopubs_rdf.ttl'))


      # self.run_sparql_query('http://nanopub-sparql.137.120.31.102.nip.io/sparql',
      #                       nanopubs_sparql_query, 'nanopubs_rdf.ttl')

      # Transform turtle to KGX TSV
      kgx_dir = self.get_dir('kgx/')
      tsv_transformer = PandasTransformer(rdf_transformer.graph)
      tsv_transformer.save(kgx_dir + 'pskg_nanopubs', output_format='tsv')

      # Zip nodes and edges files 
      with zipfile.ZipFile(self.get_dir('knowledge_collaboratory_kgx.zip'), 'w') as zip_file:
          for tsv_file in os.listdir(kgx_dir):
              zip_file.write(kgx_dir + tsv_file, tsv_file)

      resp = flask.send_from_directory(self.get_dir(), 'knowledge_collaboratory_kgx.zip',
          as_attachment=True, 
          mimetype='application/zip',
          attachment_filename='knowledge_collaboratory_kgx.zip'
      )
      return resp

