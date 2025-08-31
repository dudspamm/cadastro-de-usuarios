def cadastro_funcionarios(): #Define uma função que contém todo o menu e lógica de cadastro.

    funcionarios = {} #cria um dicionário vazio para armazenar os funcionários cadastrados.
    proximo_id = 1  #inicia com o valor 1, que será usada como chave (ID) única para cada funcionário cadastrado.

    while True: #Cria um loop infinito, e o programa só sai quando usar break. Isso mantém o menu ativo.
        print("=== Menu ==")
        print("1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Sair")
        print("===========")

        escolha = input("Escolha uma opção: ") #lê a entrada do usuário e armazena na variável escolha.

        match escolha: #estrutura para verificar e controlar a opção digitada.
            case '1':
                print("--- Cadastrar Funcionário ---")
                nome = input("Nome: ")
                cargo = input("Cargo: ")

                if nome and cargo:  #verifica se ambos os campos foram preenchidos (não vazios).
                    funcionarios[proximo_id] = {"nome": nome, "cargo": cargo}  #adiciona ao dicionário funcionarios uma nova entrada.
                    print(f"Funcionário '{nome}' (ID: {proximo_id}) cadastrado com sucesso!") #exibe mensagem confirmando o cadastro.
                    proximo_id += 1  #Adiciona 1 no proximo ID de cadastro de funcionário
                else:
                    print("Erro: Insira os dados corretos. Funcionário não cadastrado.") #se o usuário não preencher nome ou cargo, exibe mensagem de erro.

            case '2':
                print("--- Lista de Funcionários ---")
                if not funcionarios: #verifica se o dicionário está vazio e, se sim, informa que não há funcionários cadastrados.
                    print("Nenhum funcionário cadastrado ainda.")
                else:

                    for id_func, dados_func in funcionarios.items(): #caso existam funcionários itera sobre cada item do dicionário. Exibe o ID, nome e cargo de cada funcionário.
                        print(f"ID: {id_func}, Nome: {dados_func['nome']}, Cargo: {dados_func['cargo']}")

            case '3':
                print("Encerando sistema. Até mais!") #exibe mensagem de despedida e usa break para sair do loop.
                break

            case _:
                print("Opção inválida. Por favor, tente novamente.") #caso nenhuma opção acima seja escolhida, executa este bloco (opção inválida).


if __name__ == "__main__": #Verifica se o script está sendo executado diretamente (não importado). Se sim, chama a função principal cadastro_funcionarios()
  cadastro_funcionarios()