import pytest
from ex1_demo import *

def test_calculer_stats_valeurs():
    liste = [1, 2, 3, 4, 5]
    resultat = calculer_stats(liste)
    assert resultat == (1, 5, 3.0)
    assert isinstance(resultat, tuple)

def test_ajouter_element_retour():
    notes = [10, 12]
    resultat = ajouter_element(notes, 11)
    assert resultat == [10, 11, 12]

def test_ajouter_element_mutabilite():
    # Une liste passée en paramètre peut être modifiée par la fonction
    # (passage par affectation) : la liste ORIGINALE change aussi.
    notes = [10, 12]
    ajouter_element(notes, 7)
    assert notes == [7, 10, 12]

# Tests avec plan de tests paramétré :
@pytest.mark.parametrize('n1, n2, n3, moyenne_attendue', [
    (4,5,6,5),
    (6,7,8,7),
    (0,0,0,0),
    (1,1,1,1)
])
def test_calculer_moyenne_sans_liste(n1, n2, n3, moyenne_attendue):
    assert calculer_moyenne_sans_liste(n1, n2, n3) == moyenne_attendue

@pytest.mark.parametrize("nombres, attendu", [
    ([1, 2, 3, 4, 5], (1, 5, 3.0)),
    ([10, 20, 30], (10, 30, 20.0)),
    ([7], (7, 7, 7.0)),
])
def test_calculer_stats_parametrize(nombres, attendu):
    assert calculer_stats(nombres) == attendu
