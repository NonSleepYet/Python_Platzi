#Ejemplo de iteradores

#Crear una lista
my_list = [1, 2, 3, 4]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))

#Creando cadena
text = "Hola mundo"
#creando objeto iterador
iter_text = iter(text)
#iterar la cadena
#for char in iter_text:
    #print(char)

#Crear iterador para los numeros impares

#limite
limit = 10
#Crear iterador
odd_itter = iter(range(0,limit+1,2))
#usar iterador
for num in odd_itter:
    print(num)


