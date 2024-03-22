from personnage import Personnage


def test_est_vivant(self):
    perso = Personnage("Test", 10)
    self.assertTrue(perso.est_vivant())
    perso.hp = 0
    self.assertFalse(perso.est_vivant())
    
def test_prendre_degats(self):
    perso = Personnage("Test", 10)
    perso.prendre_degats(5)
    self.assertEqual(perso.hp, 5)
