menor = None;

while True:
    numero = int(input('Digite um número (Digite 0 para parar): '));
    
    if numero == 0:
        break;
        
    if menor is None or numero < menor:
        menor = numero;
    
if menor is None:
    print('Nenhum valor válido foi digitado');
else:
    print('O menor número digitado foi:', menor);