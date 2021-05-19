total = 0
run = True
while run:
    entier = int(input())
    if entier != -1:
        total = entier + total
    else:
        run = False

print(total)
