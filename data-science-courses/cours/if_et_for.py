# preparation
file = open("../sources/departements-fr.csv","r")
read_file = file.read()

# mise en forme
rows = read_file.split('\n')

departements = []
int_habitants = []

for row in rows:
    values = row.split(',')
    departements.append(values[0])
    int_habitants.append(int(values[1]))

print(departements)
print(int_habitants)

# Condition if et boucle for
found = False

for dep in departements:
    if dep == 'Paris':
        found = True

if found:
    print('Paris est present dans la liste')

counter = 0
index = 0

for dep in departements:
    if dep == "Paris":
        index = counter
    counter += 1

print(index)