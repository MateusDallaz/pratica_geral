#Exercicio 1:

for i in range(1, 11):
    print(i)

#Exercicio 2:

for i in range(10, 0, -1):
    print(i)

#Exercicio 3:

for i in range(0, 20, 2):
    print(i)

#Exercicio 4:

for i in range(1, 20, 2):
    print(i)

#Exercicio 5:

n = int(input('Digite um numero: '))

for i in range (1, 11):
    print(f'A tabuada de {n} é: {i} x {n} = {n*i}')

#Exercicio 6:

soma = 0

for i in range(1, 101):
    soma += i

print(f'A soma dos numeros é: {soma}')

#Exercicio 7:

n = int(input('Digite um número: '))

for i in range(1, n+1):
    print(i)


#Exercicio 8:

soma = 0

for i in range(0, 51, 2):
    soma += i

print(f'A soma é: {soma}')

#Exercicio 9:

soma = 0

for i in range(1, 51, 2):
    soma += i

print(f'A soma é: {soma}')

#Exercicio 10:

for i in range(1, 11):
    print(f'{i}² = {i**2}')    

#Exercicio 11:

for i in range(1, 11):
    print(f'{i}³  = {i**3}')

#Exercicio 12:

soma = 0

for i in range(1, 6):
    nota = int(input('Digite as notas: '))
    soma += nota

media = soma/5

print(f'A media final é igual a: {media}')

#Exercicio 13:

maior = 0

for i in range(1, 6):
    numero = int(input('Digite um número: '))
    if maior == 0 or numero > maior:
        maior = numero
        
print(f'O maior número digitado foi: {maior}')