cities_number = ["Paris,45","Madrid,171","Rome,12"]

final_list = []

for row in cities_number:
    split_list = row.split(",")
    final_list.append(split_list)

print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])