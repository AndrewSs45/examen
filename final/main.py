numeros = input("Ingresa los números separados por comas: ")
numb = numeros.split(',')
lista = [int(numero) for numero in numb]
print("Lista creada:", lista)

maxnumber = max(lista)
print("El número más grande es:", maxnumber)

listnumb = int(input('Digite el número que deseas saber el número de repeticiones: '))
repeticiones = lista.count(listnumb)

print(f'El número {listnumb} se repite {repeticiones} veces')

