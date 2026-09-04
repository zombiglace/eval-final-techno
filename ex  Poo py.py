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
        self.solde = self.solde - montant

compte = CompteBancaire("Alice", 100)

print(compte.titulaire)
print(compte.solde)
compte.deposer(50)
print(compte.solde)

compte.retirer(30)
print(compte.solde) 
