import random
import string
import json
from pathlib import Path
from datetime import datetime

class GeradorSenhas:
    def __init__(self):
        self.letras_minusculas = string.ascii_lowercase
        self.letras_maiusculas = string.ascii_uppercase
        self.numeros = string.digits
        self.simbolos = "!@#$%&*()_+-=[]{}|;:,.<>?"
        self.historico = []
        self.arquivo_historico = Path("historico_senhas.json")

    def gerar_senha(self, tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
        # Começa com letras minúsculas para garantir que sempre terá pelo menos uma
        caracteres = self.letras_minusculas
        
        if usar_maiusculas:
            caracteres += self.letras_maiusculas
        if usar_numeros:
            caracteres += self.numeros
        if usar_simbolos:
            caracteres += self.simbolos

        # Gera a senha
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        
        # Garante que a senha tem pelo menos um caractere de cada tipo selecionado
        if usar_maiusculas and not any(c in self.letras_maiusculas for c in senha):
            senha = senha[:-1] + random.choice(self.letras_maiusculas)
        if usar_numeros and not any(c in self.numeros for c in senha):
            senha = senha[:-1] + random.choice(self.numeros)
        if usar_simbolos and not any(c in self.simbolos for c in senha):
            senha = senha[:-1] + random.choice(self.simbolos)

        # Salva no histórico
        self.salvar_no_historico(senha)
        
        return senha

    def salvar_no_historico(self, senha):
        registro = {
            "senha": senha,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.historico.append(registro)
        self.salvar_historico()

    def salvar_historico(self):
        with open(self.arquivo_historico, 'w', encoding='utf-8') as f:
            json.dump(self.historico, f, ensure_ascii=False, indent=4)

    def carregar_historico(self):
        if self.arquivo_historico.exists():
            with open(self.arquivo_historico, 'r', encoding='utf-8') as f:
                self.historico = json.load(f)

def main():
    gerador = GeradorSenhas()
    gerador.carregar_historico()

    while True:
        print("\n=== Gerador de Senhas Seguras ===")
        print("1. Gerar nova senha")
        print("2. Ver histórico de senhas")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção (1-3): ")

        if opcao == "1":
            try:
                tamanho = int(input("Tamanho da senha (8-32): "))
                tamanho = max(8, min(32, tamanho))  # Limita entre 8 e 32
                
                usar_maiusculas = input("Usar letras maiúsculas? (s/n): ").lower() == 's'
                usar_numeros = input("Usar números? (s/n): ").lower() == 's'
                usar_simbolos = input("Usar símbolos? (s/n): ").lower() == 's'

                senha = gerador.gerar_senha(
                    tamanho=tamanho,
                    usar_maiusculas=usar_maiusculas,
                    usar_numeros=usar_numeros,
                    usar_simbolos=usar_simbolos
                )
                
                print(f"\nSua senha gerada é: {senha}")
                
            except ValueError:
                print("Por favor, digite um número válido para o tamanho da senha.")

        elif opcao == "2":
            if not gerador.historico:
                print("\nNenhuma senha no histórico.")
            else:
                print("\n=== Histórico de Senhas ===")
                for registro in gerador.historico:
                    print(f"Data: {registro['data']}")
                    print(f"Senha: {registro['senha']}")
                    print("-" * 30)

        elif opcao == "3":
            print("\nObrigado por usar o Gerador de Senhas!")
            break

        else:
            print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main() 