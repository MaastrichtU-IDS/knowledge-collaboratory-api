FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
## Gunicorn image: https://github.com/tiangolo/uvicorn-gunicorn-docker/tree/master/docker-images

LABEL org.opencontainers.image.source="https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api"

## Change the current user to root and the working directory to /app
USER root
WORKDIR /app

# Install NodeJS to try out the Comunica SPARQL package
# RUN apt-get update && \
#     apt-get install -y nodejs curl wget vim
# RUN curl -L https://www.npmjs.com/install.sh | sh
# RUN npm install -g @comunica/actor-init-sparql


# Avoid to reinstall packages when no changes to requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then pip install pytest ; fi"

## Copy the source code (in the same folder as the Dockerfile)
COPY . .

## Gunicorn config
ENV MODULE_NAME=src.main
ENV VARIABLE_NAME=app
ENV PORT=8808

RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then pip install -e . ; else pip install . ; fi"

EXPOSE 8808

# ENTRYPOINT ["uvicorn", "openpredict.main:app",  "--host", "0.0.0.0", "--port", "8808"]
# ENTRYPOINT [ "gunicorn", "-w", "8", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8808", "openpredict.main:app"]

# ENTRYPOINT [ "python3", "src/api.py" ]
