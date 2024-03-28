### Entidades:

1. **Usuário**
   - Atributos: ID (chave primária), Nome, Email, Senha.

2. **Tarefa**
   - Atributos: ID (chave primária), Data de Conclusão, Nome, Status (por exemplo: pendente, andamento e concluída).

### Relacionamentos:

1. **Relacionamento entre Usuário e Tarefa**
   - Um usuário pode ter várias tarefas.
   - Uma tarefa pertence a um único usuário.
   - Chave Estrangeira: O ID do usuário armazenado na tabela de Tarefas.
