maior = None;
menor =  None;

while True:
    numero = int(input('Digite um número: '));
    
    if numero == 0:
        break;
    
    if maior is None or numero > maior:
        maior = numero;
        
    if menor is None or numero < menor:
        menor = numero;
        
print('O maior número digitado foi: ', maior);
print('O menor número digitado foi: ', menor);