def calculer_stats(nombres):
    """Retourne un tuple (minimum, maximum, moyenne) d'une liste de nombres."""
    minimum = min(nombres)
    maximum = max(nombres)
    moyenne = sum(nombres) / len(nombres)
    return (minimum, maximum, moyenne)

def ajouter_element(liste, element):
    """Ajoute un élément à la liste et retourne la liste modifiée et ordonnée."""
    liste.append(element)
    return sorted(liste)


def calculer_moyenne_sans_liste(nb1, nb2, nb3):
    """Retourne la moyenne de 3 nombres."""
    moyenne = nb1 + nb2 + nb3 / 3
    return moyenne