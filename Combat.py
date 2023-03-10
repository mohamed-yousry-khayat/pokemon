from random import *
from Pokemon import *

class Combat:
    def __init__(self):
        # On instancie les attributs de la classe à des valeurs initiales
        self.round = 0
        self.PlayerActif = 0 # 0 = Joueur, 1 = Ordinateur
        self.QuiAtt = 0  # Qui attaque
        self.QuiDef = 1  # Qui défend
    # Méthode qui définit aléatoirement un joueur qui commence
    def PlayerStart(self):
        NombreJoueur = [0, 1]  # 0 = Joueur, 1 = Ordinateur
        self.PlayerActif = random.choice(NombreJoueur)
    # Méthode qui switch d'un joueur à l'autre l'attribut PlayerActif
    def ChangePlayerActif(self) :
        if self.PlayerActif == 0:
            self.PlayerActif = 1
        elif self.PlayerActif == 1:
            self.PlayerActif = 0
        return self.PlayerActif
    # Méthode d'attaque, return les dégats générés
    def Attaque(self,PointAttaquant,BonusAttaquant):
        return (random.randint(1,PointAttaquant)) * BonusAttaquant

print("Bienvenue Pokémon ! Bon jeu !")

pokemon = int(input("Choisissez votre pokémon : tapez 0 pour Ponyta (Feu), 1 pour Carapuce (Eau), 2 pour Racaillou (Terre), 3 pour Evoli (Normal) : "))
# On crée une instance de Pokémon qui sera le Joueur
Pok = Pokemon()
# On affecte le pokémon choisi
if pokemon == 0:
    Pok.ChoixPlayerpokemon("Ponyta")
elif pokemon == 1:
    Pok.ChoixPlayerpokemon("Carapuce")
elif pokemon == 2:
    Pok.ChoixPlayerpokemon("Racaillou")
elif pokemon == 3:
    Pok.ChoixPlayerpokemon("Evoli")
else :
    input("Invalide, saississez un pokémon entre 0 et 3")
    exit()
# On crée une instance de pokémon adverse (l'ordinateur)
PokOrdi = Pokemon()
# On choisit aléatoirement un Pokémon adverse
PokOrdi.ChoixRandomPlayerOrdi()

print("Votre pokémon est :", Pok.nomdupokemon, "avec", Pok.pointsdevie, "points de vie.", "de niveau", Pok.niveau)
print("Et votre adversaire est :", PokOrdi.nomdupokemon, "avec", PokOrdi.pointsdevie, "points de vie", "de niveau", Pok.niveau)

# On calcule et met à jour les attributs des bonus de chaque joueur
Pok.AvantageFaiblesse(Pok.typespokemon, PokOrdi.typespokemon)
PokOrdi.AvantageFaiblesse(PokOrdi.typespokemon, Pok.typespokemon)

Jeux = Combat()
# On choisit un joueur au hasard pour commencer
Jeux.PlayerStart()
# On affiche le joueur qui commence
if Jeux.PlayerActif == 0:
    print(Pok.nomdupokemon, "commence...")
else:
    print(PokOrdi.nomdupokemon, "commence...")

# Boucle du jeu
while Pok.pointsdevie > 0 or PokOrdi.pointsdevie > 0:
    # On lance une attaque
    if Jeux.PlayerActif == 0:
        print(Pok.nomdupokemon, "attaque...")
    else:
        print(PokOrdi.nomdupokemon, "attaque...")

    # Si le player joue
    if Jeux.PlayerActif == 0:
        degat = Jeux.Attaque(Pok.attaque, Pok.bonusattaque)
        PokOrdi.pointsdevie -= degat
        print(PokOrdi.nomdupokemon, "a pris", degat, "il lui reste", PokOrdi.pointsdevie, "points de vie")
    # Si l'ordinateur joue
    elif Jeux.PlayerActif == 1 :
        degat = Jeux.Attaque(PokOrdi.attaque,PokOrdi.bonusattaque)
        Pok.pointsdevie -= degat
        print(Pok.nomdupokemon, "a pris", degat, "il vous reste", Pok.pointsdevie, "points de vie")
    if Pok.pointsdevie <= 0 or PokOrdi.pointsdevie <= 0:
        break
    Jeux.ChangePlayerActif()
    entree = input("Appuyez sur une touche pour continuer")

# Il y a un gagnant
if Pok.pointsdevie <= 0:
    print(Pok.nomdupokemon, "est mort. Vous avez perdu !")
else:
    print(PokOrdi.nomdupokemon, "est mort. Bravo vous avez gagné !")