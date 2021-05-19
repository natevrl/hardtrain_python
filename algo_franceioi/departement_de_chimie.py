total_mesures = int(input())
temperature_minimal = int(input())
temperature_maximal = int(input())

for _ in range(total_mesures):
    prelevement = int(input())
    if temperature_minimal <= prelevement <= temperature_maximal:
        print("Rien à signaler")

    else:
        print("Alerte !!")
        break
