maior = None;

while True:
    numero = int(input('Digite um número (Digite 0 para parar): '));
    
    if numero == 0:
        break;
        
    if maior is None or numero  > maior:
        maior = numero;
    
if maior is None:
    print('Nenhum valor válido foi digitado');
else:
    print('O maior número digitado foi: ', maior);