class ConversionUnite:
    def __init__(self, typeConversion):
        self.typeConversion = typeConversion

        print("1) Conversion metres vers pouces")
        print("2) Conversion pouces vers metres")

        while self.typeConversion not in ("1", "2"):
            self.typeConversion = input("Entrée votre choix 1 ou 2 : ")

    def conversion(self, unite: []):
        if self.typeConversion == "1":
            i = 0
            while i < len(unite):
                unite[i] = unite[i] / 0.0254
            i += 1
        elif self.typeConversion == "2":
            unite = unite * 0.0254
        return unite

    def saisieUnite(self):
        valUnite = []
        val = 1
        i = 1
        while val != 0:
            val = int(input("Entrez la valeur " + str(i) + " à convertir (0 pour arrêter la saisie) : "))
            valUnite.append(val)
            i += 1
        #print(valUnite)

    def afficher(self, tabUnite: []):
        i = 0
        while i < len(tabUnite):
            print("Le resultat est : ", tabUnite[i])
        i += 1

conv = ConversionUnite(1)
tabSaisie = []
tabSaisie = conv.saisieUnite()

for i in range(0, len(tabSaisie)):
    print(tabSaisie[i])
#tabList = conv.conversion(tabSaisie)
'''
j = 0
while j < len(tabSaisie):
    print(tabSaisie[j])
j += 0

tabUnite = []
tabUnite = conv.conversion(tabSaisie)
print(tabUnite)
conv.afficher(tabUnite)
'''