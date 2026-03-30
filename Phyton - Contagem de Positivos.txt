contador = 0;

while True:
        num = int(input('Digite um número (digite -1 para parar): '));
        
        if num == -1:
            break;
        if num > 0:
            contador += 1;
print('A quantia de número positivos digitados é de: ', contador);