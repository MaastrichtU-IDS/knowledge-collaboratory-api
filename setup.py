from setuptools import setup, find_packages

setup(
    name='Knowledge Collaboratory API',
    version='0.1.0',
    url='https://github.com/MaastrichtU-IDS/knowledge-collaboratory-api.git',
    author='Vincent Emonet',
    author_email='vincent.emonet@gmail.com',
    description='Knowledge Collaboratory API to access RDF Nanopublications',
    packages=find_packages(),
    install_requires=open("requirements.txt", "r").readlines(),
)