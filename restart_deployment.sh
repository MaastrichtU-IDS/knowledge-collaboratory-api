#!/bin/bash

#git add .
#git commit -m "Improvements"
#git push

ssh ids2 'cd /data/deploy-ids-tests/knowledge-collaboratory-api ; git pull ; docker-compose down ; docker-compose build ; docker-compose up -d'

## No cache:
# ssh ids2 'cd /data/deploy-ids-tests/knowledge-collaboratory-api ; git pull ; docker-compose down ; docker-compose build --no-cache ; docker-compose up -d'