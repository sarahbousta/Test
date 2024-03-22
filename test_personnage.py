from personnage import Personnage


def test_est_vivant(self):
    perso = Personnage("Test", 10)
    self.assertTrue(perso.est_vivant())
    perso.hp = 0
    self.assertFalse(perso.est_vivant())
