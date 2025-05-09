# 🔐 Gerador de Senhas Seguras

Um gerador de senhas seguro e personalizável desenvolvido em Python, que permite criar senhas fortes com diferentes níveis de complexidade e mantém um histórico das senhas geradas.

## ✨ Funcionalidades

- Geração de senhas personalizáveis
- Opções de personalização:
  - Tamanho da senha (8-32 caracteres)
  - Inclusão de letras maiúsculas
  - Inclusão de números
  - Inclusão de símbolos especiais
- Histórico de senhas geradas
- Salvamento automático do histórico em arquivo JSON
- Interface via linha de comando (CLI)

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Bibliotecas padrão:
  - `random`: Para geração de números aleatórios
  - `string`: Para manipulação de strings
  - `json`: Para salvar o histórico
  - `pathlib`: Para manipulação de caminhos de arquivo
  - `datetime`: Para registro de data e hora

## 📋 Pré-requisitos

- Python 3.x instalado
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão do Python)

## 🚀 Como Usar

1. Clone o repositório ou baixe o arquivo `gerador_senhas.py`
2. Execute o script:
   ```bash
   python gerador_senhas.py
   ```
3. Siga as instruções no menu:
   - Opção 1: Gerar nova senha
   - Opção 2: Ver histórico de senhas
   - Opção 3: Sair

## 💡 Exemplo de Uso

```
=== Gerador de Senhas Seguras ===
1. Gerar nova senha
2. Ver histórico de senhas
3. Sair

Escolha uma opção (1-3): 1
Tamanho da senha (8-32): 12
Usar letras maiúsculas? (s/n): s
Usar números? (s/n): s
Usar símbolos? (s/n): s

Sua senha gerada é: Kj#9mP$2nL5v
```

## 📁 Estrutura do Projeto

```
projeto_003_gerador_senhas/
├── gerador_senhas.py    # Script principal
├── historico_senhas.json # Arquivo de histórico (gerado automaticamente)
└── README.md           # Este arquivo
```

## 🔒 Segurança

- O programa garante que a senha gerada contenha pelo menos um caractere de cada tipo selecionado
- Usa o módulo `random` para geração de números verdadeiramente aleatórios
- O histórico é salvo localmente em formato JSON
- Não há conexão com internet ou serviços externos

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✍️ Autor

Douglas Rodrigues

---
Feito com ❤️ e Python 🐍 