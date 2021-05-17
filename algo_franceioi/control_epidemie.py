la_plus_haute = []
# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        la_plus_haute.append(mountain_h)

    print(max(la_plus_haute))