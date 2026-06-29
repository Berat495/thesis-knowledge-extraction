# Ontology-Guided Knowledge Graph Construction from Art and Dance Blog Posts

## Overview

This repository contains the implementation developed for my Bachelor's thesis at Vrije Universiteit Amsterdam.

The project presents a complete pipeline for transforming unstructured cultural heritage blog posts into RDF knowledge graphs using ontology-guided prompt engineering.

The pipeline consists of:

- Web scraping
- Information extraction using Large Language Models
- Ontology-guided prompting
- RDF generation using RDFLib
- Knowledge graph construction
- Knowledge graph visualisation

---

## Repository Structure

```
data/
    posts.json
    artdance.ttl

experiments/
    Prompt A
    Prompt B
    Prompt C

collect_posts.py
create_rdf.py
ontology.py
ontology.ttl
rdf_generator.py
query_test.py
visualize_graph.py
README.md
requirements.txt
```

---

## Pipeline

1. Collect blog posts
2. Extract entities using prompt engineering
3. Map extracted entities to ontology classes
4. Generate RDF triples
5. Export Turtle (.ttl)
6. Visualise the RDF graph

---

## Technologies

- Python
- RDFLib
- BeautifulSoup
- PyVis
- NetworkX
- OpenAI API

---

## Thesis

Bachelor Thesis

Vrije Universiteit Amsterdam

2026
