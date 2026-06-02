# Dance Images RDF Project

## Goal
Transform blog data from artanddance.art.blog into a semantic RDF knowledge graph.

## Data Source
https://artanddance.art.blog/

## Pipeline

1. Scrape blog posts
2. Extract title, date, content and tags
3. Store data in JSON
4. Map data to ontology classes
5. Generate RDF triples
6. Query RDF using SPARQL

## Ontology

Classes:
- BlogPost
- Artist
- Century
- Theme

Properties:
- mentionsArtist
- belongsToCentury
- hasTheme
- content

## Example Triple

BlogPost:
David Teniers — The bride who never dances

mentionsArtist:
David Teniers the Younger

belongsToCentury:
17th century