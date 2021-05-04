[![TRAPI version](https://img.shields.io/badge/TRAPI-v1.0.0-blueviolet)](https://github.com/NCATSTranslator/ReasonerAPI) [![Test production API](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions/workflows/run-tests-prod.yml/badge.svg)](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions/workflows/run-tests-prod.yml) [![Generate KGX from Knowledge Collaboratory](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions/workflows/generate-kgx.yml/badge.svg)](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions/workflows/generate-kgx.yml)

This repository provides guidelines to publish Nanopublications as a user with the Nanobench, and query the published Nanopublications network as a researcher searching for answers 💬

Services has been been deployed publicly to query the Nanopublications network using Translator standards to retrieve the Knowledge Collaboratory graph, a collection of drug indications annotated using preferred identifiers (usually from MONDO, CHEBI, DrugBank, etc).

Check the **Translator Reasoner API** to query the Nanopublications network SPARQL endpoint at

**[🔗 https://api.collaboratory.semanticscience.org](https://api.collaboratory.semanticscience.org)**

* Supports [Translator Reasoner API](https://github.com/NCATSTranslator/ReasonerAPI) `1.0.0`
* Include operation to retrieve the Knowledge Collaboratory nanopublications in the [`kgx`](https://github.com/biolink/kgx) format

## The Knowledge Collaboratory concept

![PSKG](PSKG-knowledge_collaboratory.png)

## Publish Nanopublications 📬

### Publish with the Nanobench UI

Requirements: [Java 8+](https://openjdk.java.net/install/)

Use the [Nanobench 🛋️](https://github.com/peta-pico/nanobench) to publish and explore nanopublications using a convenient web UI.

Download the latest release of the `nanobench.zip` file from GitHub: https://github.com/peta-pico/nanobench/releases/tag/nanobench-1.19

Unzip the file, and put the jar file in a convenient folder (at `~/.nanopub/nanobench.jar` for example, to be able to call it from anywhere easily)

> Visit the [complete nanobench installation instructions](https://github.com/peta-pico/nanobench/blob/master/INSTALL.md) for more details.

Run the Nanobench on http://localhost:37373. It will use the `ids_rsa` key in the `.nanopub` folder to authenticate, or guide you to generate one:

```bash
java -jar ~/.nanopub/nanobench.jar -httpPort 37373 -resetExtract
```

See also:

* Check the [vemonet/nanobench wiki](https://github.com/vemonet/nanobench/wiki/Add-an-evidence-to-an-association) to get a full tutorial to publish associations!
* Templates for the Translator (e.g. "Defining a biomedical association with its context") can be seen and improved in [the MaastrichtU-IDS/nanobench-templates GitHub repository](https://github.com/MaastrichtU-IDS/nanobench-templates/tree/master/templates/translator).

### Publish a tabular file with python

1. Use the [BioLink JSON-LD Context file](https://github.com/biolink/biolink-model/blob/master/context.jsonld) to use the right URIs (so that Translator tools can map them to CURIEs)
2. Checkout the [`src/publish_nanopubs.py`](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/blob/master/src/publish_nanopubs.py) file to see an example for generating nanopublications for drug indications from a simple TSV file.

## Deploy the Knowledge Collaboratory API 🚀

Starts the **Translator Reasoner API to query the Nanopublications SPARQL endpoint**

* Query the Knowledge Collaboratory Nanopublications (drug indications in the BioLink format) using the [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) standards and [KGX](https://github.com/biolink/kgx)
  * Supports [Translator Reasoner API](https://github.com/NCATSTranslator/ReasonerAPI) `1.0.0` 
  * Include operation to retrieve the Knowledge Collaboratory nanopublications in the `kgx` format
  * The TRAPI-SPARQL interface and `kgx` transformer are implemented in Python in the `src/` folder
* OpenAPI 3 with Swagger UI, built in Python using [zalando/connexion](https://github.com/zalando/connexion)

Available at **[https://api.collaboratory.semanticscience.org 🔗](https://api.collaboratory.semanticscience.org)**

Starts the **Translator Reasoner API to query the Nanopublications SPARQL endpoint**, supporting `kgx` and TRAPI `1.0.0` (defined in this repo in `src/`)

> Requires [Python 3.7+](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)

Clone the repository first

```bash
git clone https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api.git
cd knowledge-collaboratory-api
```

### Start the API locally 🛩️

Install dependencies

```bash
pip3 install -r requirements.txt
```

> If you are facing conflict with already installed packages, then you might want to use a [Virtual Environment](https://docs.python.org/3/tutorial/venv.html) to isolate the installation in the current folder before installing knowledge-collaboratory-api:
>
> ```bash
> # Create the virtual environment folder in your workspace
> python3.8 -m venv .venv
> # Activate it using a script in the created folder
> source .venv/bin/activate
> ```

Start the API in **production** mode on http://localhost:8808 with Tornado:

```bash
python3 src/api.py
```

Or start the API in **debug** mode with Flask (the API will be reloaded automatically at each change to the code):

```bash
python3 src/api.py debug
```

>  Check [CONTRIBUTING.md](/CONTRIBUTING.md) for more details on how to run the API locally and contribute.

### Start with Docker 🐳

Requirements: [Docker](https://docs.docker.com/get-docker/).

Build and start the container with [docker-compose 🐳](https://docs.docker.com/compose/)

```bash
docker-compose up -d --build
```

> Access the Swagger UI at [http://localhost:8808](http://localhost:8808)

> We use [nginx-proxy](https://github.com/nginx-proxy/nginx-proxy) and [docker-letsencrypt-nginx-proxy-companion](https://github.com/nginx-proxy/docker-letsencrypt-nginx-proxy-companion) as reverse proxy for HTTP and HTTPS in production. You can change the proxy URL and port via environment variables `VIRTUAL_HOST`, `VIRTUAL_PORT` and `LETSENCRYPT_HOST` in the [docker-compose.yml](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/blob/master/docker-compose.yml) file.

Check the logs:

```bash
docker-compose logs
```

Stop the container:

```bash
docker-compose down
```

### Test the Collaboratory API

See the [`TESTING.md`](/TESTING.md) file for more details on testing the API.

## Overview of API operations 🧭

Overview of the different operations available in the Knowledge Collaboratory Translator Reasoner API (supporting `kgx`)

### Query operation

The user sends a [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) query to the Knowledge Collaboratory Nanopublications in the BioLink format (e.g. drug indications). The query is a graph with nodes and edges defined in JSON, and uses classes from the [BioLink model](https://biolink.github.io/biolink-model).

### Predicates operation

The `/predicates` operation will return the entities and relations provided by this API in a JSON object (following the [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) specifications).

### Kgx operation

The `/kgx` operation will return the complete Knowledge Collaboratory drug indications in [KGX](https://github.com/biolink/kgx) TSV format (in a `.zip` file)

## Current resources in the Collaboratory

* Drugs indications from the [PREDICT publication](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3159979/)

* Drugs indications from the [NeuroDKG](https://github.com/MaastrichtU-IDS/neuro_dkg/), and off-label drug indications

# Acknowledgments

Service funded by the [NIH NCATS Translator project](https://ncats.nih.gov/translator/about). 

![Funded the the NIH NCATS Translator project](https://ncats.nih.gov/files/TranslatorGraphic2020_1100x420.jpg)