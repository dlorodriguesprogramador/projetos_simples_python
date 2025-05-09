# Organizador de Arquivos

Um programa em Python para organizar e gerenciar arquivos em seu computador.

## Funcionalidades

- Organização automática de arquivos por categoria
- Renomeação em lote de arquivos
- Listagem detalhada de arquivos
- Sistema de backup automático
- Log de operações

## Requisitos

- Python 3.6 ou superior
- Bibliotecas padrão do Python (não são necessárias instalações adicionais)

## Como Usar

1. Clone ou baixe este repositório
2. Navegue até a pasta do projeto
3. Execute o programa:
   ```
   python main.py
   ```

## Menu Principal

1. **Organizar arquivos por categoria**
   - Organiza automaticamente os arquivos em pastas baseadas em suas extensões
   - Cria um backup antes da operação

2. **Renomear arquivos em lote**
   - Adicionar prefixo aos arquivos
   - Adicionar sufixo aos arquivos
   - Substituir texto nos nomes dos arquivos

3. **Listar arquivos**
   - Mostra informações detalhadas sobre os arquivos
   - Inclui nome, categoria, tamanho e data de modificação

4. **Sair**
   - Encerra o programa

## Estrutura do Projeto

```
projeto_004_organizador_arquivos/
├── main.py           # Interface principal do programa
├── operacoes.py      # Funções de manipulação de arquivos
├── config.py         # Configurações e constantes
└── README.md         # Este arquivo
```

## Logs e Backups

- Os logs são salvos em `logs/operacoes.log`
- Os backups são salvos em `backups/`
- Cada backup é nomeado com timestamp para fácil identificação

## Contribuindo

Sinta-se à vontade para contribuir com melhorias através de pull requests.

## Licença

Este projeto está sob a licença MIT.
