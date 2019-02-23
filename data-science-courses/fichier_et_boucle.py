#open() ouvrir un fichier 'r' mode read
file = open('sources/mon_texte.txt','r')
print(file)

# lis le contenu du fichier
read_file = file.read()
print(read_file)