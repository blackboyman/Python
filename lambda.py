liste = [10,6,-5,5,30,-50,100]

lambda_sorted = lambda element_list: (sorted(index) for index in element_list)

sorted_liste = lambda_sorted(liste)

print(sorted_liste)

sortList = lambda x: (x.sort())
sortList(liste)
print(liste)