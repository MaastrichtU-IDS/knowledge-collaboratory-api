[![Test production API](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/workflows/Test%20production%20API/badge.svg)](https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api/actions?query=workflow%3A%22Test+production+API%22)

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
pytest tests/integration
```
