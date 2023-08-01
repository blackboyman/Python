

def reverseString(chaine):
    Nvocaracter = ""
    for caracter in chaine:
        Nvocaracter = caracter+Nvocaracter
    return Nvocaracter

print(reverseString('karamoko COULIBALY'))

def reverseString2(chaine):
    return chaine[::-1]

print(reverseString2('karamoko COULIBALY Hamed'))
'''
def reverseString(chaine):
    TestARenverser = []
    TestARenverser.append(chaine)
    caracter = []
    for i in TestARenverser:
        print(i)
        print(len(i))
        for j in range(len(i)):
            caracter.append(i[j-1])
            #print(i[j])
        print(caracter)

reverseString('karamoko')
'''