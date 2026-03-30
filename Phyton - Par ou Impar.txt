par = 0
impar = 0

while True:
    numero = int(input('Digite um número (Digite 0 para parar): '));
    if numero == 0:
        break;
    
    if numero %2 == 0:
        par += 1;
    else:
        impar += 1;
        
print('A quantia de números pares digitados é de: ', par, 'e a quantia de números impares é de:', impar);