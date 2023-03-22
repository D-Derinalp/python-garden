# Garden Path Sentences

This is a Python project that imports Spacy and ready to run on Docker. 
It has sensible defaults for security.

## Table of Contents
1. Requirements
2. Setup
3. What does the project do?
4. Contribute

## 1. Requirements
- Python 3.7 or later versions
- Docker

## 2. Setup

Firstly install [Docker](https://docs.docker.com/get-docker/) on your computer.
Now launch pycharm and configure a project on this working directory.
All following commands must be run only once at project installation.

The first clone of the repository:

```bash
$ git clone https://github.com/D-derinalp/python-garden.git
$ cd python-garden
```

Then install the all dependencies:
```bash
$ pip install -r requirements.txt
```

### Docker Image
Run the following command to create docker image:

```bash
docker build -t python-garden .
```

To create docker container you should run the image with following command:

```bash
docker run python-garden
```

## 3. What does the project do?

This project has a list of garden path sentences. It categorises each sentence by importing Spacy.
It tokenises and tags each sentence in the list and performs entity recognition.
It shows explanation of some entities (NROP, GPE).

## 4. Contribute

Contributions are always welcome! 