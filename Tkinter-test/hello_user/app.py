from tkinter import *
import getpass
import webbrowser


def open_radical_github():
    webbrowser.open_new("https://github.com/Radic4l")


# fenetre principal

root = Tk()

# user variables
current_user = getpass.getuser()

# personalisation de la fenetre
root.title('Radical App')
root.geometry("720x480")
root.wm_minsize(480, 360)
root.wm_maxsize(720, 480)
root.iconbitmap("src/logo.ico")
root.config(background='#9aaabc')

# Creation de frame
frame = Frame(root, bg="#9aaabc")

# ajouter du texte
label_title = Label(frame, text="Hello " + current_user, font=("Consola", 16), bg='#9aaabc', fg='white')
label_title.pack()
# Second texte
label_subtitle = Label(frame, text="Application created by Radical", font=("Consola", 10), bg='#9aaabc', fg='white')
label_subtitle.pack()

# Ajouter un bouton
gh_button = Button(frame, text="Mon Github", font=("Consola", 14), bg="white", fg="#9aaabc",command=open_radical_github)
gh_button.pack(pady=25, fill=X)

# afficher la
frame.pack(expand=YES)

# afficher
root.mainloop()
