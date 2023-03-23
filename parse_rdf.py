import rdflib


def rdf_parser(filename):
    # Chargement de l'ontologie
    g = rdflib.Graph()
    g.parse(filename, format="xml")

    # Recuperation des classes
    classes = set()
    for s, p, o in g:
        if p == rdflib.RDF.type and o == rdflib.OWL.Class:
            classes.add(s)

    # Recuperation des propriétés de données
    data_properties = set()
    for s, p, o in g:
        if p == rdflib.RDF.type and o == rdflib.OWL.DatatypeProperty:
            data_properties.add(s)

    # Recuperation des propriétés
    object_properties = set()
    for s, p, o in g:
        if p == rdflib.RDF.type and o == rdflib.OWL.ObjectProperty:
            object_properties.add(s)

    # Affichage des resultants
    print("Classes :")
    for c in classes:
        print(" - " + str(c))

    print("Propriétés de données :")
    for dp in data_properties:
        print(" - " + str(dp))

    print("Propriétés :")
    for op in object_properties:
        print(" - " + str(op))

