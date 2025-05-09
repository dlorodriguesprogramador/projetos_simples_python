# 🌐 Web Scraping de Citações

Um script Python que realiza web scraping do site [Quotes to Scrape](https://quotes.toscrape.com/), extraindo citações famosas e suas informações.

## ✨ Funcionalidades

- Extração de citações de um site web
- Uso de bibliotecas populares de web scraping
- Processamento de HTML para extrair dados específicos
- Saída formatada das citações encontradas

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Bibliotecas externas:
  - `requests`: Para fazer requisições HTTP
  - `beautifulsoup4`: Para parsing e extração de dados HTML

## 📋 Pré-requisitos

- Python 3.x instalado
- Bibliotecas necessárias:
  ```bash
  pip install requests beautifulsoup4
  ```

## 🚀 Como Usar

1. Clone o repositório ou baixe o arquivo `web_scraping.py`
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script:
   ```bash
   python web_scraping.py
   ```

## 💡 Exemplo de Saída

```
"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking."
"It is our choices that show what we truly are, far more than our abilities."
"There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle."
```

## 📁 Estrutura do Projeto

```
projeto_002_web_scraping/
├── web_scraping.py    # Script principal
├── requirements.txt   # Dependências do projeto
└── README.md         # Este arquivo
```

## 🔍 Como Funciona

1. O script faz uma requisição HTTP para o site Quotes to Scrape
2. Utiliza BeautifulSoup para fazer o parsing do HTML
3. Localiza todos os elementos `<span>` com o atributo `itemprop="text"`
4. Extrai e imprime o texto de cada citação encontrada

## ⚠️ Considerações Éticas

- Respeite os termos de uso do site
- Não faça requisições em excesso
- Considere adicionar delays entre as requisições
- Verifique se o site permite web scraping

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✍️ Autor

Douglas Rodrigues

---
Feito com ❤️ e Python 🐍