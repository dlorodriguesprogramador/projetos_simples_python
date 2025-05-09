# 🎮 Jogo de Adivinhação

Um jogo simples de adivinhação desenvolvido em Python, onde o jogador precisa descobrir um número aleatório entre 1 e 10 em até 3 tentativas.

## ✨ Funcionalidades

- Geração aleatória de número entre 1 e 10
- Sistema de vidas (3 tentativas)
- Dicas se o número é maior ou menor que o palpite
- Interface via linha de comando (CLI)
- Feedback imediato após cada tentativa

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Bibliotecas padrão:
  - `random`: Para geração do número aleatório

## 📋 Pré-requisitos

- Python 3.x instalado
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão do Python)

## 🚀 Como Jogar

1. Clone o repositório ou baixe o arquivo `adivinha.py`
2. Execute o script:
   ```bash
   python adivinha.py
   ```
3. Digite um número entre 1 e 10
4. Siga as dicas para tentar adivinhar o número correto
5. Você tem 3 tentativas para acertar

## 💡 Exemplo de Jogo

```
Digite um número: 5
O número sorteado é maior que o chute.

Digite um número: 8
O número sorteado é menor que o chute.

Digite um número: 7
Você acertou!
```

## 📁 Estrutura do Projeto

```
projeto_001_adivinha/
├── adivinha.py    # Script principal do jogo
└── README.md      # Este arquivo
```

## 🎯 Regras do Jogo

1. O computador escolhe um número aleatório entre 1 e 10
2. O jogador tem 3 tentativas para adivinhar o número
3. Após cada tentativa, o jogo informa se o número é maior ou menor
4. O jogo termina quando:
   - O jogador acerta o número
   - O jogador perde todas as tentativas

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✍️ Autor

Douglas Rodrigues

---
Feito com ❤️ e Python 🐍 