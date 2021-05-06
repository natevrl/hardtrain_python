from tkinter import *

FILM_SEMAINE_04 = [{"numero": 1, "titre": "Voyage au centre du html", "horaire": "20h10", "place_dispo": 100},
                   {"numero": 2, "titre": "Les 9 jsons cachés", "horaire": "18h00", "place_dispo": 3},
                   {"numero": 3, "titre": "Algobox - Le Film", "horaire": "15h00", "place_dispo": 117}]

FILM_SPECIAL_HALLOWEEN = [{"numero": 1, "titre": "Massacre a la tronconeuse", "horaire": "14h00", "place_dispo": 120},
                          {"numero": 2, "titre": "Freddy", "horaire": "23h44", "place_dispo": 17},
                          {"numero": 3, "titre": "J'ai rencontré le diable", "horaire": "00h00", "place_dispo": 4},
                          {"numero": 4, "titre": "Saw 7", "horaire": "20h00", "place_dispo": 54},
                          {"numero": 5, "titre": "Annabelle", "horaire": "04h00", "place_dispo": 12}]

# init tkinter
fenetre = Tk()
fenetre.title("Logiciel Gestion - Cinema")
fenetre.geometry("600x400")


# fonction qui s'active lorsque qu'on clique sur le bouton reserver
def click_btn(list_film, film_id, txt_variable):
    print("click of sur le film : ", film_id)
    if list_film[film_id - 1]['place_dispo'] > 0:
        list_film[film_id - 1]['place_dispo'] -= 1
        txt_variable.set(list_film[film_id - 1]['place_dispo'])
        print(f"vous avez choisis : {list_film[film_id - 1]['titre']}")
        print(f"il reste desormais {list_film[film_id - 1]['place_dispo']} places")
    else:
        print(f"Desole, {list_film[film_id - 1]['titre']} est complet !")
        txt_variable.set("Film complet")


def gestion_tkinter(list_film):
    for film in list_film:
        place_var = StringVar()
        place_var.set(film["place_dispo"])

        titre_label = Label(fenetre, text=film["titre"])
        titre_label.grid(row=film['numero'], column=0)

        titre_places = Label(fenetre, textvariable=place_var)
        titre_places.grid(row=film['numero'], column=1)

        titre_horaires = Label(fenetre, text=film["horaire"])
        titre_horaires.grid(row=film['numero'], column=2)

        bouton_reserver = Button(fenetre, text="Reserver", activebackground="Green", command=lambda
            num=film["numero"],
            txt_variable=place_var: click_btn(list_film, num, txt_variable))
        bouton_reserver.grid(row=film['numero'], column=3)


def main():
    gestion_tkinter(FILM_SEMAINE_04)
    fenetre.mainloop()


if __name__ == "__main__":
    main()
