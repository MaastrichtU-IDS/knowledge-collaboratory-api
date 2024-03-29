[![Test production API](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions/workflows/run-tests-prod.yml/badge.svg)](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions/workflows/run-tests-prod.yml)

Install the required dependency to run tests:

```bash
pip install pytest
```

## Manual tests

Use the [`docs/openpredict-examples.ipynb`](https://github.com/MaastrichtU-IDS/translator-openpredict/blob/master/docs/openpredict-examples.ipynb) Jupyter notebook to manually try queries against the OpenPredict API.

## Integration tests

Integration tests are run automatically by a [GitHub Action workflow](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions?query=workflow%3A%22Run+tests%22) everyday at 01:00am GMT+1 on the OpenPredict production API.

Tests consist in POST `/query` TRAPI operations by requesting Drug - Disease associations

We test for an expected number of results and a few specific results.

To run the tests of the OpenPredict production API locally:

```bash
docker-compose -f docker-compose.test.yml up --force-recreate
```

Or while the API is already running with docker-compose:

```bash
docker-compose exec api pytest tests/integration/test_trapi.py::test_post_trapi -s
```

