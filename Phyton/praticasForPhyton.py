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

#Exercicio 14:

menor = 0

for i in range(1, 6):
    numero = int(input('Digite um número: '))
    if menor == 0 or numero < menor:
        menor = numero
        
print(f'O maior número digitado foi: {menor}')

#Exercicio  15:

positivos = []
for i in range(1, 11):
    numero = int(input('Digite um número: '))
    if numero %2 == 0:
        positivos.append(numero)

print(f'Os numeros positivos são: {positivos}')

#Exercicio 16:

par = 0
impar = 0

for i in range(1, 11):
    numero = int(input('Digite um número: '))
    if numero %2 == 0:
        par += 1
    else:
        impar += 1

print(f'O total de números pares foi de {par} e os impares foi {impar}')

#Exercicio 17:

multi = 1

for i in range(1, 6):
    num = int(input('Digite um número: '))
    multi *= num
    
print(f'A multiplicação final ficou: {multi}')

#Exercicio 18:

nome = input('Digite seu nome: ')

for letra in nome:
    print(letra)

#Exercicio 19:

palavra = input('Digite uma palavra: ').lower()
contador = 0

for letra in palavra:
    if  letra in "aeiou":
        contador +=1
        
print(f'A quantidade de vogais é: {contador}')

#Exercicio 20:

palavra = input('Digite uma palavra: ').lower()
contador = 0

for letra in palavra:
    if  letra not in "aeiou":
        contador +=1
        
print(f'A quantidade de consoantes é: {contador}')