import pytest
from ex2_pratique import est_pair, note_lettre, filtrer_positifs

# ================= ÉTAPE 1 : tests SANS paramètres =================

def test_est_pair_nombre_pair():
    assert est_pair(4) == True
def test_est_pair_nombre_impair():
    # TODO : tester un nombre impair
    assert est_pair(3) == False

# TODO (étudiant) : ajouter un test pour 0
def test_est_paire_nombre_pare():
    assert est_pair(0) == True

# ================= ÉTAPE 2 : tests AVEC paramètres =================

@pytest.mark.parametrize("note, attendu", [
    (95, "A"),
    (89, "B"),
    (80, "B"),
    (70, "C"),
    (50, "F"),
    # TODO (étudiant) : ajouter un cas pour la note 80 -> "B"

    # TODO (étudiant) : ajouter un cas pour la note 89 -> "B"

])
def test_note_lettre(note, attendu):
    assert note_lettre(note) == attendu


# TODO : refait les tess de la fonction est_pair sous forme de test paramétré
@pytest.mark.parametrize("nombre, attendu", [
    (95, False),
    (89, False),
    (80, True),
    (70, True),
    (50, True),




])
def test_est_pair_nombres(nombre, attendu):
    assert est_pair(nombre) == attendu


# ================= ÉTAPE 3 : fonction plus complexe (liste) =================

def test_filtrer_positifs_retour():
    nombres = [-3, 5, -1, 8, 0]
    resultat = filtrer_positifs(nombres)
    assert resultat == [5, 8]


# TODO (étudiant) : ajouter un test qui vérifie que la liste ORIGINALE
# (nombres) n'a PAS été modifiée par filtrer_positifs (elle doit rester
# [-3, 5, -1, 8, 0]).


# TODO (étudiant) : ajouter un test_filtrer_positifs_type() qui vérifie
# que le résultat est bien de type list.
