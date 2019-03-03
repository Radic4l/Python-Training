# Introduction aux fonctions

## objectifs:
# Lire des mots correctements ecrit dans un fichier.
# Utiliser de nouvelles methodes sur nos chaines de caracteres.
# Creer des fonctions qui nous permettent de re-utiliser nos composants du correcteur orthographique.
# Datasets dictionnaire.txt et texte.txt.

# La tokenization du vocabulaire.

vocabulary = open("../sources/dictionnaire.txt","r",encoding="utf-8").read()
#print(vocabulary)

tokenized_vocabulary = vocabulary.split(" ")
#print(tokenized_vocabulary)

file = open("../sources/texte.txt","r", encoding="utf-8")
texte_string = file.read()
#print(texte_string)

# fonction replace(arg1,arg2) arg1 element à remplacer, arg2 element nouvelle valeur

# mon_texte = "python,est,cool".replace(","," ")
# print(mon_texte)

# retirer tous les caracteres speciaux (ponctuation) et les lignes vides de text_string.
# afficher text_string

new_texte_string = texte_string.replace(",","").replace(".","").replace("'","").replace("\n","")
#print(new_texte_string)


# Les fonctions

## ecrire une fonction clean_text qui retire ponctuation et lignes vides
## appliquer la fonction a text_string et assigner le resultat a la variable cleaned_text
## Afficher cleaned_text

def clean_text(value):
    cleaned_value = value.replace(".","")
    cleaned_value = value.replace(",","")
    cleaned_value = value.replace("'","")
    cleaned_value = value.replace("\n","")
    return(cleaned_value)

cleaned_text = clean_text(texte_string)
print(clean_text)
