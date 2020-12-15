[![Generate KGX from Knowledge Collaboratory](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/workflows/Generate%20KGX%20from%20Knowledge%20Collaboratory/badge.svg)](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions?query=workflow%3A%22Generate+KGX+from+Knowledge+Collaboratory%22) [![Validate RDF graphs](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/workflows/Validate%20Knowledge%20Collaboratory%20RDF/badge.svg)](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions?query=workflow%3A%22Validate+Knowledge+Collaboratory+RDF%22)

# Contributing

When contributing to this repository, please first discuss the change you wish to make via an [issue](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/issues) if applicable.

If you are part of the [MaastrichtU-IDS organization on GitHub](https://github.com/MaastrichtU-IDS) you can directly create a branch in this repository. Otherwise you will need to first [fork this repository](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/fork).

To contribute:

1. Clone the repository 📥

```bash
git clone https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api.git
cd knowledge-collaboratory-api
```

2. Create a new branch from the `master` branch and add your changes to this branch 🕊️

```bash
git checkout -b my-branch
```

## Development process

Install from the source code, and update the package automatically when the files changes locally :arrows_counterclockwise:

```bash
pip3 install -r requirements.txt
```

> See the [main README](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api) for more details on the package installation.

### Start the Knowledge Collaboratory API :rocket:

Start the **API in debug mode** on http://localhost:8808 with Flask (the API will be reloaded automatically at each change to the code)

```bash
python3 src/api.py debug
```

Or in **production** mode with Tornado:

```bash
python3 src/api.py
```

> By default the API will use the SPARQL endpoint of IDS Nanopublications server Virtuoso.

## Pull Request process

1. Ensure the API works before sending a pull request 🧪
2. Update the `README.md` with details of changes, this includes new environment variables, exposed ports, useful file locations and container parameters 📝
3. [Send a pull request](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/compare) to the `master` branch, answer the questions in the pull request message 📤
4. Project contributors will review your change as soon as they can ✔️

## Versioning process

The versioning scheme for new releases on GitHub used is [SemVer](http://semver.org/) (Semantic Versioning).

Change version in `setup.py` before new release.

---

## Workflows to generate KGX files from RDF graphs

[![Generate KGX from Knowledge Collaboratory](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/workflows/Generate%20KGX%20from%20Knowledge%20Collaboratory/badge.svg)](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions?query=workflow%3A%22Generate+KGX+from+Knowledge+Collaboratory%22) [![Validate RDF graphs](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/workflows/Validate%20Knowledge%20Collaboratory%20RDF/badge.svg)](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions?query=workflow%3A%22Validate+Knowledge+Collaboratory+RDF%22)

We use [GitHub Actions workflows](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/tree/master/.github/workflows) to validate, and transform to KGX TSV files, RDF graphs:

* [`.github/workflows/generate-kgx.yml`](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/blob/master/.github/workflows/generate-kgx.yml)
* [`.github/workflows/validate-rdf.yml`](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/blob/master/.github/workflows/validate-rdf.yml)

The RDF graphs are accessible through public SPARQL endpoints:

* [NeuroDKG](https://graphdb.dumontierlab.com/repositories/NeuroDKG)
* [Nanopublications Personal Scientific Knowledge Graph](http://nanopub-sparql.137.120.31.102.nip.io/sparql)

Attempt to ShEx validation with SHACLEX:

1. Clone and compile shaclex with `sbt`

```bash
git clone https://github.com/weso/shaclex.git
cd shaclex
sbt test
```

2. Run with `sbt`:

```bash
sbt "run --engine=ShEx 
         --schemaUrl https://raw.githubusercontent.com/biolink/biolink-model/master/biolink-model.shex
         --schemaFormat ShExC 
         --data ../knowledge-collaboratory-api/output/neurodkg.ttl"
```

Convert ShEx to SHACL:

```bash
sbt "run --schemaUrl https://raw.githubusercontent.com/biolink/biolink-model/master/biolink-model.shex
           --schemaFormat ShExC 
           --outSchemaFormat Turtle
           --engine SHEX 
           --outEngine SHACLEX
           --showSchema 
           --no-validate"
```

> `--outEngine`: SHACLEX, SHEX, JENASHACL,SHACL_TQ

Results in:

```
[info] Error: es.weso.schema.ShExSchema$ShExSchemaError: Not implemented conversion of non-normalized shapes yet.
[info] Shape: Shape(Some(IRILabel(<https://w3id.org/biolink/vocab/ActivityAndBehavior>)),None,None,None,Some(EachOf(None,List(EachOf(Some(IRILabel(<https://w3id.org/biolink/vocab/ActivityAndBehavior_tes>)),List(Inclusion(IRILabel(<https://w3id.org/biolink/vocab/Occurrent_tes>)), TripleConstraint(None,None,None,<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>,Some(NodeConstraint(None,None,None,List(),Some(List(IRIValue(<https://w3id.org/biolink/vocab/Occurrent>))),None,None)),Some(0),Some(IntMax(1)),None,None,None)),None,None,None,None), TripleConstraint(None,None,None,<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>,Some(NodeConstraint(None,None,None,List(),Some(List(IRIValue(<https://w3id.org/biolink/vocab/ActivityAndBehavior>))),None,None)),Some(0),Some(IntMax(1)),None,None,None)),None,None,None,None)),None,None,None)
[info] Error: Contains an inclusion
```

---

## Query the Nanopublications network with SPARQL

Query 1, filter out retracted nanopubs:

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bl: <https://w3id.org/biolink/vocab/>
PREFIX np: <http://www.nanopub.org/nschema#>
PREFIX npx: <http://purl.org/nanopub/x/>
CONSTRUCT {
  ?association
    bl:association_type ?association_type ;
    rdf:subject ?subject ;
    rdf:predicate ?predicate ;
    rdf:object ?object ;
    bl:relation ?relation ;
  	bl:provided_by ?provided_by .
  ?subject bl:category ?subjectCategory .
  ?object bl:category ?objectCategory . 
} WHERE {
  graph ?np_assertion {
    ?association
      bl:association_type ?association_type ;
      rdf:subject ?subject ;
      rdf:predicate ?predicate ;
      rdf:object ?object ;
      bl:relation ?relation ;
      bl:provided_by ?provided_by .
  }
  ?subject bl:category ?subjectCategory .
  ?object bl:category ?objectCategory .
  graph ?np_head {
    ?np_uri np:hasAssertion ?np_assertion .
  }
  FILTER NOT EXISTS { ?creator npx:retracts ?np_uri }
}
```

Query 2 does not filter out retracted nanopubs:

```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX bl: <https://w3id.org/biolink/vocab/>
PREFIX d2s: <https://w3id.org/d2s/>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX bio2rdf: <http://bio2rdf.org/>
PREFIX covid: <http://idlab.github.io/covid19#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dctypes: <http://purl.org/dc/dcmitype/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX idot: <http://identifiers.org/idot/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX void: <http://rdfs.org/ns/void#>
PREFIX void-ext: <http://ldf.fi/void-ext#>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX ncit: <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX schema: <http://schema.org/>
PREFIX omop: <http://api.ohdsi.org/WebAPI/vocabulary/concept/>
PREFIX cohd: <https://w3id.org/trek/cohd/>
CONSTRUCT {
  ?association
    bl:association_type ?association_type ;
    rdfs:label ?label ;
    rdf:subject ?subject ;
    rdf:predicate ?predicate ;
    rdf:object ?object ;
    bl:relation ?relation ;
  	bl:provided_by ?provided_by ;
    bl:has_evidence ?targetgroup ;
    bl:stage_qualifier ?lifestage .
  
  ?subject bl:category ?subjectCategory .
  ?object bl:category ?objectCategory . 

  ?targetgroup a ?targetGroupType ;
    bl:category ?targetGroupCategory ;
    bl:has_drug ?drug ;
    bl:has_phenotype ?phenotype .
  ?lifestage a bl:LifeStage ;
    rdfs:label ?lifestageLabel .
}
WHERE { 
  ?association
    bl:association_type ?association_type ;
    rdfs:label ?label ;
    rdf:subject ?subject ;
    rdf:predicate ?predicate ;
    rdf:object ?object ;
    bl:relation ?relation ;
  	bl:provided_by ?provided_by .
  
  	?subject bl:category ?subjectCategory .
  	?object bl:category ?objectCategory . 
   
  	OPTIONAL {
    	?association bl:has_evidence ?targetgroup .
  		?targetgroup a ?targetGroupType ;
    		bl:category ?targetGroupCategory .
	}
  	OPTIONAL {
      ?targetgroup bl:has_drug ?drug .
	}
  	OPTIONAL {
      ?targetgroup bl:has_phenotype ?phenotype .
	}  
  	OPTIONAL {
    	?association bl:stage_qualifier ?lifestage .
  		?lifestage a bl:LifeStage ;
    		rdfs:label ?lifestageLabel .
	}
}
```

## 🧪 Experimental

1. Use the **Nanopublication sandbox server**

* Server: http://test-server.nanopubs.lod.labs.vu.nl/
* grlc API: http://test-grlc.nanopubs.lod.labs.vu.nl/ 

2. Use a **Comunica SPARQL endpoint on the Nanopublications LDF server**

* Nanopublications [LDF](http://query.linkeddatafragments.org/) queried using [`comunica/actor-init-sparql`](https://hub.docker.com/r/comunica/actor-init-sparql)
* URL for SPARQL endpoint: [**http://nanopub-sparql.137.120.31.102.nip.io/sparql?query=**](http://nanopub-sparql.137.120.31.102.nip.io/sparql?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20owl%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20bl%3A%20%3Chttps%3A%2F%2Fw3id.org%2Fbiolink%2Fvocab%2F%3E%0APREFIX%20d2s%3A%20%3Chttps%3A%2F%2Fw3id.org%2Fd2s%2F%3E%0APREFIX%20sio%3A%20%3Chttp%3A%2F%2Fsemanticscience.org%2Fresource%2F%3E%0APREFIX%20bio2rdf%3A%20%3Chttp%3A%2F%2Fbio2rdf.org%2F%3E%0APREFIX%20covid%3A%20%3Chttp%3A%2F%2Fidlab.github.io%2Fcovid19%23%3E%0APREFIX%20dc%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0APREFIX%20dct%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX%20dctypes%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fdcmitype%2F%3E%0APREFIX%20foaf%3A%20%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0APREFIX%20idot%3A%20%3Chttp%3A%2F%2Fidentifiers.org%2Fidot%2F%3E%0APREFIX%20dcat%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%23%3E%0APREFIX%20void%3A%20%3Chttp%3A%2F%2Frdfs.org%2Fns%2Fvoid%23%3E%0APREFIX%20void-ext%3A%20%3Chttp%3A%2F%2Fldf.fi%2Fvoid-ext%23%3E%0APREFIX%20obo%3A%20%3Chttp%3A%2F%2Fpurl.obolibrary.org%2Fobo%2F%3E%0APREFIX%20ncit%3A%20%3Chttp%3A%2F%2Fncicb.nci.nih.gov%2Fxml%2Fowl%2FEVS%2FThesaurus.owl%23%3E%0APREFIX%20xsd%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX%20schema%3A%20%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX%20omop%3A%20%3Chttp%3A%2F%2Fapi.ohdsi.org%2FWebAPI%2Fvocabulary%2Fconcept%2F%3E%0APREFIX%20cohd%3A%20%3Chttps%3A%2F%2Fw3id.org%2Ftrek%2Fcohd%2F%3E%0ACONSTRUCT%20%7B%0A%20%20%3Fassociation%0A%20%20%20%20bl%3Aassociation_type%20%3Fassociation_type%20%3B%0A%20%20%20%20rdfs%3Alabel%20%3Flabel%20%3B%0A%20%20%20%20rdf%3Asubject%20%3Fsubject%20%3B%0A%20%20%20%20rdf%3Apredicate%20%3Fpredicate%20%3B%0A%20%20%20%20rdf%3Aobject%20%3Fobject%20%3B%0A%20%20%20%20bl%3Arelation%20%3Frelation%20%3B%0A%20%20%09bl%3Aprovided_by%20%3Fprovided_by%20%3B%0A%20%20%20%20bl%3Ahas_evidence%20%3Ftargetgroup%20%3B%0A%20%20%20%20bl%3Astage_qualifier%20%3Flifestage%20.%0A%20%20%0A%20%20%3Fsubject%20bl%3Acategory%20%3FsubjectCategory%20.%0A%20%20%3Fobject%20bl%3Acategory%20%3FobjectCategory%20.%20%0A%0A%20%20%3Ftargetgroup%20a%20%3FtargetGroupType%20%3B%0A%20%20%20%20bl%3Acategory%20%3FtargetGroupCategory%20%3B%0A%20%20%20%20bl%3Ahas_drug%20%3Fdrug%20%3B%0A%20%20%20%20bl%3Ahas_phenotype%20%3Fphenotype%20.%0A%20%20%3Flifestage%20a%20bl%3ALifeStage%20%3B%0A%20%20%20%20rdfs%3Alabel%20%3FlifestageLabel%20.%0A%7D%0AWHERE%20%7B%20%0A%20%20%3Fassociation%0A%20%20%20%20bl%3Aassociation_type%20%3Fassociation_type%20%3B%0A%20%20%20%20rdf%3Asubject%20%3Fsubject%20%3B%0A%20%20%20%20rdf%3Apredicate%20%3Fpredicate%20%3B%0A%20%20%20%20rdf%3Aobject%20%3Fobject%20%3B%0A%20%20%20%20bl%3Arelation%20%3Frelation%20%3B%0A%20%20%09bl%3Aprovided_by%20%3Fprovided_by%20.%0A%20%20%0A%20%20%3Fsubject%20bl%3Acategory%20%3FsubjectCategory%20.%0A%20%20%3Fobject%20bl%3Acategory%20%3FobjectCategory%20.%20%0A%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20rdfs%3Alabel%20%3Flabel%20.%0A%20%20%7D%0A%20%20%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20bl%3Ahas_evidence%20%3Ftargetgroup%20.%0A%20%20%20%20%3Ftargetgroup%20a%20%3FtargetGroupType%20%3B%0A%20%20%20%20%20%20bl%3Acategory%20%3FtargetGroupCategory%20.%0A%09%7D%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Ftargetgroup%20bl%3Ahas_drug%20%3Fdrug%20.%0A%09%7D%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Ftargetgroup%20bl%3Ahas_phenotype%20%3Fphenotype%20.%0A%09%7D%20%20%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20bl%3Astage_qualifier%20%3Flifestage%20.%0A%20%20%20%20%3Flifestage%20a%20bl%3ALifeStage%20%3B%0A%20%20%20%20%20%20rdfs%3Alabel%20%3FlifestageLabel%20.%0A%09%7D%0A%7D%0A)
* Or query it using the [YASGUI query editor](https://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20owl%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20bl%3A%20%3Chttps%3A%2F%2Fw3id.org%2Fbiolink%2Fvocab%2F%3E%0APREFIX%20d2s%3A%20%3Chttps%3A%2F%2Fw3id.org%2Fd2s%2F%3E%0APREFIX%20sio%3A%20%3Chttp%3A%2F%2Fsemanticscience.org%2Fresource%2F%3E%0APREFIX%20bio2rdf%3A%20%3Chttp%3A%2F%2Fbio2rdf.org%2F%3E%0APREFIX%20covid%3A%20%3Chttp%3A%2F%2Fidlab.github.io%2Fcovid19%23%3E%0APREFIX%20dc%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0APREFIX%20dct%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX%20dctypes%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fdcmitype%2F%3E%0APREFIX%20foaf%3A%20%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0APREFIX%20idot%3A%20%3Chttp%3A%2F%2Fidentifiers.org%2Fidot%2F%3E%0APREFIX%20dcat%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%23%3E%0APREFIX%20void%3A%20%3Chttp%3A%2F%2Frdfs.org%2Fns%2Fvoid%23%3E%0APREFIX%20void-ext%3A%20%3Chttp%3A%2F%2Fldf.fi%2Fvoid-ext%23%3E%0APREFIX%20obo%3A%20%3Chttp%3A%2F%2Fpurl.obolibrary.org%2Fobo%2F%3E%0APREFIX%20ncit%3A%20%3Chttp%3A%2F%2Fncicb.nci.nih.gov%2Fxml%2Fowl%2FEVS%2FThesaurus.owl%23%3E%0APREFIX%20xsd%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX%20schema%3A%20%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX%20omop%3A%20%3Chttp%3A%2F%2Fapi.ohdsi.org%2FWebAPI%2Fvocabulary%2Fconcept%2F%3E%0APREFIX%20cohd%3A%20%3Chttps%3A%2F%2Fw3id.org%2Ftrek%2Fcohd%2F%3E%0ACONSTRUCT%20%7B%0A%20%20%3Fassociation%0A%20%20%20%20bl%3Aassociation_type%20%3Fassociation_type%20%3B%0A%20%20%20%20rdfs%3Alabel%20%3Flabel%20%3B%0A%20%20%20%20rdf%3Asubject%20%3Fsubject%20%3B%0A%20%20%20%20rdf%3Apredicate%20%3Fpredicate%20%3B%0A%20%20%20%20rdf%3Aobject%20%3Fobject%20%3B%0A%20%20%20%20bl%3Arelation%20%3Frelation%20%3B%0A%20%20%09bl%3Aprovided_by%20%3Fprovided_by%20%3B%0A%20%20%20%20bl%3Ahas_evidence%20%3Ftargetgroup%20%3B%0A%20%20%20%20bl%3Astage_qualifier%20%3Flifestage%20.%0A%20%20%0A%20%20%3Fsubject%20bl%3Acategory%20%3FsubjectCategory%20.%0A%20%20%3Fobject%20bl%3Acategory%20%3FobjectCategory%20.%20%0A%0A%20%20%3Ftargetgroup%20a%20%3FtargetGroupType%20%3B%0A%20%20%20%20bl%3Acategory%20%3FtargetGroupCategory%20%3B%0A%20%20%20%20bl%3Ahas_drug%20%3Fdrug%20%3B%0A%20%20%20%20bl%3Ahas_phenotype%20%3Fphenotype%20.%0A%20%20%3Flifestage%20a%20bl%3ALifeStage%20%3B%0A%20%20%20%20rdfs%3Alabel%20%3FlifestageLabel%20.%0A%7D%0AWHERE%20%7B%20%0A%20%20%3Fassociation%0A%20%20%20%20bl%3Aassociation_type%20%3Fassociation_type%20%3B%0A%20%20%20%20rdf%3Asubject%20%3Fsubject%20%3B%0A%20%20%20%20rdf%3Apredicate%20%3Fpredicate%20%3B%0A%20%20%20%20rdf%3Aobject%20%3Fobject%20%3B%0A%20%20%20%20bl%3Arelation%20%3Frelation%20%3B%0A%20%20%09bl%3Aprovided_by%20%3Fprovided_by%20.%0A%20%20%0A%20%20%3Fsubject%20bl%3Acategory%20%3FsubjectCategory%20.%0A%20%20%3Fobject%20bl%3Acategory%20%3FobjectCategory%20.%20%0A%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20rdfs%3Alabel%20%3Flabel%20.%0A%20%20%7D%0A%20%20%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20bl%3Ahas_evidence%20%3Ftargetgroup%20.%0A%20%20%20%20%3Ftargetgroup%20a%20%3FtargetGroupType%20%3B%0A%20%20%20%20%20%20bl%3Acategory%20%3FtargetGroupCategory%20.%0A%09%7D%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Ftargetgroup%20bl%3Ahas_drug%20%3Fdrug%20.%0A%09%7D%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Ftargetgroup%20bl%3Ahas_phenotype%20%3Fphenotype%20.%0A%09%7D%20%20%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20bl%3Astage_qualifier%20%3Flifestage%20.%0A%20%20%20%20%3Flifestage%20a%20bl%3ALifeStage%20%3B%0A%20%20%20%20%20%20rdfs%3Alabel%20%3FlifestageLabel%20.%0A%09%7D%0A%7D%0A&endpoint=http%3A%2F%2Fnanopub-sparql.137.120.31.102.nip.io%2Fsparql&requestMethod=GET&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=text%2Fturtle%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table).
* Or checkout an association directly in the LDF: http://ldf.np.dumontierlab.com/np?subject=https%3A%2F%2Fw3id.org%2Fum%2Fneurodkg%2FDB01148_OMIM231200
* Checkout a BioLink-compliant nanopub: http://server.nanopubs.lod.labs.vu.nl/RAavLF3YkTN96cEi1YWpFVXr_X2Czh3hzQXFAHkGGYrUo