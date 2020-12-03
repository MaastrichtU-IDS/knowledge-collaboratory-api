[![Python versions](https://img.shields.io/pypi/pyversions/nanopub-reasoner-api)](https://pypi.org/project/nanopub-reasoner-api)

# Use the API 📬

### Query operation

The user sends a [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) query asking for the predicted targets given: a source, and the relation to predict. The query is a graph with nodes and edges defined in JSON, and uses classes from the [BioLink model](https://biolink.github.io/biolink-model).

See this [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) query example:

```json
{
  "message": {
    "query_graph": {
      "edges": [
        {
          "id": "e00",
          "source_id": "n00",
          "target_id": "n01",
          "type": "treated_by"
        }
      ],
      "nodes": [
        {
          "curie": "DRUGBANK:DB00394",
          "id": "n00",
          "type": "drug"
        },
        {
          "id": "n01",
          "type": "disease"
        }
      ]
    }
  }
}
```

### Predicates operation

The `/predicates` operation will return the entities and relations provided by this API in a JSON object (following the [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) specifications).

> Try it at [https://nanopub-reasoner-api.137.120.31.102.nip.io/predicates](https://nanopub-reasoner-api.137.120.31.102.nip.io/predicates)

### Notebook example

> TODO

# Deploy the API 📦

You can also use nanopub-reasoner-api to build new classifiers, and deploy your API.

> Requires [Python 3.6+](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)

### Install the API 📥

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

### Start the API 🛩️

In debug mode for development with Flask:

```bash
python3.7 src/api.py debug
```

In production mode with Tornado:

```bash
python3.7 src/api.py
```

> Access the Swagger UI at [http://localhost:8808](http://localhost:8808)

#### Alternative: Run with Docker

Running using Docker can be convenient if you just want to run the API without installing the package locally, or if it runs in production alongside other services.

Build and start the `nanopub-reasoner-api-api` container with [docker-compose 🐳](https://docs.docker.com/compose/)

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

# Acknowledgments

* Service supported by the [NCATS Translator project](https://ncats.nih.gov/translator/about). 
