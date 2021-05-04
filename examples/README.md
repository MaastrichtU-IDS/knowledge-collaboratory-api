Query the Nanopublication network:

## SPARQL example ✨️

You can also query the nanopublication network with a SPARQL query on the endpoint http://virtuoso.np.dumontierlab.137.120.31.101.nip.io/sparql:

**<a href="https://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20biolink%3A%20%3Chttps%3A%2F%2Fw3id.org%2Fbiolink%2Fvocab%2F%3E%0APREFIX%20np%3A%20%3Chttp%3A%2F%2Fwww.nanopub.org%2Fnschema%23%3E%0APREFIX%20npx%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fnanopub%2Fx%2F%3E%0Aprefix%20npa%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fnanopub%2Fadmin%2F%3E%0APREFIX%20dct%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX%20orcid%3A%20%3Chttps%3A%2F%2Forcid.org%2F%3E%20%0A%23SELECT%20DISTINCT%20%3Fnp_uri%20%3Flabel%20%3Frelation%20%3Fsubject%20%3Fpredicate%20%3Fobject%20%3Fpubkey%0ASELECT%20DISTINCT%20*%0AWHERE%20%7B%0A%20%20graph%20%3Fnp_assertion%20%7B%0A%20%20%20%20%3Fassociation%0A%20%20%20%20%20%20rdfs%3Alabel%20%3Flabel%20%3B%0A%20%20%20%20%20%20rdf%3Asubject%20%3Fsubject%20%3B%0A%20%20%20%20%20%20rdf%3Apredicate%20%3Fpredicate%20%3B%0A%20%20%20%20%20%20rdf%3Aobject%20%3Fobject%20%3B%0A%20%20%20%20%20%20biolink%3Arelation%20%3Frelation%20%3B%0A%20%20%20%20%20%20biolink%3Aprovided_by%20%3Fprovided_by%20%3B%0A%20%20%20%20%20%20biolink%3Aassociation_type%20%3Fassociation_type%20.%0A%20%20%20%20%3Fsubject%20biolink%3Acategory%20%3Fsubject_category%20.%0A%20%20%20%20%3Fobject%20biolink%3Acategory%20%3Fobject_category%20.%0A%20%20%7D%0A%20%20FILTER%20(%20%3Fsubject_category%20%3D%20biolink%3ADrug%20%7C%7C%20%3Fsubject_category%20%3D%20biolink%3AChemicalSubstance%20)%0A%20%20FILTER%20(%20%3Fobject_category%20%3D%20biolink%3ADisease%20)%0A%20%20%23FILTER%20(%20%3Fsubject%20%3D%20%3Chttps%3A%2F%2Fidentifiers.org%2FDRUGBANK%3ADB00394%3E%20%7C%7C%20%3Fsubject%20%3D%20%3Chttps%3A%2F%2Fidentifiers.org%2FCHEBI%3A75725%3E%20)%0A%0A%20%20graph%20%3Fnp_head%20%7B%0A%20%20%20%20%3Fnp_uri%20np%3AhasAssertion%20%3Fnp_assertion%20.%0A%20%20%7D%0A%20%20graph%20npa%3Agraph%20%7B%0A%20%20%20%20%3Fnp_uri%20npa%3AhasValidSignatureForPublicKey%20%3Fpubkey%20.%0A%20%20%7D%0A%20%20%7B%0A%20%20%20%20%3Fnp_uri%20dct%3Acreator%20orcid%3A0000-0002-7641-6446%20.%0A%20%20%7D%0A%20%20%0A%20%20FILTER%20(%20str(%3Fpubkey)%20%3D%20%22MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCamPJb4SzqpLXn%2F%2FXJ5dlVfzz6QI%2BRPmiJTLXF%2Fby2JR7sHMKRsCQDFsYMlq8zGHghOIkjRP9dpLZUtZzUcHt3MXiFKEPo8eGzUe9p%2BJXKFC8xxkJr94z2vq6IdMf71Iu1GH8SeDAKt%2FDgYO4zNaw8VuXvxnZRewKZSA%2Bu8zWPVwIDAQAB%22)%0A%20%20FILTER%20NOT%20EXISTS%20%7B%20%3Fcreator%20npx%3Aretracts%20%3Fnp_uri%20%7D%0A%7D%20&endpoint=http%3A%2F%2Fvirtuoso.np.dumontierlab.137.120.31.101.nip.io%2Fsparql&requestMethod=POST&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=application%2Fn-triples%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table">Try the query here</a>**

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX biolink: <https://w3id.org/biolink/vocab/>
PREFIX np: <http://www.nanopub.org/nschema#>
PREFIX npx: <http://purl.org/nanopub/x/>
prefix npa: <http://purl.org/nanopub/admin/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX orcid: <https://orcid.org/> 
#SELECT DISTINCT ?np_uri ?label ?relation ?subject ?predicate ?object ?pubkey
SELECT DISTINCT *
WHERE {
  graph ?np_assertion {
    ?association
      rdfs:label ?label ;
      rdf:subject ?subject ;
      rdf:predicate ?predicate ;
      rdf:object ?object ;
      biolink:relation ?relation ;
      biolink:provided_by ?provided_by ;
      biolink:association_type ?association_type .
    ?subject biolink:category ?subject_category .
    ?object biolink:category ?object_category .
  }
  FILTER ( ?subject_category = biolink:Drug || ?subject_category = biolink:ChemicalSubstance )
  FILTER ( ?object_category = biolink:Disease )
  #FILTER ( ?subject = <https://identifiers.org/DRUGBANK:DB00394> || ?subject = <https://identifiers.org/CHEBI:75725> )

  graph ?np_head {
    ?np_uri np:hasAssertion ?np_assertion .
  }
  graph npa:graph {
    ?np_uri npa:hasValidSignatureForPublicKey ?pubkey .
  }
  {
    ?np_uri dct:creator orcid:0000-0002-7641-6446 .
  }
  
  FILTER ( str(?pubkey) = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCamPJb4SzqpLXn//XJ5dlVfzz6QI+RPmiJTLXF/by2JR7sHMKRsCQDFsYMlq8zGHghOIkjRP9dpLZUtZzUcHt3MXiFKEPo8eGzUe9p+JXKFC8xxkJr94z2vq6IdMf71Iu1GH8SeDAKt/DgYO4zNaw8VuXvxnZRewKZSA+u8zWPVwIDAQAB")
  FILTER NOT EXISTS { ?creator npx:retracts ?np_uri }
} 
```

We can use those 2 options to filter by creator:

* ORCID:

  ```SPARQL
  ?np_uri dct:creator orcid:0000-0002-7641-6446 .
  ```

* Pubkey:

  ```SPARQL
  FILTER ( str(?pubkey) = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCamPJb4SzqpLXn//XJ5dlVfzz6QI+RPmiJTLXF/by2JR7sHMKRsCQDFsYMlq8zGHghOIkjRP9dpLZUtZzUcHt3MXiFKEPo8eGzUe9p+JXKFC8xxkJr94z2vq6IdMf71Iu1GH8SeDAKt/DgYO4zNaw8VuXvxnZRewKZSA+u8zWPVwIDAQAB")
  ```

# Example notebooks 📔

We provide [Jupyter Notebooks](https://jupyter.org/) with examples to use the OpenPredict API in this folder.

To try the examples clone the repository:

```bash
git clone https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api.git
```

Then go to the `examples` folder and open the notebooks with your favorite viewer (Jupyter or VisualStudio Code)

To install the dependencies:

```bash
/path/to/vscode/interpreter/python -m pip install -r requirements.txt
```

You can also start the notebook with docker (requires docker to be installed):

```bash
docker-compose up
```

> The default password of the notebook started with docker is `password`

Contributions, [feedbacks](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/issues) and pull requests are welcomed!
