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

class Article:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class Pokemon:
    def __init__(self, nom, pv, atk):
        self.nom = nom
        self.pv = pv
        self.atk = atk

    def attaquer(self, adv):
        adv.pv = adv.pv - self.atk
pikachu = Pokemon("Pikachu", 100, 20)
salameche = Pokemon("Salamèche", 80, 15)

pikachu.attaquer(salameche)

print(salameche.pv)



class Panier:
    def __init__(self):
        self.contenu = []

    def ajouter(self, un_article):
        self.contenu.append(un_article)

    def calculer_total(self):
        total = 0
        for article in self.contenu:
            total += article.prix
        return total

a1 = Article("Clavier", 30.0)
a2 = Article("Souris", 20.0)

panier = Panier()
panier.ajouter(a1)
panier.ajouter(a2)


class Mediatheque:
    def __init__(self):
        self.liste_livres = []

    def ajouter_livre(self, un_livre):
        self.liste_livres.append(un_livre)

    def rechercher_par_auteur(self, nom_auteur):
        resultats = []
        
        for livre in self.liste_livres:
            if livre.auteur == nom_auteur:
                resultats.append(livre)
        
        return resultats

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur



livre1 = Livre("Harry Potter", "J.K. Rowling")
livre2 = Livre("1984", "George Orwell")
livre3 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")
livre4 = Livre("Harry Potter 2", "J.K. Rowling")


mediatheque = Mediatheque()



mediatheque.ajouter_livre(livre1)
mediatheque.ajouter_livre(livre2)
mediatheque.ajouter_livre(livre3)
mediatheque.ajouter_livre(livre4)

print("Nombre de livres :", len(mediatheque.liste_livres))


resultats = mediatheque.rechercher_par_auteur("J.K. Rowling")

print("Livres de J.K. Rowling :")

for livre in resultats:
    print("-", livre.titre)


resultats = mediatheque.rechercher_par_auteur("Victor Hugo")

print("Livres de Victor Hugo :", resultats)
print(panier.calculer_total())
