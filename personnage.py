class Personnage:
    def __init__(self, nom, hp):
        self.nom = nom
        self.hp = hp

    def est_vivant(self):
        return self.hp > 0
    
def prendre_degats(self, degats):
    self.hp -= degats

def attaquer(self, cible, degats):
    if self.est_vivant():
        cible.prendre_degats(degats)

