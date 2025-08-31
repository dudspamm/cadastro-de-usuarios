# Sistema de Cadastro de Funcionários em Python 🧑‍💻

![Status do Projeto](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 📝 Descrição
Este projeto consiste em um sistema completo de cadastro de funcionários (CRUD) que roda diretamente no terminal. Desenvolvido em Python, o programa oferece uma interface de linha de comando (CLI) para que o usuário possa criar, ler e deletar registros de funcionários. Os dados são salvos permanentemente em um arquivo JSON, garantindo que as informações não sejam perdidas entre as sessões de uso.

## ✨ Funcionalidades Principais
- **✅ Cadastrar Funcionário:** Permite adicionar novos funcionários com nome e cargo. O sistema atribui um ID único e sequencial para cada novo registro.
- **📄 Listar Funcionários:** Exibe na tela uma lista formatada com o ID, nome e cargo de todos os funcionários cadastrados.
- **❌ Remover Funcionário:** Permite ao usuário remover um funcionário existente através do seu ID.
- **💾 Persistência de Dados com JSON:** Todas as alterações (criação e remoção) são salvas em tempo real no arquivo `funcionarios.json`, garantindo a integridade dos dados.
- **🔢 Gerenciamento de IDs:** O sistema calcula automaticamente o próximo ID disponível, mesmo após múltiplas sessões e remoções.
- **🛡️ Tratamento de Erros:** Inclui validações para entradas de usuário vazias, IDs não encontrados e arquivos JSON vazios ou corrompidos.

## 💻 Tecnologias Utilizadas
* ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🚀 Como Executar o Projeto
Para rodar este projeto, você precisará ter o Python 3 instalado em sua máquina.

1. Clone este repositório para o seu computador:
   ```bash
   git clone [https://github.com/dudspamm/Cadastro-de-usuarios.git](https://github.com/dudspamm/Cadastro-de-usuarios.git)
