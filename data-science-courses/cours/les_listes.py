# Créer une liste

month = []
month.append("janvier")
month.append("février")
# etc

print(month)
print(type(month))

month_2 = [1,"janvier",2,"février"]
print(month_2)

temperatures = ["France",122.5,"Spain",124.0]
temperatures.append("United States")
temperatures.append(134.1)

print(temperatures)

# Récupérer une valeur dans une liste

years = [2013,2014,2015,2016,2017,2018,2019]

first_value = years[0]
second_value = years[1]
last_value = years[6]
print(first_value)
print(second_value)
print(last_value)

# Récupérer la longueur d'une liste

int_month = [1,2,3,4,5,6,7,8,9,10,11,12]
total_length = len(int_month)
print(total_length)

last_value_position = len(int_month) - 1
last_value = int_month[last_value_position]
print(last_value)

last_value_1 = int_month[(len(int_month) - 1)]
print(last_value_1)

countries = ["France","Spain","Russian","Canada","Australia","Argentina"]
temperatures = [122.5,124.0,95.7,105.2,112.5,128.3]
print(len(countries) + len(temperatures))

# Récupérer un morceau de liste (slicing)
all_months = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
months_slicing_1 = all_months[3:9]
print(months_slicing_1)

months_slicing_2 = all_months[5:]
print(months_slicing_2)

