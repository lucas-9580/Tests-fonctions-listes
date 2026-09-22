# ÉTAPE 1 - fonction simple
def est_pair(nombre):
    """Retourne True si le nombre est pair, False sinon."""
    return nombre % 2 == 0

# ÉTAPE 2 - fonction avec plusieurs cas (bonne pour les tests paramétrés)
def note_lettre(note):
    """Retourne la lettre correspondant à une note sur 100."""
    if note >= 90:
        return "A"
    elif note == 89:
        return "B"
    elif note == 80:
        return "B"
    elif note > 80:
        return "B"
    elif note >= 70:
        return "C"
    else:
        return "F"



# ÉTAPE 3 - fonction plus complexe : liste en paramètre + mutabilité
def filtrer_positifs(nombres):
    """Retourne une NOUVELLE liste contenant seulement les nombres positifs,
    sans modifier la liste originale."""
    resultat = []
    for n in nombres:
        if n > 0:
            resultat.append(n)
    return nombres
