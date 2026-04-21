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

#Exercicio 21:

frase = input('Digite a frase: ')

for caractere in frase:
    print(caractere)

#Exercicio 22: 

lista = []
soma = 0

for numero in range(1, 6):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    soma += numero

print(f'A soma dos numeros {lista} é {soma}')

#Exercicio 23:

pares = []
impares = []

for i in range(1, 11):
    numero = int(input('Digite um número: '))
    if numero %2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
        
print(f'Dentre os números digitados: {pares} são pares e {impares} são impares')

#Exercicio 24:

lista = []
maior = 0

for i in range(1, 11):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if maior == 0 or numero > maior:
        maior = numero
    
print(f'O maior número digitado foi: {maior}')

#Exercicio 25:

lista = [1, 2, 5, 7, 3, 2, 9, 3, 8, 2, 6, 6, 9, 2, 5]
procurado = int(input('Digite o numero procurado (ente 1 e 10): '))
contador = 0 

for numero in lista:
    if numero == procurado:
        contador += 1

if contador > 0:
    print(f'O número {procurado} apareceu {contador} vezes')
else:
    print(f'O número {procurado} não está na lista')

#Exercicio 26:

numero = int(input('Digite um número: '))
fatorial = 1

for i in range(1, numero + 1):
    print(f"{fatorial} x {i} = {fatorial * i}")
    fatorial = fatorial * i
    
print(f"\nO resultado final é: {fatorial}")

#Exercicio 27:

numero = int(input('Digite um número: '))
contador = 0

for i in range(1, numero +1):
    if numero % i == 0:
        contador += 1

if contador == 2:
    print(f'\nO número {numero} é primo')
else:
    print(f'\nO número {numero} não é primo')

#Exercicio 28:

numero = int(input('Digite um número: '))
contador = 0
divisor = []

for i in range(1, numero +1):
    if numero % i == 0:
        contador += 1
        divisor.append(i)

print(f'\nO número {numero} é dividido por {divisor}')
if contador == 2:
    print(f'E o número {numero} é primo')
else:
    print(f'E o número {numero} não é primo')

#Exercicio 29:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número maior que o anterior: '))
soma = 0

for i in range (n1, n2 + 1):
    antes = soma
    soma += i
    print(f'\n{antes} + {i} = {soma}')

print(f'\nO resultado da soma dos números entre {n1} e {n2} é: {soma}')