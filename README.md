Query the Nanopublication network using SPARQL and Translator Reasoner API at http://nanopub-reasoner-api.137.120.31.102.nip.io/ 

This repository provides guidelines to publish Nanopublications as a user with the Nanobench, and query the published Nanopublications network as a researcher searching for answers 💬

![PSKG](PSKG-knowledge_collaboratory.png)

## Publish Nanopublications

Use the [Nanobench](https://github.com/vemonet/nanobench) to publish and explore nanopublications using a convenient web UI.

Download the latest release of the Nanobench jar file for the Translator ecosystem in `~/.nanopub/nanobench.jar`:

```bash
curl -s https://api.github.com/repos/vemonet/nanobench/releases/latest | grep "browser_download_url.*.jar" | cut -d : -f 2,3 | tr -d \" | wget -O ~/.nanopub/nanobench.jar -i -
```

Run the Nanobench (it will use the `ids_rsa` key in the `.nanopub` folder to authenticate):

```bash
java -jar ~/.nanopub/nanobench.jar -httpPort 37373 -resetExtract
```

> Access on http://localhost:37373

> Check the [vemonet/nanobench wiki](https://github.com/vemonet/nanobench/wiki/Add-an-evidence-to-an-association) to get a full tutorial to publish associations.

Templates for the Translator (e.g. "Defining a biomedical association") can be seen and improved in [the MaastrichtU-IDS/nanobench-templates GitHub repository](https://github.com/MaastrichtU-IDS/nanobench-templates/tree/master/templates/translator).

## Query with the Translator Reasoner API 📬

An Open API is available to query the Nanopublications network using the [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) standards.

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

> Try it at [https://nanopub-reasoner-api.137.120.31.102.nip.io/predicates](https://nanopub-reasoner-api.137.120.31.102.nip.io/predicates)

## Run the API with Docker

Running using Docker can be convenient if you just want to run the API without installing the package locally, or if it runs in production alongside other services.

2 services are started:

* A SPARQL endpoint to query the Nanopublication network of HDT files using `comunica/actor-init-sparql`
* A Reasoner API to query the SPARQL endpoint, using https://github.com/MaastrichtU-IDS/d2s-api/tree/develop

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

# Acknowledgments

Service funded by the [NIH NCATS Translator project](https://ncats.nih.gov/translator/about). 

![Funded the the NIH NCATS Translator project](https://ncats.nih.gov/files/TranslatorGraphic2020_1100x420.jpg)