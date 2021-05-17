nb_personnes = int(input())
# critères suspects
def degre_de_suspectabilite(taille, age, poids, cheval, cheveux_brun):
    trait_suspect = 0
    if ((taille >= 178) and (taille <= 182)):
        trait_suspect += 1
    if (age >= 34):
        trait_suspect += 1
    if (poids < 70):
        trait_suspect += 1
    if(cheval == 0):
        trait_suspect += 1
    if (cheveux_brun == 1):
        trait_suspect += 1
    if trait_suspect == 5:
        print("Très probable")
    elif trait_suspect == 3 or trait_suspect == 4:
        print("Probable")
    elif trait_suspect == 0:
        print("Impossible")
    elif trait_suspect == 1 or trait_suspect == 2:
        print("Peu probable")
def main():
    for personne in range(nb_personnes):
        degre_de_suspectabilite(taille=int(input()), age=int(input()), poids=int(input()), cheval=int(input()),
                                cheveux_brun=int(input()))

if __name__ == "__main__":
    main()



# nb_personnes = int(input())
#
# for personne in range(nb_personnes):
#     trait_suspect = 0
#     taille = int(input())
#     age = int(input())
#     poids = int(input())
#     cheval = int(input()) #1 = True // 0 = False
#     cheveux_brun = int(input()) #1 = True // 0 = False
#
#     # critères suspects
#     taille_suspecte = ((taille >= 178) and (taille <= 182))
#     age_suspect = (age >= 34)
#     poids_suspect = (poids < 70)
#     cheval_suspect = (cheval == 0)
#     cheveux_brun_suspect = (cheveux_brun == 1)
#
#     if taille_suspecte:
#         trait_suspect += 1
#     if age_suspect:
#         trait_suspect += 1
#     if poids_suspect:
#         trait_suspect += 1
#     if cheval_suspect:
#         trait_suspect += 1
#     if cheveux_brun_suspect:
#         trait_suspect += 1
#
#     if trait_suspect == 5:
#         print("Très probable")
#     elif trait_suspect == 3 or trait_suspect == 4:
#         print("Probable")
#     elif trait_suspect == 0:
#         print("Impossible")
#     elif trait_suspect == 1 or trait_suspect == 2:
#         print("Peu probable")
