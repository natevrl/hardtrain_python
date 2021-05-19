population = int(input())
jour = 0
contamine = 1

while contamine < population:
    jour += 1
    contamine += contamine*2

print(jour)