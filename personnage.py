class Personnage:
    def __init__(self, nom, hp):
        self.nom = nom
        self.hp = hp

    def est_vivant(self):
        return self.hp > 0

   
