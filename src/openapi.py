import os
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from reasoner_pydantic import Query, Message
from typing import Optional, List, Dict, Any


class TRAPI(FastAPI):
    """Translator Reasoner API - wrapper for FastAPI."""

    required_tags = [
        {"name": "reasoner"},
        {"name": "trapi"},
        {"name": "translator"},
    ]

    def __init__(
        self,
        *args,
        # contact: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        super().__init__(
            *args,
            title='Knowledge Collaboratory API',
            root_path_in_servers=False,
            **kwargs,
        )

        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def openapi(self) -> Dict[str, Any]:
        """Build custom OpenAPI schema."""
        if self.openapi_schema:
            return self.openapi_schema

        tags = self.required_tags
        if self.openapi_tags:
            tags += self.openapi_tags
    
        openapi_schema = get_openapi(
            title='Knowledge Collaboratory API',
            version='1.0.0',
            openapi_version='3.0.1',
            description="""Translator Reasoner API for the Knowledge Collaboratory, hosted on the [Nanopublications network](http://nanopub.org/wordpress/), for annotated drug indications or any other BioLink-compliant claims.
\n\n This Open API supports [Translator Reasoner API](https://github.com/NCATSTranslator/ReasonerAPI) queries
\n\nSee the API GitHub repository: [github.com/MaastrichtU-IDS/knowledge-collaboratory-api](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api)
\n\n[![Test production API](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions/workflows/run-tests-prod.yml/badge.svg)](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions/workflows/run-tests-prod.yml)
\n\nThis service is supported by the [NCATS Translator project](https://ncats.nih.gov/translator/about)""",
            routes=self.routes,
            tags=tags,
        )

        if os.getenv('LETSENCRYPT_HOST'):
            # Retrieving URL used for nginx reverse proxy
            openapi_schema["servers"] = [
                {
                    "url": 'https://' + os.getenv('LETSENCRYPT_HOST'),
                    "description": 'Production Knowledge Collaboratory API',
                    "x-maturity": 'production',
                    "x-location": 'IDS'
                }
            ]

        openapi_schema["info"]["x-translator"] = {
            "component": 'KP',
            "team": "Clinical Data Provider",
            "biolink-version": "1.8.2",
            "infores": 'infores:knowledge-collaboratory',
            "externalDocs": {
                "description": "The values for component and team are restricted according to this external JSON schema. See schema and examples at url",
                "url": "https://github.com/NCATSTranslator/translator_extensions/blob/production/x-translator/",
            },
        }
        openapi_schema["info"]["x-trapi"] = {
            "version": "1.2.0",
            "operations": [
                "lookup",
            ],
            "externalDocs": {
                "description": "The values for version are restricted according to the regex in this external JSON schema. See schema and examples at url",
                "url": "https://github.com/NCATSTranslator/translator_extensions/blob/production/x-trapi/",
            },
        }

        openapi_schema["info"]["contact"] = {
            "name": "Vincent Emonet",
            "email": "vincent.emonet@maastrichtuniversity.nl",
            # "x-id": "vemonet",
            "x-role": "responsible developer",
        }
        openapi_schema["info"]["termsOfService"] = 'https://raw.githubusercontent.com/MaastrichtU-IDS/translator-openpredict/master/LICENSE'
        openapi_schema["info"]["license"] = {
            "name": "MIT license",
            "url": "https://opensource.org/licenses/MIT",
        }
        
        # From fastapi:
        openapi_schema["info"]["x-logo"] = {
            # "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
            "url": "https://raw.githubusercontent.com/MaastrichtU-IDS/dsri-documentation/master/website/static/img/um_logo.png"
        }

        self.openapi_schema = openapi_schema
        return self.openapi_schema


TRAPI_EXAMPLE = {
  "message": {
    "query_graph": {
      "edges": {
        "e01": {
          "object": "n1",
          "predicates": [
            "biolink:treats"
          ],
          "subject": "n0"
        }
      },
      "nodes": {
        "n0": {
          "categories": [
            "biolink:Drug",
            "biolink:ChemicalSubstance"
          ],
          "ids": [
            "DRUGBANK:DB00394",
            "CHEBI:75725"
          ]
        },
        "n1": {
          "categories": [
            "biolink:Disease"
          ]
        }
      }
    }
  },
  "query_options": {
    "n_results": 30
  }
}