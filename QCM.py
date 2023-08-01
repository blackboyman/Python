# LES COLLECTIONS : PROJET QUESTIONNAIRE
#
# Partez de ce code source pour réaliser la version 2 du projet questionnaire
#
#############################################################################
# FORMATION COMPLÈTE "DÉVELOPPEUR PYTHON"
#
# Pour progresser en programmation et aller plus loin avec le langage Python,
# découvrez ma formation complète ici :
# https://codeavecjonathan.com/formations.html
#############################################################################
def demander_reponse_numerique_utilisateur(min, max):
  reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") : ")
  try:
    reponse_int = int(reponse_str)
    if(min <= reponse_int <= max):
      return reponse_int
    print("ERREUR: Merci Entrer un nombre (entre " + str(min) + " et " + str(max) + ")")
  except:
    print("ERREUR: Merci Entrer un nombre ")

  return demander_reponse_numerique_utilisateur(min, max)


def poser_question(question):
  titre_question = question[0]
  choix = question[1]
  bonne_reponse = question[2]

  global score
  print("QUESTION")
  print(titre_question)

  for i in range(len(choix)):
    print(i + 1, " : ", choix[i])
  print()

  reponse_int = demander_reponse_numerique_utilisateur(1, len(choix) )

  if choix[reponse_int - 1].lower() == bonne_reponse.lower():
    print("Bonne réponse")
    score += 1
  else:
    print("Mauvaise réponse")

  print()


score = 0
print("Score final :", score)



def lancer_questions(questionnaire):
  for question in questionnaire:
    poser_question(question)

question1 = "Quelle est la capitale de la France ?", ("Marseille", "Nice",
                                                      "Paris", "Nantes",
                                                      "Lyon"), "Paris"
question2 = "Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise","Florence"), "Rome"

question3 = "Quelle est la capitale de Russie ?", ("Rome", "Venise", "Moscou","Florence"), "Moscou"


questionnaire = (question1, question2, question3)
lancer_questions(questionnaire)



