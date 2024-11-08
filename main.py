# main.py
"""
author = klaus.kapllani@esiee.fr
"""

FILENAME = "listes.csv"

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []

    with open(filename, 'r', encoding="utf-8") as f:
        l = [[int(v) for v in ligne.strip().split(';')] for ligne in f.readlines()]
    return l

def get_list_k(data, k):
    """retourne la k-ème liste de data

    Args:
        data (list): une liste de listes

    Returns:
        list: la k-ème liste
    """
    return data[k]

def get_first(l):
    """retourne le premier élément d'une liste

    Args:
        l (list): une liste

    Returns:
        int : le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """retourne le dernier élément d'une liste

    Args:
        l (list): une liste

    Returns:
        int : le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """retourne le maximum liste

    Args:
        l (list): une liste

    Returns:
        int : le maximum de la liste
    """
    return max(l)

def get_min(l):
    """retourne le minimum d'une liste

    Args:
        l (list): une liste

    Returns:
        int : le minimum de la liste
    """
    return min(l)

def get_sum(l):
    """retourne la somme d'une liste

    Args:
        l (list): une liste

    Returns:
        int : la somme de la liste
    """
    return sum(l)

def main():
    """
    Fonction principale qui lit le fichier <FILENAME>,
    affiche les éléments de la k-eme liste, puis son premier élément,
    son dernier élément, son élément max, son élément min et enfin la somme de celle-ci.

    Returns :
        rien
    """
    data = read_data(FILENAME)
    k = 37
    print(k, get_list_k(data, 37))
    print("Le premier élément de la ", k, "ème liste est :", get_first(get_list_k(data, 37)))
    print("Le dernier élément de la ", k, "ème liste est :", get_last(get_list_k(data, 37)))
    print("L'élément max de la ", k, "ème liste est :", get_max(get_list_k(data, 37)))
    print("L'élément min de la ", k, "ème liste est :", get_min(get_list_k(data, 37)))
    print("La somme de la ", k, "ème liste est :", get_sum(get_list_k(data, 37)))

if __name__ == "__main__":
    main()
