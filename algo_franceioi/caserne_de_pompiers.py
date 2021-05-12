nb_pairs = int(input())
zone1 = ()
zone2 = ()

for total_pair in range(nb_pairs):
    for pair in range(2):
        abscisse_min = int(input())
        abscisse_max = int(input())
        ordonee_min = int(input())
        ordonee_max = int(input())
        if not zone1:
            zone1 = (abscisse_min, abscisse_max, ordonee_min, ordonee_max)
        else:
            zone2 = (abscisse_min, abscisse_max, ordonee_min, ordonee_max)
    if ((zone2[0] < zone1[1]) and (zone2[2] < zone1[3])) \
            and ((zone2[1] > zone1[0]) and (zone2[2] < zone1[3])) \
            and ((zone1[0] < zone2[1]) and (zone1[2] < zone2[3])):
        print("OUI")
    else:
        print("NON")
    zone1 = ()
    zone2 = ()
