#Exercico 1:

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: ? '))
profissao = input('Qual sua profissão: ')

print(f'Olá, meu nome é {nome}, tenho {idade} anos e sou {profissao}')

#Exercicio 2:

n = int(input('Digite um número: '))

print(f'O antecessor de {n} é {n-1}, e o seu sucessor é {n+1}')

#Exercicio 3: 

n = int(input('Digite um numero: '))

for i in range (n, -1, -1):
    print(i)

#Exercicio 4

contador = 1
soma = 0

while contador <= 5:
    numero = int(input('Digite um numero: '))
    contador +=1
    soma += numero
    
print(f'A soma dos números é {soma}')

#Exercicio 5: 

nomes = []
contador = 1

while contador <= 5:
    nome = input(f'Digite o {contador}° nome: ')
    nomes.append(nome)
    contador += 1

print('\nLista de Nomes:')
for i, nome in enumerate(nomes, start = 1):
    print(f'{i} - {nome}')
    

#Exercicio 6:

temperaturas = []
contador = 1

while contador <= 7:
    dias = float(input(f'Digite a temperatura registrada no {contador}° dia: '))
    temperaturas.append(dias)
    contador += 1
    

media = sum(temperaturas)/len(temperaturas)

print(f'\nA temperatura máxima registrada na semana foi {max(temperaturas)}°C, a minima foi {min(temperaturas)}°C e a média semanal foi {media:.2f}°C')

#Exercicio 7:

nome = None

def saudacoes():
    nome = input('Digite seu nome: ')
    print(f'Saudações {nome}, Seja bem vindo')

saudacoes()

#Exercico 8:

idade = int(input('Digite sua idade: '))

def verificarIdade():
    if idade >= 18:
        print('Você é maior de idade')
    else: 
        print('Você é menor de idade')
        
verificarIdade()