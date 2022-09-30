name = 'Anna'
age = 18
height = 1,68
has_car = True

names = ['Anna', 'Oskars', 'Jenifer', 'Mik', 'Anna']
ages = [18, 20, 18, 17, 29]

for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")





annas_data = {
    'name': 'Anna',
    'age': 18,
    'email': 'anna@somemail.com',
    'school': 'Dobeles VĢ'
}

oskars_data = {
    'name': 'Oskars',
    'age': 20,
    'email': 'oskars@somemail.com',
    'school': 'Siguldas VĢ'
}

personal_data = [annas_data, oskars_data]

print(personal_data[0]['email'])
