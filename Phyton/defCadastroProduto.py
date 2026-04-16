produto = {
    'nome': None,
    'preco': None,
    'quantidade': None
};

def produtoCadastrado():
    return produto['nome'] is not None;
    
def cadastroProduto():
    print('--- Cadastro de Produto --- \n');
    produto['nome'] = input('Digite o nome do produto: ');
    produto['preco'] = float(input('Digite o Preço: '));
    produto['quantidade'] = int(input('Digite a Quantidade em Estoque: '));
    print('\n--- Produto cadastrado com sucesso! ---\n ');
    
def mostrarProduto():
    print('--- Produtos Cadastrados ---\n');
    if not produtoCadastrado():
        print('Nenhum produto cadastrado.\n');
    else:
        print(f"Nome: {produto['nome']}");
        print(f"Preço: R${produto['preco']}");
        print(f"Estoque: {produto['quantidade']} unidades\n");
        
def verificarEstoque():
    print('--- Estoque ---\n');
    if not produtoCadastrado():
        print('Nenhum produto cadastrado.\n');
    else:
        if produto['quantidade'] > 0:
            print(f"O estoque do produto {produto['nome']} é de {produto['quantidade']}\n");
        else:
            print(f"O produto {produto['nome']} está sem estoque\n");
def atualizarProduto():
    print('--- Atualização de Produto ---\n');
    if not produtoCadastrado():
        print('Nenhum produto cadastrado.\n');
    else:
        produto['nome'] = input('Digite o Novo Nome do Prouto: ');
        produto['preco'] = float(input('Digite o Preço Atualizado: '));
        produto['quantidade'] = int(input('Atualize a Quantidade em Estoque: '));
        print('Produto atualizado com sucesso.\n');
def menu():
    while True:
        print('1 - Cadastro de Produto');
        print('2 - Produtos Cadastrados');
        print('3 - Estoque');
        print('4 - Atualização de Produto');
        print('5 - Sair');
        
        opcao = input('\nEscolha uma opção: ');
        
        if opcao == '1':
            cadastroProduto();
        elif opcao == '2':
            mostrarProduto();
        elif opcao == '3':
            verificarEstoque();
        elif opcao == '4':
            atualizarProduto();
        elif opcao == '5':
            print('\n Até à proxima!')
            break;
        else:
            print('\n Digite uma opção valida.\n');
    
menu();