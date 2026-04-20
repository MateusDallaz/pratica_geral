maior = 0;

while True:
    numero = int(input('Digite um número (Digite 0 para parar): '));
    
    if numero == 0:
        break;
        
    if maior == 0 or numero  > maior:
        maior = numero;
    
if maior == 0:
    print('Nenhum valor válido foi digitado');
else:
    print(f'O maior número digitado foi: {maior}');