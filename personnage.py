class Personnage:
    def __init__(self, nom, hp):
        self.nom = nom
        self.hp = hp

    def est_vivant(self):
        return self.hp > 0

    def prendre_degats(self, degats):
        """Diminue les points de vie du personnage selon les dégâts reçus."""
        self.hp -= degats

    def attaquer(self, cible, degats):
        """Permet au personnage d'attaquer une cible et de lui infliger des dégâts."""
        if self.est_vivant():
            cible.prendre_degats(degats)
