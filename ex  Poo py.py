class Chronometre:
    def __init__(self):
        self.time = 0
    
    def tic(self):
        self.time = self.time + 1
    
    def reset(self):
        self.time = 0
chrono = Chronometre()

print(chrono.time) 

chrono.tic()
print(chrono.time) 

chrono.reset()
print(chrono.time) 
class CompteBancaire:
    def __init__(self, titulaire, solde_initial):
        self.solde = solde_initial
        self.titulaire = titulaire

    def deposer(self, montant):
        self.solde = self.solde + montant

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde = self.solde - montant
        else:
            print("Solde insuffisant")


compte = CompteBancaire("Alice", 100)

print(compte.titulaire)
print(compte.solde)

compte.deposer(50)
print(compte.solde)

compte.retirer(151)
print(compte.solde)

class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def est_carre(self):
        return self.largeur == self.hauteur


rectangle = Rectangle(5, 10)

print(rectangle.aire())
print(rectangle.est_carre())

