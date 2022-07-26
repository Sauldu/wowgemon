class Arme:
    # Cette classe contient les infos sur une arme

    def __init__(self):
        self.nom = 'poings'
        self.degats = 1
        self.type = '[arme]'
        self.distance = 'contact'

    def presentation(self):
        # Affiche les valeurs de l'arme
        print('Arme : ', self.nom, ' qui fait ', self.degats,
              'dégats à la distance :', self.distance)
