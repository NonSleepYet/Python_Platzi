numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"Nombre": "Gustavo",
               "Apellido": "Vanegas",
               "Altura" : 1.65,
               "Edad" : 30}
print(information)
del information ["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Gustavo": {"Nombre": "Gustavo",
               "Apellido": "Vanegas",
               "Altura" : 1.65,
               "Edad" : 30},
                "Daniela" :{"Nombre": "Daniela",
               "Apellido": "Rodriguez",
               "Altura" : 1.65,
               "Edad" : 27},
                "Crisopher" :{"Nombre": "Cristopher",
               "Apellido": "Vanegas",
               "Altura" : 1.02,
               "Edad" : 5}}
print(contacts["Daniela"])