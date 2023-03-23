import csv
from rdflib import Graph, Literal, URIRef

g = Graph()
g.parse("eudataset.owl", format="xml")

subjects_predicates = {
    'http://www.semanticweb.org/ontologies/Energy-produced': {
        'http://www.semanticweb.org/ontologies/country': 'country',
        'http://www.semanticweb.org/ontologies/year': 'year',
        'http://www.semanticweb.org/ontologies/type-energy': 'energy_type',
        'http://www.semanticweb.org/ontologies/energydatasetEU#produced': 'produced_value'
    },
    'http://www.semanticweb.org/ontologies/Energy-consumed': {
        'http://www.semanticweb.org/ontologies/country': 'country',
        'http://www.semanticweb.org/ontologies/year': 'year',
        'http://www.semanticweb.org/ontologies/type-energy': 'energy_type',
        'http://www.semanticweb.org/ontologies/energydatasetEU#consumed': 'consumed_value',
    },
    'http://www.semanticweb.org/ontologies/energydatasetEU#GHG_emission': {
        'http://www.semanticweb.org/ontologies/country': 'country',
        'http://www.semanticweb.org/ontologies/year': 'year',
        'http://www.semanticweb.org/ontologies/sector': 'sector',
        'http://www.semanticweb.org/ontologies/energydatasetEU#GHG_emission_rate': 'GHG_value'

    },
    'http://www.semanticweb.org/ontologies/CO2_emission': {
        'http://www.semanticweb.org/ontologies/country': 'country',
        'http://www.semanticweb.org/ontologies/year': 'year',
        'http://www.semanticweb.org/ontologies/sector': 'sector',
        'http://www.semanticweb.org/ontologies/energydatasetEU#CO2_emission_rate': 'C02_value'
    }
}

# Chargement du fichier CSV
with open("eudataset.csv") as f:
    # Parcours des lignes du fichier CSV
    reader = csv.DictReader(f)
    header = next(reader)
    for row in reader:
        # Création des triplets RDF
        for key, value in subjects_predicates.items():
            subject = URIRef(key)
            for k, v in value.items():
                predicate = URIRef(k)
                objet = Literal(row[v])
                g.add((subject, predicate, objet))

# Enregistrement du dataset RDF
g.serialize("dataset_energy.rdf", format="xml")

