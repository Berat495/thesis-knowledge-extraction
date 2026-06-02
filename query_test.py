from rdflib import Graph

g = Graph()

g.parse("data/artdance.ttl", format="turtle")

query = """
PREFIX ex: <http://example.org/artdance/>

SELECT ?post ?artist
WHERE {
    ?post ex:mentionsArtist ?artist .
}
"""

for row in g.query(query):
    print(row)