from rdflib import Graph, URIRef
from pyvis.network import Network

g = Graph()
g.parse("data/artdance.ttl", format="turtle")

net = Network(
    height="900px",
    width="100%",
    bgcolor="#ffffff",
    font_color="black",
    directed=True,
    notebook=False
)

allowed_relations = {
    "mentionsArtist",
    "mentionsArtwork",
    "belongsToCentury",
    "hasTheme"
}

for s, p, o in g:
    if not isinstance(s, URIRef):
        continue

    if not isinstance(o, URIRef):
        continue

    subject = str(s).split("/")[-1]
    predicate = str(p).split("/")[-1]
    obj = str(o).split("/")[-1]

    if predicate not in allowed_relations:
        continue

    net.add_node(subject, label=subject)
    net.add_node(obj, label=obj)
    net.add_edge(subject, obj, label=predicate)

net.write_html("knowledge_graph.html", notebook=False)

print("Knowledge graph opgeslagen als knowledge_graph.html")