# Thesis Knowledge Extraction

## Project Overview

This project investigates how information about dance depicted in visual art can be extracted from unstructured blog texts and converted into RDF knowledge graph data.

The project uses the blog:

https://artanddance.art.blog/

as a case study.

The final goal is to build a pipeline that automatically extracts structured information from art-related texts and represents this information as RDF triples in a knowledge graph.

---

## Research Question

How can prompt engineering be used to automatically extract information about dance depicted in visual art from unstructured blog texts and convert this information into RDF knowledge graph data?

---

## Current Pipeline

Blog Posts
↓
Web Scraper
↓
Text Extraction
↓
Entity Detection
↓
RDF Generator
↓
Knowledge Graph

---

## Repository Structure

artdance-rdf-project/

├── scraper.py

├── collect_posts.py

├── rdf_generator.py

├── ontology.py

├── visualize_graph.py

├── query_test.py

├── ontology.ttl

├── data/

│ ├── posts.json

│ └── artdance.ttl

└── knowledge_graph.html

---

## Implemented Features

- Web scraping of blog posts
- Text extraction
- RDF generation using RDFLib
- Ontology prototype
- Knowledge graph visualization using PyVis
- SPARQL querying

---

## Technologies

- Python
- BeautifulSoup
- RDFLib
- SPARQL
- PyVis

---

## Future Work

- Prompt engineering with Large Language Models
- Automatic entity extraction
- Ontology refinement
- Evaluation against manually annotated data
- Knowledge graph quality assessment

---

## Author

Berat Kirtis

Vrije Universiteit Amsterdam

Artificial Intelligence
