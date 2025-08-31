import json
import os # Usaremos o 'os' para verificar se o arquivo existe

# Nome do arquivo que vai funcionar como nosso "banco de dados"
NOME_ARQUIVO = 'funcionarios.json'

def carregar_dados():
    """Lê os dados do arquivo JSON e os retorna como um dicionário."""
    if not os.path.exists(NOME_ARQUIVO):
        return {} # Se o arquivo não existe, retorna um dicionário vazio
    
    try:
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as f:
            # json.load() lê o arquivo e transforma o JSON em um dicionário Python
            return json.load(f)
    except json.JSONDecodeError:
        # Se o arquivo estiver vazio ou corrompido, retorna um dicionário vazio
        return {}

def salvar_dados(dados):
    """Salva os dados (dicionário) no arquivo JSON."""
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        # json.dump() pega um objeto Python e o escreve no arquivo em formato JSON
        # indent=4 deixa o arquivo formatado e legível para humanos
        json.dump(dados, f, indent=4)

def cadastro_funcionarios():
    # Carrega os funcionários que já estavam salvos
    funcionarios = carregar_dados()
    
    # Calcula o próximo ID baseado no maior ID que já existe
    if funcionarios:
        # Pega todas as chaves (IDs), converte para inteiros e pega o maior. Soma 1.
        proximo_id = max(int(k) for k in funcionarios.keys()) + 1
    else:
        proximo_id = 1

    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Remover Funcionário")
        print("4. Sair")
        print("============")

        escolha = input("Escolha uma opção: ")

        match escolha:
            case '1':
                print("\n--- Cadastrar Funcionário ---")
                nome = input("Nome: ").strip()
                cargo = input("Cargo: ").strip()

                if nome and cargo:
                    # Adiciona ao dicionário. Note que proximo_id precisa ser string para ser chave de JSON
                    funcionarios[str(proximo_id)] = {"nome": nome, "cargo": cargo}
                    
                    # SALVA OS DADOS NO ARQUIVO APÓS O CADASTRO
                    salvar_dados(funcionarios)

                    print(f"Funcionário '{nome}' (ID: {proximo_id}) cadastrado com sucesso!")
                    proximo_id += 1
                else:
                    print("Erro: Insira os dados corretos. Funcionário não cadastrado.")
            
            case '2':
                print("\n--- Lista de Funcionários ---")
                # Recarrega os dados para garantir que temos a versão mais atual
                funcionarios_atualizados = carregar_dados()
                if not funcionarios_atualizados:
                    print("Nenhum funcionário cadastrado ainda.")
                else:
                    for id_func, dados_func in funcionarios_atualizados.items():
                        print(f"ID: {id_func}, Nome: {dados_func['nome']}, Cargo: {dados_func['cargo']}")

            case '3':
                print("\n--- Remover Funcionário ---")
                id_remover= input("Digite o ID do funcionário para remover: ").strip()
                # Recarrega os dados para garantir que temos a versão mais atual
                funcionarios_atualizados = carregar_dados()
                if id_remover in funcionarios_atualizados:
                    del funcionarios_atualizados[id_remover]
                    # SALVA OS DADOS NO ARQUIVO APÓS A REMOÇÃO
                    salvar_dados(funcionarios_atualizados)
                    print(f"Funcionário ID {id_remover} removido com sucesso.")
                else:
                    print(f"Erro: Funcionário ID {id_remover} não encontrado.")
            
            case '4':
                print("\nEncerrando sistema. Até mais!")
                break
            
            case _:
                print("\nOpção inválida. Por favor, tente novamente.")

# Verifica se o script está sendo executado diretamente e chama a função principal
if __name__ == "__main__":
    cadastro_funcionarios()