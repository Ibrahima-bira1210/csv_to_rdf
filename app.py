from flask import Flask, request, Response
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDFS
import csv
from flask_restx import Api, Resource, fields
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
api = Api(app, version='1.0', title='CSV to RDF API', description='Convert CSV to RDF')

csv_file = api.parser()
csv_file.add_argument('file', location='files', type=FileStorage, required=True)


@app.route('/csv-to-rdf', methods=['POST'])
def convert_csv_to_rdf():
    # Namespaces
    ns = Namespace("http://example.com/")
    # Recuperation des fichiers uploadés
    csv_file = request.files['csvFile']
    rdf_file = request.files['rdfFile']

    # Création d'un graphe RDF
    g = Graph()

    # Chargement du fichier RDFS/XML
    g.parse(rdf_file, format='xml')

    # Ouverture du fichier CSV
    csv_data = csv_file.read().decode('utf-8')
    reader = csv.DictReader(csv_data.splitlines(), delimiter=',')
    for row in reader:
        # Création d'une ressource pour chaque ligne
        resource = URIRef(ns[row["id"]])
        g.add((resource, RDFS.Resource, ns.Resource))
        # Ajout des propriétés à partir des colonnes
        for prop, value in row.items():
            if prop != "id":
                g.add((resource, ns[prop], Literal(value)))

    # Envoi du fichier RDFS/XML modifié
    rdf_data = g.serialize(format='xml')
    response = Response(rdf_data, content_type='application/rdf+xml')
    response.headers["Content-Disposition"] = "attachment; filename=data.rdf"
    return response


if __name__ == '__main__':
    app.run()
