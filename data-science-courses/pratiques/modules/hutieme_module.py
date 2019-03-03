# Training 8 / mettre le cours en pause

## Modifier la fonction clean_text()
## Ajouter un deuxieme argument special_characters qui seras une liste de caracteres speciaux (ponctuation, saut de ligne ...)
## Ajouter un troisieme argument replacement_string qui seras l'element de remplacement

## Ecrire une boucle qui parcourt les elements de special_characters afin de remplacer chacun de ces elements par replace_string

## Transformer toujours les majuscules en minuscules
## tester votre fonction avec text_string comme premier argument, clean_characters = [",",".","'","\n"] comme deuxieme argument et replacement = "" comme troiseme
## assigner le resultat a cleaned_text et l'afficher

vocabulary = open("../../sources/dictionnaire.txt","r",encoding="utf-8").read()
#print(vocabulary)

tokenized_vocabulary = vocabulary.split(" ")
#print(tokenized_vocabulary)

file = open("../../sources/texte.txt","r", encoding="utf-8")
text_string = file.read()
print('\033[92m' +"initial text: \n" + text_string + "\n End initial text" + '\033[0m')

def clean_text(value,special_characters, replacement_string):
    #print(special_characters)
    for char in special_characters:
        value = value.replace(char,replacement_string)
        print('\033[94m' + "Text modified " + char +" : \n" + value + "\nEnd modified text\n\n\n\n" + '\033[0m')
    cleaned_value = value.lower()
    return(cleaned_value)

cleaned_text = clean_text(text_string,special_characters=[",",".","'","\n"],replacement_string="")
print('\033[93m' + "Final text: \n" + cleaned_text + "\nEnd final text" + '\033[0m')