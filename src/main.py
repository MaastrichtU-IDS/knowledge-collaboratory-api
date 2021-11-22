from fastapi import FastAPI, Body, Request, Response
from fastapi.responses import JSONResponse, RedirectResponse
from reasoner_pydantic import Query, Message
# from typing import Optional, Dict

from src.reasonerapi_parser import reasonerapi_to_sparql, get_metakg_from_nanopubs
from src.openapi import TRAPI, TRAPI_EXAMPLE


# Other TRAPI project using FastAPI: https://github.com/NCATS-Tangerine/icees-api/blob/master/icees_api/trapi.py
app = TRAPI()


@app.get("/meta_knowledge_graph", name="Get the meta knowledge graph",
    description="Get the meta knowledge graph",
    response_model=dict,
    tags=["trapi"],
)
def get_meta_knowledge_graph() -> dict:
    """Get predicates and entities provided by the API
    
    :return: JSON with biolink entities
    """
    return get_metakg_from_nanopubs()


@app.post("/query", name="TRAPI query",
    description="""Execute a Translator Reasoner API query against the Knowledge Collaboratory
""",
    response_model=Query,
    tags=["reasoner"],
)
def post_reasoner_query(
        request_body: Query = Body(..., example=TRAPI_EXAMPLE)
    ) -> Query:
    """Get associations for a given ReasonerAPI query.
    
    :param request_body: The ReasonerStdAPI query in JSON
    :return: Results as a ReasonerStdAPI Message
    """
    query_graph = request_body.message.query_graph.dict(exclude_none=True)
    print(query_graph)
    if len(query_graph["edges"]) == 0:
        return ({"status": 400, "title": "Bad Request", "detail": "No edges", "type": "about:blank" }, 400)
    if len(query_graph["edges"]) > 1:
        return ({"status": 501, "title": "Not Implemented", "detail": "Multi-edges queries not yet implemented", "type": "about:blank" }, 501)

    reasonerapi_response = reasonerapi_to_sparql(request_body.dict(exclude_none=True))
    # reasonerapi_response = request_body

    return reasonerapi_response or ('Not found', 404)



@app.get("/", include_in_schema=False)
def redirect_root_to_docs():
    """Redirect the route / to /docs"""
    return RedirectResponse(url='/docs')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8808)
