name = 'Anna'
age = 18
height = 1,68
has_car = True

names = ['Anna', 'Oskars', 'Jenifer', 'Mik', 'Anna']
ages = [18, 20, 18, 17, 29]

for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")





personal_data = [
    {
        'name': 'Anna', 
        'age': 18, 
        'email': 'anna@somemail.com', 
        'school': 'Dobeles VĢ',
        
        'car': {
            'brand': 'audi',
            'year': 2020,
            'color': 'sarkana',
            'engine': 2.0
            }
    },
    {
        'name': 'Oskars', 
        'age': 20,
        'email': 'oskars@somemail.com',
        'school': 'Siguldas VĢ'
    },
    {
        'name': 'Jenifer', 
        'age': 17,
        'email': 'jenife@somemail.com',
        'school': 'Talmācības'     
    }
]

for data in personal_data:
    print(data['email'])
