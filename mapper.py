# Initialiser le dictionnaire principal

def mapper():
    dict_principal = {}

    # Dictionaire ClasseFichier
    dict_classFichier = {}
    while True:
        sub_key = input("Entrez le nom de la clé ou mettez fin "
                        "quand vous avez termine: ")
        if sub_key == "fin":
            break
        sub_value = input("Entrez la valeur de la clé: ")
        dict_classFichier[sub_key] = sub_value

    # Dictionaire ClassColone
    dict_classColone = {}
    while True:
        sub_key1 = input("Entrez le nom de la clé ou "
                         "mettez fin quand vous avez termine: ")
        if sub_key1 == "fin":
            break
        sub_value1 = input("Entrez la valeur de la clé: ")
        dict_classFichier[sub_key1] = sub_value1

    # Dictionaire PropColone
    dict_PropColone = {}
    while True:
        sub_key2 = input("Entrez le nom de la clé ou "
                         "mettez fin quand vous avez termine: ")
        if sub_key2 == "fin":
            break
        sub_value2 = input("Entrez la valeur de la clé: ")
        dict_classFichier[sub_key2] = sub_value2

    dict_principal['classFichier'] = dict_classFichier
    dict_principal['classColone'] = dict_classColone
    dict_principal['PropColone'] = dict_PropColone
    return dict_principal
