car = {
    "brand": "Toyota",
    "Model": "Camry",
    "Year": 2020,
    "color": ["ash", "red", "black"],
    "User": "Mummy"
}
print(car)
print(car["Year"])
x = car.keys()
print(x)
car["Year"] = 2023
print(car)
# print(car.item())
# print(car)
# car = {
#     "brand": "Toyota",
#     "Model": "Camry",
#     "Year": 2020,
#     "color": ["ash", "red", "black"],
#     "User": "Mummy"
# }
# car.pop("color")
# print(car)
# car.popitem()
# print(car)
print("**************")    
for x in car:
    print(x)
print("**************")        
for a in car:
    print(car[a])    
print("**************")      
for c in car.values():
    print(c)   
print("**************")    
for d in car.items():
    print(d)    
print("**************")    
for e in car.keys():
    print(e)
print("**************") 
# for f in car.clear():
#     print(f)
# print("**************")    
# for h in car.get():
#     print(h)       

print("**************")
carr = {"brands": "Lexus"}
carr = car.copy()
print(carr)

Python_class = {
    'Student1':{
        'Name': 'John',
        'Age': 17,
        'Course': 'Ethical Hacking',
        'Complexion': 'Caramel'
    },
    'Student2':{
        'Name': 'Mummuy Happy',
        'Age': 20,
        'Course': 'Data Science',
        'Complexion': 'Caramel'
    },
    'Student3':{
        'Name': 'Justina',
        'Age': 17,
        'Course': 'Data Science',
        'Complexion': 'Fair'
    },
    'Student4':{
        'Name': 'Rejoice',
        'Age': 14,
        'Course': 'Cyber Security',
        'Complexion': 'Dark'
    },
    'Student5':{
        'Name': 'Chigemezu',
        'Age': 6,
        'Course': 'Marketing',
        'Complexion': 'Caramel'
    },
    'Student6':{
        'Name': 'Eyong Roy',
        'Age': 22,
        'Course': 'Data Science',
        'Complexion': 'Caramel'
    },
}
print(Python_class)
print(Python_class['Student1']['Name'])
print(Python_class.items())
for x in Python_class.items():
    print(x)
    
d = {}
print(d)
print(type(d))    