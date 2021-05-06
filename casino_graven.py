import random
print("Bienvenue sur la nouvelle machine à sous de N4t4nistorus")

list_fruits = ["ananas", "cerise", "orange", "pasteque", "pomme_dore"]

hasard_3 = random.choices(list_fruits, weights=(20, 25, 40, 10, 5), k=3)

print(hasard_3)

