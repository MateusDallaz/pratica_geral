cliente = {
    'nome': None,
    'cpf': None,
    'saldo': None,
}

def contaCriada():
    return cliente['nome'] is not None;
    
def criarConta():
    print('\n--- Criação de Conta ---\n');
    cliente['nome'] = input('Digite seu nome: ');
    cliente['cpf'] = input('Digite seu CPF: ');
    cliente['saldo'] = float(input('Digite seu saldo inicial: '));
    print('\n--- Cliente cadastrado com sucesso! ---')
    
def verSaldo():
    print('\n --- Saldo Disponivel ---\n');
    if not contaCriada():
        print('Nenhuma conta cadastrada');
    else:
        print(f"O saldo seu saldo disponivel é de: R${cliente['saldo']:.2f}")

def deposito():
    print('\n--- Deposito ---\n');
    if not contaCriada():
        print('Nenhuma conta cadastrada');
    else:
        deposito = float(input('Digite a quantia que deseja depositar: '));
       
        if deposito <= 0:
           print('Digite um valor valido para deposito');
        else:
           cliente['saldo'] += deposito;
           print(f"Deposito realizado com suscesso!\nSeu novo saldo é de: R${cliente['saldo']:.2f}");
           
def saque():
    print('\n--- Saque ---\n');
    if not contaCriada():
        print('Nenhuma conta cadastrada');
    else:
        saque = float(input('Digite o valor de saque: '));
        
        if saque > cliente['saldo']:
            print('Saldo Insuficiente!\n');
        elif saque <= 0:
            print('Digite um valor valido\n');
        else:
            cliente['saldo']-= saque;
            print(f"Saque realizado com sucesso!\nSeu novo saldo é de: R${cliente['saldo']:.2f}");

def menu():
    while True:
        print('--- Menu ---\n');
        print('1- Criar conta');
        print('2- Ver saldo');
        print('3- Deposito');
        print('4- Saque');
        print('5- Sair');
        
        opcao = input('\nEscolha uma oção: ');
        
        if opcao  == '1':
            criarConta();
        elif opcao == '2':
            verSaldo();
        elif opcao == '3':
            deposito();
        elif opcao == '4':
            saque();
        elif opcao == '5':
            print('\nEspero ter ajudado, Até a proxima!');
            break;
        else:
            print('\nDigite uma opção valida\n');
            
menu();