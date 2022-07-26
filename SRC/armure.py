class Armure:
    # Cette classe contient les infos sur une armure
    def __init__(self):
        self.nom = 'aucune'
        self.protection = 0
        self.type = '[armure]'

    def presentation(self):
        # Affiche les valeurs d'armure

        print('Armure :', self.nom, ' qui protège de ', self.protection,
              'dégats')
