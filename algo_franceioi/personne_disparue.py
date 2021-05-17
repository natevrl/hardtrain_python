homme_recherchee = int(input())
liste_personnes = int(input())
for personne in range(liste_personnes):
    numero_personne = int(input())
    homme_est_dans_laville = (homme_recherchee == numero_personne)
    if homme_est_dans_laville:
        print("Sorti de la ville")
        break
else:
    print("Encore dans la ville")






