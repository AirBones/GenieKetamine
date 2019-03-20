class Drogues:
    def __init__(self, intitule, prix):
        self.intitule = intitule
        self.prix = prix

    def __str__(self):
        return self.intitule + " : " + str(self.prix) + " $"
