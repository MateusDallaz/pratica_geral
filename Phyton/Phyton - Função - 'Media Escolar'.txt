aluno = {
    'nome': None,
    'nota1': None,
    'nota2': None,
    'nota3': None
 };

def mediaFinal():
    return aluno['nome'] is not None;
    
def cadastroAluno():
    print('\n--- Cadastro do Aluno --- \n');
    aluno['nome'] = input('Digite o nome do aluno: ');
    aluno['nota1'] = float(input('Digite a 1ª nota: '));
    aluno['nota2'] = float(input('Digite a 2ª nota: '));
    aluno['nota3'] = float(input('Digite a 3ª nota: '));
    print('\n--- Aluno cadastrado com sucesso! ---');
    
def mostrarAluno():
    print('\n--- Alunos Cadastrados ---\n');
    if not mediaFinal():
        print('Nenhum aluno cadastrado.\n');
    else:
        print(f"Nome: {aluno['nome']}");
        print(f"1ª Nota: {aluno['nota1']}");
        print(f"2ª Nota: {aluno['nota2']}");
        print(f"3ª Nota: {aluno['nota3']}");

def calculoMedia():
    media = (aluno['nota1'] + aluno['nota2'] + aluno['nota3']) / 3;
    print(f"\nSua media final é: {media:.2f}")
    if media >= 7:
        print('\nParabéns você foi aprovado!');
    elif media >=5 and media < 7:
        print('\nVocê está em recuperação');
    else:
        print('\nVocê foi reprovado, estude mais na prixima vez')
        
    return media;

def atualizarMedia():
    print('\n--- Atualização de Medias ---\n')
    if not mediaFinal():
        print('Nenhum aluno cadastrado.\n');
    else:
        aluno['nome'] = input('Digite o novo nome do aluno: ');
        aluno['nota1'] = float(input('Digite a 1ª nota: '));
        aluno['nota2'] = float(input('Digite a 2ª nota: '));
        aluno['nota3'] = float(input('Digite a 3ª nota: '));
        print('\n--- Aluno atualizado com sucesso! ---');

def menu():
    while True:
        print('\n--- Menu Interativo ---\n')
        print('1 - Cadastrar Aluno');
        print('2 - Mostrar Dados do Aluno');
        print('3 - Calcular Média');
        print('4 - Atualizar Dados');
        print('5 - Sair');
        
        opcao = input('\nEscolha uma opção: ')
        
        if opcao == '1':
            cadastroAluno();
        elif opcao == '2':
            mostrarAluno();
        elif opcao == '3':
            calculoMedia();
        elif opcao == '4':
            atualizarMedia();
        elif opcao == '5':
            print('\n Até a próixima!');
            break;
        else:
            print('\n--- Por gentileza digite uma opção valida ---\n');
            
menu();