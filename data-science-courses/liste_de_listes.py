cities_number = ["Paris,45","Madrid,171","Rome,12"]

final_list = []

for row in cities_number:
    split_list = row.split(",")
    final_list.append(split_list)

print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

# Recuperer et afficher les elements d'une liste de listes
first_list = final_list[0]
first_list_first_value = first_list[0]

print("My first value from my first list in my list of lists is : {0}".format(first_list_first_value))

# ou alors on peut aussi faire

first_list_first_value_2 = final_list[0][0] # premiere liste premiere element
print("My first value from my first list in my list of lists is : {0}".format(first_list_first_value_2))

second_list_first_value = final_list[1][0]
print("My first value from my second list in my list of lists is : {0}".format(second_list_first_value))

second_list_second_value = final_list[1][1] # deuxieme liste deuxieme element
print("My second value from my second list in my list of lists is : {0}".format(second_list_second_value))