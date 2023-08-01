class Personne:
    def __init__(self, nom:str ="", age:int=0):
        self.nom = nom
        #Vérification nom vide
        if self.nom == "":
            self.DemanderNom()
        ######################

        self.age = age
        #print("Constructeur personne " + nom +" age "+ str(self.age))

    def DemanderNom(self):
        self.nom = input("Saisir le nom : ")
       # self.age = input("Saisir age : ")

    def SePresenter(self):
        if self.age == 0:
            print("Je m'appel " + str(self.nom))
        else:
            print("Je m'appel " + str(self.nom) + " j'ai " + str(self.age))

#Test de majorité
        if self.age !=0:
            if self.EstMajeur():
                print("Je suis mineur")
            else:
                print("Je suis majeur")
    def EstMajeur(self):
        if self.age <= 18:
            return True
        return False


print()
personne1 = Personne("",0)
personne1.SePresenter()
#print(personne1.EstMajeur())

print()

personne2 = Personne("KARAMOKO",88)
personne2.SePresenter()
#print(personne2.EstMajeur())

print()

personne3 = Personne("KARAMOKO",15)
personne3.SePresenter()
#print(personne2.EstMajeur())
