#!/bin/bash

#git add .
#git commit -m "Improvements"
#git push

ssh ids2 'cd /data/deploy-services/knowledge-collaboratory-api ; git pull ; docker-compose -f docker-compose.prod.yml build ; docker-compose -f docker-compose.prod.yml down ; docker-compose -f docker-compose.prod.yml up -d --force-recreate'

## No cache:
# ssh ids2 'cd /data/deploy-services/knowledge-collaboratory-api ; git pull ; docker-compose down ; docker-compose build --no-cache ; docker-compose up -d'