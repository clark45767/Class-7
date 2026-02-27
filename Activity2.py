my_dictionary_1={}
my_dicrionary_2={1:'apple',
                 2:'pineapple',
                 3:'orange',
                 4:'banana'}
my_dictionary_3={'name':'Clark', 1:[4,23.7]}
my_dictionary_1 ={'name': 'Clark', 'age':16}
print(my_dictionary_1['name'])
print(my_dictionary_1['age'])
#update value
my_dictionary_1['age'] = 25
#add value
my_dictionary_1['address'] = 'UAE'
print(my_dictionary_1)
#remove element
my_dictionary_1.pop('age')
print(my_dictionary_1)
#access particular element
print("Address :", my_dictionary_1.get('address'))