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
"""
eq str
"""

class Fraction:

    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être nul.")
        self.num = num
        self.den = den

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return f"{self.num}/{self.den}"
        
    def __eq__(self, autre_fraction):
        return self.num * autre_fraction.den == self.den * autre_fraction.num

    def multiplier(self, autre_fraction):
        return Fraction(
            self.num * autre_fraction.num,
            self.den * autre_fraction.den
        )


f1 = Fraction(3, 4)
f2 = Fraction(2, 4)
f3 = Fraction(1, 2)
f4 = Fraction(5, 1)

assert str(f1) == "3/4", f"Erreur : str(f1) renvoie '{str(f1)}' au lieu de '3/4'"
assert str(f4) == "5", f"Erreur : str(f4) renvoie '{str(f4)}' au lieu de '5'"

assert (
    f2 == f3
), "Erreur : Fraction(2, 4) et Fraction(1, 2) doivent être égales avec =="

assert not (
    f1 == f2
), "Erreur : Fraction(3, 4) et Fraction(2, 4) ne sont pas égales"

f_prod = f1.multiplier(f2)

assert isinstance(
    f_prod, Fraction
), "Erreur : multiplier doit renvoyer une instance de Fraction"

assert f_prod.num == 6 and f_prod.den == 16, "Erreur dans le calcul du produit"

print("Validé!")






class Utilisateur:

    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.amis = []

    def __str__(self):
        
        return f"@{self.pseudo} ({len(self.amis)} amis)"
        
    def __eq__(self, autre_user):
        return self.pseudo == autre_user.pseudo

    def ajouter_ami(self, nouvel_ami):
        if nouvel_ami not in self.amis and nouvel_ami !=self:
            self.amis.append(nouvel_ami)




# --- Validation Exercice 2 ---
u1 = Utilisateur("Thomas")
u2 = Utilisateur("Alice")
u3 = Utilisateur("Thomas")  # Même pseudo que u1

assert (
    str(u1) == "@Thomas (0 amis)"
), f"Erreur d'affichage : '{str(u1)}' au lieu de '@Thomas (0 amis)'"

assert u1 == u3, "Erreur : deux utilisateurs avec le même pseudo doivent être =="
assert not (u1 == u2), "Erreur : deux pseudos différents ne doivent pas être =="

u1.ajouter_ami(u2)
assert (
    len(u1.amis) == 1
), "Erreur : l'ami n'a pas été ajouté à la liste self.amis"
assert (
    str(u1) == "@Thomas (1 amis)"
), f"Erreur d'affichage après ajout : '{str(u1)}'"

u1.ajouter_ami(u3)  # Même pseudo que u1, ne doit pas être ajouté à nouveau
assert (
    len(u1.amis) == 1
), "Erreur : doublon ajouté dans la liste d'amis via __eq__"

u1.ajouter_ami(u1)  # Tentative de s'ajouter soi-même
assert len(u1.amis) == 1, "Erreur : un utilisateur s'est ajouté lui-même"

print("Validé!")


class Duree:

    def __init__(self, heures, minutes):
        self.heures = heures
        self.minutes = minutes

    def __str__(self):
        if self.heures == 0:
            return f"{self.minutes}min"
        return f"{self.heures}h {self.minutes}min"

    def __eq__(self, autre_duree):
        return (self.heures * 60 + self.minutes) == (
            autre_duree.heures * 60 + autre_duree.minutes
        )

    def additionner(self, autre_duree):
        total_minutes = self.minutes + autre_duree.minutes
        heures = self.heures + autre_duree.heures + total_minutes // 60
        minutes = total_minutes % 60

        return Duree(heures, minutes)




# --- Validation Exercice 3 ---
d1 = Duree(1, 30)
d2 = Duree(0, 90)
d3 = Duree(0, 45)

assert (
    str(d1) == "1h 30min"
), f"Erreur : str(d1) renvoie '{str(d1)}' au lieu de '1h 30min'"
assert str(d3) == "45min", f"Erreur : str(d3) renvoie '{str(d3)}' au lieu de '45min'"

assert d1 == d2, "Erreur : Duree(1, 30) et Duree(0, 90) doivent être =="
assert not (d1 == d3), "Erreur : des durées différentes sont considérées =="

d_somme = d3.additionner(Duree(1, 45))
assert isinstance(
    d_somme, Duree
), "Erreur : additionner doit renvoyer une instance de Duree"
assert (
    d_somme.heures == 2 and d_somme.minutes == 30
), f"Erreur de normalisation : obtenu {d_somme.heures}h {d_somme.minutes}min au lieu de 2h 30min"

print("Validé!")




class Livre:

    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f"{self.titre}, par {self.auteur}"

    def __eq__(self, autre_livre):
                return (
            self.titre.lower() == autre_livre.titre.lower()
            and self.auteur.lower() == autre_livre.auteur.lower()
        )

class Bibliotheque:

    def __init__(self):
        self.livres = []

    def ajouter_livre(self, nouveau_livre):
        if nouveau_livre not in self.livres:
            self.livres.append(nouveau_livre)

# --- Validation Exercice 4 ---
l1 = Livre("1984", "George Orwell")
l2 = Livre("1984", "george orwell")  # Différence de casse
l3 = Livre("Dune", "Frank Herbert")

assert (
    str(l1) == "1984, par George Orwell"
), f"Erreur d'affichage : '{str(l1)}'"
assert (
    l1 == l2
), "Erreur : la comparaison des livres doit être insensible à la casse"
assert not (l1 == l3), "Erreur : deux livres différents sont considérés =="

biblio = Bibliotheque()
biblio.ajouter_livre(l1)
assert len(biblio.livres) == 1, "Erreur lors de l'ajout du livre"

biblio.ajouter_livre(l2)  # Doublon (casse différente)
assert (
    len(biblio.livres) == 1
), "Erreur : un doublon de livre a été ajouté à la bibliothèque"

biblio.ajouter_livre(l3)
assert len(biblio.livres) == 2, "Erreur : le livre l3 aurait dû être ajouté"

print("Validé!")





