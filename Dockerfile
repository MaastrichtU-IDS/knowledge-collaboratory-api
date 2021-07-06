FROM python:3.7 
# Starts from the official docker image for python with version 3.7

# Install NodeJS to try out the Comunica SPARQL package
RUN apt-get update
RUN apt-get install nodejs -y
RUN curl -L https://www.npmjs.com/install.sh | sh
RUN npm install -g @comunica/actor-init-sparql

# Install pip dependencies
ADD requirements.txt .
RUN pip install -r requirements.txt
# RUN pip install --install-option="--extras-require=swagger-ui" git+https://github.com/vemonet/connexion@fix-servers-overwrite

# Copy the source code from the current folder to the container (in the current working directory)
COPY . .

# Install the pip packages
RUN pip install -r requirements.txt

# Indicate the image will be exposing this port (optional)
EXPOSE 8808

# The command that will be run when the container is started (here it starts the API on port 8808)
ENTRYPOINT [ "python3", "src/api.py" ]
