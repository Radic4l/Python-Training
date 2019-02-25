import string
from random import randint, choice
from tkinter import *


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min,password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0, password)


# Creer une fenetre

window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("src/logo.ico")
window.config(background="#9aaabc")

# creer la frame principal
frame = Frame(window,bg="#9aaabc")


# creation d'image
width = 300
height = 300
image = PhotoImage(file="src/password.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width,height=height,bg='#9aaabc', bd=0,highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.grid(row=0,column=0,sticky=W)

# creer une sous boite
right_frame = Frame(frame,bg="#9aaabc")

# creer un titre
label_title = Label(right_frame,text="Mot de passe",font=("Helvetica",20), bg="#9aaabc", fg="white" )
label_title.pack()

# creer un champ/entree/input
password_entry = Entry(right_frame,font=("Helvetica",20), bg="#9aaabc", fg="white" )
password_entry.pack()

# creer un bouton
generate_password_button = Button(right_frame,text="Générer",font=("Helvetica",20), bg="#9aaabc", fg="white", command=generate_password)
generate_password_button.pack(fill=X)

# on place la sous boite a droite de la frame principal
right_frame.grid(row=0,column=1,sticky=W)

# affichier la frame
frame.pack(expand=YES)

# barre de menu
menu_bar = Menu(window)

# creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer notre fenetre pour ajouter le menu bar
window.config(menu=menu_bar)

# afficher une fenetre
window.mainloop()