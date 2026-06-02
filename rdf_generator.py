import json
import re
from rdflib import Graph, Namespace, Literal, RDF
from rdflib.namespace import DCTERMS, RDFS

EX = Namespace("http://example.org/artdance/")

graph = Graph()

graph.bind("ex", EX)
graph.bind("dc", DCTERMS)
graph.bind("rdfs", RDFS)

graph.add((EX.BlogPost, RDF.type, RDFS.Class))
graph.add((EX.Artist, RDF.type, RDFS.Class))
graph.add((EX.Century, RDF.type, RDFS.Class))
graph.add((EX.Theme, RDF.type, RDFS.Class))
graph.add((EX.Artwork, RDF.type, RDFS.Class))

graph.add((EX.hasTheme, RDF.type, RDF.Property))
graph.add((EX.mentionsArtist, RDF.type, RDF.Property))
graph.add((EX.belongsToCentury, RDF.type, RDF.Property))
graph.add((EX.mentionsArtwork, RDF.type, RDF.Property))
graph.add((EX.sourceUrl, RDF.type, RDF.Property))
graph.add((EX.content, RDF.type, RDF.Property))

artist_names = {
    "David Teniers the Younger",
    "Pieter Bruegel the Elder",
    "Pieter Brueghel the Younger",
    "Jan Brueghel the Elder",
    "Pieter van der Heyden",
    "Pieter Jansz. Quast",
    "Pieter Codde",
    "Adriaen Brouwer",
    "Adriaen van Ostade",
    "Pieter Nolpe",
    "Salomon Savery",
    "Piet Mondrian",
    "Dick Bruna",
    "Willy Sluiter",
    "Isaac Israels",
    "George Hendrik Breitner",
    "Bart van der Leck",
    "Willem de Zwart",
    "Piet van der Hem",
    "Johan Dijkstra",
    "Rie Cramer",
    "Lucas van Valckenborch",
    "Abel Grimmer",
    "Jacob Grimmer",
    "David Vinckboons",
    "Dirck Hals",
    "Frans Pourbus the Younger",
    "Hieronymus Francken the Younger",
    "Chris van den Hoef",
    "Jan Bleys",
    "Johan Braakensiek",
    "Henri Braakensiek",
    "Jan Josef Horemans the Elder",
    "Matthijs Röling",
    "Sebastiaen Vrancx",
    "Stallman Pim",
    "Willem Duyster",
    "Adriaen Pietersz. van de Venne"
}

artwork_titles = {
    "Peasant Wedding Dance",
    "Village Festival and Feast",
    "Country Celebration",
    "Peasant Wedding",
    "The Wedding Banquet",
    "Spring",
    "An Allegory of Spring",
    "Spring Landscape",
    "Delft Tango 5",
    "Children dancing to the street musician",
    "Barrel Organ in the Jordaan, Amsterdam",
    "Dancing by the Street Organ",
    "Dancing near the Organ",
    "Kermis in Volendam",
    "Kermis in Spaander",
    "Dancing Fisherman",
    "Two Dancing Amsterdam Girls"
}

def make_slug(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")

def is_century(tag):
    return "century" in tag.lower()

with open("data/posts.json", "r", encoding="utf-8") as file:
    posts = json.load(file)

for post in posts:
    post_uri = EX[make_slug(post["title"])]

    graph.add((post_uri, RDF.type, EX.BlogPost))
    graph.add((post_uri, DCTERMS.title, Literal(post["title"])))
    graph.add((post_uri, DCTERMS.date, Literal(post["date"])))
    graph.add((post_uri, EX.sourceUrl, Literal(post["url"])))
    graph.add((post_uri, EX.content, Literal(post["content"])))

    for artwork in artwork_titles:
        if artwork.lower() in post["content"].lower():
            artwork_uri = EX[make_slug(artwork)]

            graph.add((artwork_uri, RDF.type, EX.Artwork))
            graph.add((artwork_uri, RDFS.label, Literal(artwork)))
            graph.add((post_uri, EX.mentionsArtwork, artwork_uri))

    for tag in post["tags"]:
        tag_uri = EX[make_slug(tag)]

        if tag in artist_names:
            graph.add((tag_uri, RDF.type, EX.Artist))
            graph.add((tag_uri, RDFS.label, Literal(tag)))
            graph.add((post_uri, EX.mentionsArtist, tag_uri))

        elif is_century(tag):
            graph.add((tag_uri, RDF.type, EX.Century))
            graph.add((tag_uri, RDFS.label, Literal(tag)))
            graph.add((post_uri, EX.belongsToCentury, tag_uri))

        else:
            graph.add((tag_uri, RDF.type, EX.Theme))
            graph.add((tag_uri, RDFS.label, Literal(tag)))
            graph.add((post_uri, EX.hasTheme, tag_uri))

graph.serialize("data/artdance.ttl", format="turtle")

print("Verbeterde RDF met artworks gemaakt: data/artdance.ttl")