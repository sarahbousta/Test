
import unittest
from personnage import Personnage

class TestPersonnage(unittest.TestCase):

    def setUp(self):
        """Initialisation des objets Personnage pour les tests."""
        self.perso = Personnage("Test", 10)
        self.attaquant = Personnage("Attaquant", 10)
        self.cible = Personnage("Cible", 10)

    def test_personnage_est_vivant_quand_points_de_vie_positifs(self):
        """Un personnage doit être considéré comme vivant si ses points de vie sont positifs."""
        self.assertTrue(self.perso.est_vivant())

    def test_personnage_nest_pas_vivant_quand_points_de_vie_nuls(self):
        """Un personnage ne doit pas être considéré comme vivant si ses points de vie tombent à 0."""
        self.perso.hp = 0
        self.assertFalse(self.perso.est_vivant())

    def test_personnage_prendre_degats_diminue_points_de_vie(self):
        """Les points de vie du personnage doivent diminuer de la quantité de dégâts reçus."""
        self.perso.prendre_degats(5)
        self.assertEqual(self.perso.hp, 5)
    
    def test_personnage_attaquer_autre_personnage_inflige_degats(self):
        """Attaquer un autre personnage doit diminuer les points de vie de ce dernier."""
        self.attaquant.attaquer(self.cible, 5)
        self.assertEqual(self.cible.hp, 5)

if __name__ == '__main__':
    unittest.main()
