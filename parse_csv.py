import csv


def csv_parser(file_name):
    # Chargement du fichier CSV
    with open(file_name) as f:
        reader = csv.reader(f)
        header = next(reader)

    # Affichage de l'en-tête
    print("En-tête :")
    for h in header:
        print(" - " + h)
