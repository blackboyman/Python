# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        message_presentation = "Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans"

        print(message_presentation)
        self.GenreMajorite()

    def EstMajeur(self):
        return self.age >= 18

    def GenreMajorite(self):
        if self.genre:#Masculin   
            print("Genre : Masculin")
            if self.EstMajeur():#EstMajeur=Oui    
                print("Je suis majeur")    
            else:#EstMajeur=Non 
                print("Je suis mineur") 
        else:#Feminin           
            print("Genre : Feminin")
            if self.EstMajeur():#EstMajeur=Oui    
                print("Je suis majeure")    
            else:#EstMajeur=Non 
                print("Je suis mineure") 
        print()

personne1 = Personne("Jean", 25, True)
personne1.SePresenter()

personne2 = Personne("ALIDA", 15, False)
personne2.SePresenter()

personne3 = Personne("Emilie", 77,False)
personne3.SePresenter()