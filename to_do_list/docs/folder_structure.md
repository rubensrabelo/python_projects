# Documentação do Projeto

## Estrutura de Pastas

### to_do_list/

#### Arquivos da Pasta Principal:

- **main.py**: Este arquivo contém a lógica principal do programa.
- **README.md**: Fornece informações sobre o projeto, sua estrutura e como usá-lo.
- **requirements.txt**: Lista de dependências do Python. 
- **.gitignore**: Arquivo que especifica quais arquivos/diretórios devem ser ignorados pelo git durante a fase de versionamento.

#### Subpastas:

- **src/**
    - **__init__.py**: Marca o diretório como um pacote Python. 
    - **app/**
        - **__init__.py**: Marca o diretório como um pacote Python.
        - **task_manager.py**: Módulo principal para gerenciamento de tarefas.
        - **task.py**: Definição da classe Task.
- **utils/**
    - **__init__.py**: Marca o diretório como um pacote Python. Este pacote contém utilitários genéricos.
    - **file_handling.py**: Funções para lidar com entrada/saída de arquivos.
    - **validation.py**: Funções de validação de entrada.

- **tests/**
    - **__init__.py**: Marca o diretório como um pacote Python. Este pacote contém os testes para o projeto.
    - **test_task_manager.py**: Testes para o módulo task_manager.
    - **test_task.py**: Testes para o módulo task.
    - **test_file_handling.py**: Testes para funções de manipulação de arquivos.
    - **test_validation.py**: Testes para funções de validação.

- **docs/**
    - **folder_structure.md**: Este arquivo contém a lógica na estrutura das pastas do projeto.
     - **classes/**
        - Documentação relacionada às classes do projeto, como descrição de cada classe, métodos, atributos, etc.
    - **database/**
        - Documentação relacionada ao banco de dados, como modelo de dados, esquema do banco de dados, instruções de uso, etc.
