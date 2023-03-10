import random  # Utilisé pour les nombres aléatoires


class Pokemon:
    # Classe de Pokemon utilisé pour le Player mais aussi pour l'ordinateur
    def __init__(self):
        # On instancie les attributs de la classe à des valeurs initiales
        self.nomdupokemon = ""
        self.pointsdevie = 0
        self.typespokemon = "Aucun"
        self.attaque = 0
        self.bonusattaque = 1
        self.defense = 0
        self.niveau = 1


    def ChoixPlayerpokemon(self, nom):
        # Méthode Choix du pokémon
        # Mise à jour des attributs en fonction du choix de Pokémon
        if nom == "Ponyta":
            self.nomdupokemon = "Ponyta"
            self.pointsdevie = 100
            self.typespokemon = "Feu"
            self.attaque = 85
            self.defense = 55
            self.niveau = 5
        elif nom == "Carapuce":
            self.nomdupokemon = "Carapuce"
            self.pointsdevie = 100
            self.typespokemon = "Eau"
            self.attaque = 48
            self.defense = 65
            self.niveau = 5
        elif nom == "Racaillou":
            self.nomdupokemon = "Racaillou"
            self.pointsdevie = 100
            self.typespokemon = "Terre"
            self.attaque = 80
            self.defense = 100
            self.niveau = 5
        elif nom == "Evoli":
            self.nomdupokemon = "Evoli"
            self.pointsdevie = 100
            self.typespokemon = "Normal"
            self.attaque = 55
            self.defense = 50
            self.niveau = 5


    # Méthode pour choisir aléatoirement un Pokémon adverse
    def ChoixRandomPlayerOrdi(self):
        pokemonadversaire = ['Ponyta', 'Carapuce', 'Racaillou', 'Evoli']
        # On choisit au hasard un pokémon
        choixadversaire = random.choice(pokemonadversaire)
        if choixadversaire == "Ponyta" :
            self.nomdupokemon = "Ponyta"
            self.pointsdevie = 40
            self.typespokemon = "Feu"
            self.attaque = 55
        elif choixadversaire == "Carapuce" :
            self.nomdupokemon= "Carapuce"
            self.pointsdevie = 48
            self.typespokemon = "Eau"
            self.attaque = 41
        elif choixadversaire == "Racaillou" :
            self.nomdupokemon = "Racaillou"
            self.pointsdevie = 40
            self.typespokemon = "Terre"
            self.attaque = 52
        elif choixadversaire == "Evoli":
            self.nomdupokemon = "Evoli"
            self.pointsdevie = 40
            self.typespokemon = "Normal"
            self.attaque = 52


    # Méthode pour calculer les avantages et faiblesses entre deux pokémons
    def AvantageFaiblesse(self,typeAtt,typeDef) :
        # Attaquant Eau
        if typeAtt == "Eau" :
            if typeDef == "Feu" :
                self.bonusattaque = 2
            elif typeDef == "Terre" :
                self.bonusattaque = 0.5
            elif typeDef == "Eau" :
                self.bonusattaque = 1
            elif typeDef == "Normal":
                self.bonusattaque = 1

        # Attaquant Feu
        if typeAtt == "Feu" :
            if typeDef == "Feu" :
                self.bonusattaque = 1
            elif typeDef == "Terre" :
                self.bonusattaque = 2
            elif typeDef == "Eau" :
                self.bonusattaque = 0.5
            elif typeDef == "Normal" :
                self.bonusattaque = 1

        # Attaquant Terre
        if typeAtt == "Terre" :
            if typeDef == "Feu" :
                self.bonusattaque = 0.5
            elif typeDef == "Terre" :
                self.bonusattaque = 1
            elif typeDef == "Eau" :
                self.bonusattaque = 2
            elif typeDef == "Normal" :
                self.bonusattaque = 1

        # Attaquant Normal
            if typeAtt == "Noraml":
                if typeDef == "Feu":
                    self.bonusattaque = 0.75
                elif typeDef == "Terre":
                    self.bonusattaque = 0.75
                elif typeDef == "Eau":
                    self.bonusattaque = 0.75
                elif typeDef == "Normal":
                    self.bonusattaque = 1
