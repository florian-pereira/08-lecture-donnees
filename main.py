"""
Ce programme lit un fichier CSV contenant des listes d'entiers,
puis effectue des opérations simples sur ces listes, comme trouver
le premier, le dernier, le maximum, le minimum, et la somme des
éléments. Il permet également d'accéder à une liste spécifique
par son indice.
"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """
    Lit un fichier et retourne son contenu sous forme de listes.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        # Lire toutes les lignes du fichier
        lines = file.readlines()

    # Transformer chaque ligne en une liste d'entiers
    data = [list(map(int, line.strip().split(';'))) for line in lines]
    return data

def get_list_k(data, k):
    """
    Retourne la k-ième liste dans les données.
    """
    return data[k]

def get_first(lst):
    """
    Retourne le premier élément d'une liste.
    """
    return lst[0]

def get_last(lst):
    """
    Retourne le dernier élément d'une liste.
    """
    return lst[-1]

def get_max(lst):
    """
    Retourne le plus grand élément d'une liste.
    """
    return max(lst)

def get_min(lst):
    """
    Retourne le plus petit élément d'une liste.
    """
    return min(lst)

def get_sum(lst):
    """
    Retourne la somme des éléments d'une liste.
    """
    return sum(lst)

#### Fonction principale

def main():
    """
    Point d'entrée du programme.
    Lit un fichier et teste les différentes fonctions sur les listes.
    """
    # Lire les données depuis le fichier 'listes.csv'
    data = read_data(FILENAME)
    print("Données lues du fichier :", data)
    first_list = data[0]
    print("Première liste :", first_list)
    print("Premier élément :", get_first(first_list))
    print("Dernier élément :", get_last(first_list))
    print("Maximum de la liste :", get_max(first_list))
    print("Minimum de la liste :", get_min(first_list))
    print("Somme des éléments de la liste :", get_sum(first_list))
    k = 1
    print(f"Liste à l'indice {k} :", get_list_k(data, k))

if __name__ == "__main__":
    main()
