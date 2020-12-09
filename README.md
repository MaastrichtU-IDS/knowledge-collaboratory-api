[![Generate KGX graphs from RDF](https://github.com/MaastrichtU-IDS/nanopub-trapi/workflows/Generate%20KGX%20graphs%20from%20RDF/badge.svg)](https://github.com/MaastrichtU-IDS/nanopub-trapi/actions?query=workflow%3A%22Generate+KGX+graphs+from+RDF%22) [![Validate RDF graphs](https://github.com/MaastrichtU-IDS/nanopub-trapi/workflows/Validate%20RDF%20graphs/badge.svg)](https://github.com/MaastrichtU-IDS/nanopub-trapi/actions?query=workflow%3A%22Validate+RDF+graphs%22)

This repository provides guidelines to publish Nanopublications as a user with the Nanobench, and query the published Nanopublications network as a researcher searching for answers 💬

Services has been been deployed publicly to query the Nanopublications network using Translator standards to retrieve the Knowledge Collaboratory graph, a collection of drug indications annotated using preferred identifiers (usually from MONDO, CHEBI, DrugBank, etc).

* A **SPARQL endpoint** to query the Nanopublications network
  * Nanopublications [LDF](http://query.linkeddatafragments.org/) queried using [`comunica/actor-init-sparql`](https://hub.docker.com/r/comunica/actor-init-sparql)
  
  * URL for SPARQL endpoint: [**http://nanopub-sparql.137.120.31.102.nip.io/sparql?query=**](http://nanopub-sparql.137.120.31.102.nip.io/sparql?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20owl%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20bl%3A%20%3Chttps%3A%2F%2Fw3id.org%2Fbiolink%2Fvocab%2F%3E%0APREFIX%20d2s%3A%20%3Chttps%3A%2F%2Fw3id.org%2Fd2s%2F%3E%0APREFIX%20sio%3A%20%3Chttp%3A%2F%2Fsemanticscience.org%2Fresource%2F%3E%0APREFIX%20bio2rdf%3A%20%3Chttp%3A%2F%2Fbio2rdf.org%2F%3E%0APREFIX%20covid%3A%20%3Chttp%3A%2F%2Fidlab.github.io%2Fcovid19%23%3E%0APREFIX%20dc%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0APREFIX%20dct%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX%20dctypes%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fdcmitype%2F%3E%0APREFIX%20foaf%3A%20%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0APREFIX%20idot%3A%20%3Chttp%3A%2F%2Fidentifiers.org%2Fidot%2F%3E%0APREFIX%20dcat%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%23%3E%0APREFIX%20void%3A%20%3Chttp%3A%2F%2Frdfs.org%2Fns%2Fvoid%23%3E%0APREFIX%20void-ext%3A%20%3Chttp%3A%2F%2Fldf.fi%2Fvoid-ext%23%3E%0APREFIX%20obo%3A%20%3Chttp%3A%2F%2Fpurl.obolibrary.org%2Fobo%2F%3E%0APREFIX%20ncit%3A%20%3Chttp%3A%2F%2Fncicb.nci.nih.gov%2Fxml%2Fowl%2FEVS%2FThesaurus.owl%23%3E%0APREFIX%20xsd%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX%20schema%3A%20%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX%20omop%3A%20%3Chttp%3A%2F%2Fapi.ohdsi.org%2FWebAPI%2Fvocabulary%2Fconcept%2F%3E%0APREFIX%20cohd%3A%20%3Chttps%3A%2F%2Fw3id.org%2Ftrek%2Fcohd%2F%3E%0ACONSTRUCT%20%7B%0A%20%20%3Fassociation%0A%20%20%20%20bl%3Aassociation_type%20%3Fassociation_type%20%3B%0A%20%20%20%20rdfs%3Alabel%20%3Flabel%20%3B%0A%20%20%20%20rdf%3Asubject%20%3Fsubject%20%3B%0A%20%20%20%20rdf%3Apredicate%20%3Fpredicate%20%3B%0A%20%20%20%20rdf%3Aobject%20%3Fobject%20%3B%0A%20%20%20%20bl%3Arelation%20%3Frelation%20%3B%0A%20%20%09bl%3Aprovided_by%20%3Fprovided_by%20%3B%0A%20%20%20%20bl%3Ahas_evidence%20%3Ftargetgroup%20%3B%0A%20%20%20%20bl%3Astage_qualifier%20%3Flifestage%20.%0A%20%20%0A%20%20%3Fsubject%20bl%3Acategory%20%3FsubjectCategory%20.%0A%20%20%3Fobject%20bl%3Acategory%20%3FobjectCategory%20.%20%0A%0A%20%20%3Ftargetgroup%20a%20%3FtargetGroupType%20%3B%0A%20%20%20%20bl%3Acategory%20%3FtargetGroupCategory%20%3B%0A%20%20%20%20bl%3Ahas_drug%20%3Fdrug%20%3B%0A%20%20%20%20bl%3Ahas_phenotype%20%3Fphenotype%20.%0A%20%20%3Flifestage%20a%20bl%3ALifeStage%20%3B%0A%20%20%20%20rdfs%3Alabel%20%3FlifestageLabel%20.%0A%7D%0AWHERE%20%7B%20%0A%20%20%3Fassociation%0A%20%20%20%20bl%3Aassociation_type%20%3Fassociation_type%20%3B%0A%20%20%20%20rdf%3Asubject%20%3Fsubject%20%3B%0A%20%20%20%20rdf%3Apredicate%20%3Fpredicate%20%3B%0A%20%20%20%20rdf%3Aobject%20%3Fobject%20%3B%0A%20%20%20%20bl%3Arelation%20%3Frelation%20%3B%0A%20%20%09bl%3Aprovided_by%20%3Fprovided_by%20.%0A%20%20%0A%20%20%3Fsubject%20bl%3Acategory%20%3FsubjectCategory%20.%0A%20%20%3Fobject%20bl%3Acategory%20%3FobjectCategory%20.%20%0A%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20rdfs%3Alabel%20%3Flabel%20.%0A%20%20%7D%0A%20%20%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20bl%3Ahas_evidence%20%3Ftargetgroup%20.%0A%20%20%20%20%3Ftargetgroup%20a%20%3FtargetGroupType%20%3B%0A%20%20%20%20%20%20bl%3Acategory%20%3FtargetGroupCategory%20.%0A%09%7D%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Ftargetgroup%20bl%3Ahas_drug%20%3Fdrug%20.%0A%09%7D%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Ftargetgroup%20bl%3Ahas_phenotype%20%3Fphenotype%20.%0A%09%7D%20%20%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20bl%3Astage_qualifier%20%3Flifestage%20.%0A%20%20%20%20%3Flifestage%20a%20bl%3ALifeStage%20%3B%0A%20%20%20%20%20%20rdfs%3Alabel%20%3FlifestageLabel%20.%0A%09%7D%0A%7D%0A)
  
  * Or query it using the [YASGUI query editor](https://yasgui.triply.cc/#query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20owl%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20bl%3A%20%3Chttps%3A%2F%2Fw3id.org%2Fbiolink%2Fvocab%2F%3E%0APREFIX%20d2s%3A%20%3Chttps%3A%2F%2Fw3id.org%2Fd2s%2F%3E%0APREFIX%20sio%3A%20%3Chttp%3A%2F%2Fsemanticscience.org%2Fresource%2F%3E%0APREFIX%20bio2rdf%3A%20%3Chttp%3A%2F%2Fbio2rdf.org%2F%3E%0APREFIX%20covid%3A%20%3Chttp%3A%2F%2Fidlab.github.io%2Fcovid19%23%3E%0APREFIX%20dc%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0APREFIX%20dct%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX%20dctypes%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fdcmitype%2F%3E%0APREFIX%20foaf%3A%20%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0APREFIX%20idot%3A%20%3Chttp%3A%2F%2Fidentifiers.org%2Fidot%2F%3E%0APREFIX%20dcat%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%23%3E%0APREFIX%20void%3A%20%3Chttp%3A%2F%2Frdfs.org%2Fns%2Fvoid%23%3E%0APREFIX%20void-ext%3A%20%3Chttp%3A%2F%2Fldf.fi%2Fvoid-ext%23%3E%0APREFIX%20obo%3A%20%3Chttp%3A%2F%2Fpurl.obolibrary.org%2Fobo%2F%3E%0APREFIX%20ncit%3A%20%3Chttp%3A%2F%2Fncicb.nci.nih.gov%2Fxml%2Fowl%2FEVS%2FThesaurus.owl%23%3E%0APREFIX%20xsd%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX%20schema%3A%20%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX%20omop%3A%20%3Chttp%3A%2F%2Fapi.ohdsi.org%2FWebAPI%2Fvocabulary%2Fconcept%2F%3E%0APREFIX%20cohd%3A%20%3Chttps%3A%2F%2Fw3id.org%2Ftrek%2Fcohd%2F%3E%0ACONSTRUCT%20%7B%0A%20%20%3Fassociation%0A%20%20%20%20bl%3Aassociation_type%20%3Fassociation_type%20%3B%0A%20%20%20%20rdfs%3Alabel%20%3Flabel%20%3B%0A%20%20%20%20rdf%3Asubject%20%3Fsubject%20%3B%0A%20%20%20%20rdf%3Apredicate%20%3Fpredicate%20%3B%0A%20%20%20%20rdf%3Aobject%20%3Fobject%20%3B%0A%20%20%20%20bl%3Arelation%20%3Frelation%20%3B%0A%20%20%09bl%3Aprovided_by%20%3Fprovided_by%20%3B%0A%20%20%20%20bl%3Ahas_evidence%20%3Ftargetgroup%20%3B%0A%20%20%20%20bl%3Astage_qualifier%20%3Flifestage%20.%0A%20%20%0A%20%20%3Fsubject%20bl%3Acategory%20%3FsubjectCategory%20.%0A%20%20%3Fobject%20bl%3Acategory%20%3FobjectCategory%20.%20%0A%0A%20%20%3Ftargetgroup%20a%20%3FtargetGroupType%20%3B%0A%20%20%20%20bl%3Acategory%20%3FtargetGroupCategory%20%3B%0A%20%20%20%20bl%3Ahas_drug%20%3Fdrug%20%3B%0A%20%20%20%20bl%3Ahas_phenotype%20%3Fphenotype%20.%0A%20%20%3Flifestage%20a%20bl%3ALifeStage%20%3B%0A%20%20%20%20rdfs%3Alabel%20%3FlifestageLabel%20.%0A%7D%0AWHERE%20%7B%20%0A%20%20%3Fassociation%0A%20%20%20%20bl%3Aassociation_type%20%3Fassociation_type%20%3B%0A%20%20%20%20rdf%3Asubject%20%3Fsubject%20%3B%0A%20%20%20%20rdf%3Apredicate%20%3Fpredicate%20%3B%0A%20%20%20%20rdf%3Aobject%20%3Fobject%20%3B%0A%20%20%20%20bl%3Arelation%20%3Frelation%20%3B%0A%20%20%09bl%3Aprovided_by%20%3Fprovided_by%20.%0A%20%20%0A%20%20%3Fsubject%20bl%3Acategory%20%3FsubjectCategory%20.%0A%20%20%3Fobject%20bl%3Acategory%20%3FobjectCategory%20.%20%0A%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20rdfs%3Alabel%20%3Flabel%20.%0A%20%20%7D%0A%20%20%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20bl%3Ahas_evidence%20%3Ftargetgroup%20.%0A%20%20%20%20%3Ftargetgroup%20a%20%3FtargetGroupType%20%3B%0A%20%20%20%20%20%20bl%3Acategory%20%3FtargetGroupCategory%20.%0A%09%7D%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Ftargetgroup%20bl%3Ahas_drug%20%3Fdrug%20.%0A%09%7D%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Ftargetgroup%20bl%3Ahas_phenotype%20%3Fphenotype%20.%0A%09%7D%20%20%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fassociation%20bl%3Astage_qualifier%20%3Flifestage%20.%0A%20%20%20%20%3Flifestage%20a%20bl%3ALifeStage%20%3B%0A%20%20%20%20%20%20rdfs%3Alabel%20%3FlifestageLabel%20.%0A%09%7D%0A%7D%0A&endpoint=http%3A%2F%2Fnanopub-sparql.137.120.31.102.nip.io%2Fsparql&requestMethod=GET&tabTitle=Query&headers=%7B%7D&contentTypeConstruct=text%2Fturtle%2C*%2F*%3Bq%3D0.9&contentTypeSelect=application%2Fsparql-results%2Bjson%2C*%2F*%3Bq%3D0.9&outputFormat=table).
  
  * Or checkout an association directly in the LDF: http://ldf.np.dumontierlab.com/np?subject=https%3A%2F%2Fw3id.org%2Fum%2Fneurodkg%2FDB01148_OMIM231200
  
  * Checkout the nanopub: http://server.nanopubs.lod.labs.vu.nl/RAavLF3YkTN96cEi1YWpFVXr_X2Czh3hzQXFAHkGGYrUo
  
  * Try this SPARQL query:
  
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

* A **Translator Reasoner API** to query the SPARQL endpoint
  * Using the [d2s-api](https://github.com/MaastrichtU-IDS/d2s-api/tree/develop), with Java and [TRAPI](https://github.com/NCATSTranslator/ReasonerAPI) `0.9.0`
  * **http://nanopub-reasoner-api.137.120.31.102.nip.io**
* A **new Translator Reasoner API** to query the SPARQL endpoint
  * Supporting `kgx` and [TRAPI](https://github.com/NCATSTranslator/ReasonerAPI) `1.0.0-beta` (work in progress)
  * In python, defined in this repo in `src/`
  * **http://nanopub-kgx-api.137.120.31.102.nip.io**

## The Knowledge Collaboratory vision

![PSKG](PSKG-knowledge_collaboratory.png)

## Publish Nanopublications

### Nanopublish with the Nanobench UI

Requirements: [Java 8+](https://openjdk.java.net/install/)

Use the [Nanobench 🛋️](https://github.com/vemonet/nanobench) to publish and explore nanopublications using a convenient web UI.

Download the latest release of the Nanobench jar file for the Translator ecosystem by running this command:

```bash
curl -s https://api.github.com/repos/vemonet/nanobench/releases/latest | grep "browser_download_url.*.jar" | cut -d : -f 2,3 | tr -d \" | wget -O ~/.nanopub/nanobench.jar -i -
```

> The jar file is downloaded in your home folder: `~/.nanopub/nanobench.jar`

Run the Nanobench on http://localhost:37373. It will use the `ids_rsa` key in the `.nanopub` folder to authenticate, or guide you to generate one:

```bash
java -jar ~/.nanopub/nanobench.jar -httpPort 37373 -resetExtract
```

See also:

* Check the [vemonet/nanobench wiki](https://github.com/vemonet/nanobench/wiki/Add-an-evidence-to-an-association) to get a full tutorial to publish associations!
* Templates for the Translator (e.g. "Defining a biomedical association with its context") can be seen and improved in [the MaastrichtU-IDS/nanobench-templates GitHub repository](https://github.com/MaastrichtU-IDS/nanobench-templates/tree/master/templates/translator).

### Nanopublish a tabular file with python

1. Use the [BioLink JSON-LD Context file](https://github.com/biolink/biolink-model/blob/master/context.jsonld) to use the right URIs (so that Translator tools can map them to CURIEs)
2. Checkout the [`src/publish_nanopubs.py`](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/blob/master/src/publish_nanopubs.py) file to see an example for generating nanopublications for drug indications from a simple TSV file.

## Query with the Nanopublications network 📬

Using the Nanobench, SPARQL endpoint, or the Translator Reasoner APIs we built.

Deploy the new TRAPI: a Reasoner OpenAPI in Python, using [connexion](https://github.com/zalando/connexion), to query the Knowledge Collaboratory Nanopublications (drug indications in the BioLink format) using the [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) standards and KGX.

> Requires [Python 3.7+](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)

### Install the new API 📥

> Work in progress: the Reasoner API calls have not been implemented yet, only the KGX call works.

#### Clone the repository

```bash
git clone https://github.com/MaastrichtU-IDS/nanopub-reasoner-api.git
cd nanopub-trapi
```

#### Install dependencies

```bash
pip3 install -r requirements.txt
```

#### Optional: isolate with a Virtual Environment

If you are facing conflict with already installed packages, then you might want to use a [Virtual Environment](https://docs.python.org/3/tutorial/venv.html) to isolate the installation in the current folder before installing nanopub-reasoner-api:

```bash
# Create the virtual environment folder in your workspace
python3 -m venv .venv
# Activate it using a script in the created folder
source .venv/bin/activate
```

### Start the API locally 🛩️

By default it will use the public SPARQL endpoint http://nanopub-sparql.137.120.31.102.nip.io/sparql

In **debug** mode for development with Flask:

```bash
python3 src/api.py debug
```

Or in **production** mode with Tornado:

```bash
python3 src/api.py
```

> Access the Swagger UI at http://localhost:8808

## Run the SPARQL endpoint and APIs with Docker

Requirements: [Docker](https://docs.docker.com/get-docker/).

Running using Docker can be convenient if you just want to run the API without installing the package locally, or if it runs in production alongside other services.

3 services are started:

* **A SPARQL endpoint to query the Nanopublications** network of HDT files using `comunica/actor-init-sparql`
* **A Reasoner API to query the SPARQL endpoint**, using the [d2s-api](https://github.com/MaastrichtU-IDS/d2s-api/tree/develop) (Java, TRAPI `0.9.0`)
* **A new Reasoner API to query the SPARQL endpoint**, supporting `kgx` and TRAPI `1.0.0-beta` (defined in this repo in `src/`)

Build and start the container with [docker-compose 🐳](https://docs.docker.com/compose/)

```bash
docker-compose up -d
```

> Access the Swagger UI at [http://localhost:8808](http://localhost:8808)

> We use [nginx-proxy](https://github.com/nginx-proxy/nginx-proxy) and [docker-letsencrypt-nginx-proxy-companion](https://github.com/nginx-proxy/docker-letsencrypt-nginx-proxy-companion) as reverse proxy for HTTP and HTTPS in production. You can change the proxy URL and port via environment variables `VIRTUAL_HOST`, `VIRTUAL_PORT` and `LETSENCRYPT_HOST` in the [docker-compose.yml](https://github.com/MaastrichtU-IDS/nanopub-reasoner-api/blob/master/docker-compose.yml) file.

Check the logs:

```bash
docker-compose logs
```

Stop the container:

```bash
docker-compose down
```

## List of the API operations

Of the new Translator Reasoner API (supporting `kgx`)

### Query operation

The user sends a [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) query asking for the predicted targets given: a source, and the relation to predict. The query is a graph with nodes and edges defined in JSON, and uses classes from the [BioLink model](https://biolink.github.io/biolink-model).

See this [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) query example:

```json
{
  "max_results": 50,
  "message": {
    "query_graph": {
      "nodes": [
        { "id": "n00", "type": "Drug" },
        { "id": "n01", "type": "Disease" }
      ],
      "edges": [
        { "id": "e00", "type": "Association",
          "source_id": "n00", "target_id": "n01" }
      ]
    }
  }
}
```

### Predicates operation

The `/predicates` operation will return the entities and relations provided by this API in a JSON object (following the [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) specifications).

### Kgx operation

The `/kgx` operation will return the complete Knowledge Collaboratory drug indications in KGX TSV format (in a `.zip` file)

## Workflows to generate KGX files from RDF graphs

[![Generate KGX graphs from RDF](https://github.com/MaastrichtU-IDS/nanopub-trapi/workflows/Generate%20KGX%20graphs%20from%20RDF/badge.svg)](https://github.com/MaastrichtU-IDS/nanopub-trapi/actions?query=workflow%3A%22Generate+KGX+graphs+from+RDF%22) [![Validate RDF graphs](https://github.com/MaastrichtU-IDS/nanopub-trapi/workflows/Validate%20RDF%20graphs/badge.svg)](https://github.com/MaastrichtU-IDS/nanopub-trapi/actions?query=workflow%3A%22Validate+RDF+graphs%22)

We use [GitHub Actions workflows](https://github.com/MaastrichtU-IDS/nanopub-trapi/tree/master/.github/workflows) to validate, and transform to KGX TSV files, RDF graphs:

* [`.github/workflows/generate-kgx.yml`](https://github.com/MaastrichtU-IDS/nanopub-trapi/blob/master/.github/workflows/generate-kgx.yml)
* [`.github/workflows/validate-rdf.yml`](https://github.com/MaastrichtU-IDS/nanopub-trapi/blob/master/.github/workflows/validate-rdf.yml)

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
         --data ../nanopub-trapi/output/neurodkg.ttl"
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

# Acknowledgments

Service funded by the [NIH NCATS Translator project](https://ncats.nih.gov/translator/about). 

![Funded the the NIH NCATS Translator project](https://ncats.nih.gov/files/TranslatorGraphic2020_1100x420.jpg)