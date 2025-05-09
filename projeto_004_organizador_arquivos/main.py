import os
import sys
from pathlib import Path
from operacoes import (
    organizar_arquivos,
    renomear_arquivos,
    fazer_backup,
    listar_arquivos
)

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    """Exibe o menu principal do programa."""
    print("\n=== Organizador de Arquivos ===")
    print("1. Organizar arquivos por categoria")
    print("2. Renomear arquivos em lote")
    print("3. Listar arquivos")
    print("4. Sair")
    return input("\nEscolha uma opção: ")

def obter_diretorio():
    """Solicita e valida o diretório de trabalho."""
    while True:
        diretorio = input("\nDigite o caminho do diretório: ").strip()
        if os.path.isdir(diretorio):
            return diretorio
        print("Diretório inválido! Tente novamente.")

def menu_renomear():
    """Exibe o menu de renomeação de arquivos."""
    print("\n=== Renomear Arquivos ===")
    print("1. Adicionar prefixo")
    print("2. Adicionar sufixo")
    print("3. Substituir texto")
    print("4. Voltar")
    return input("\nEscolha uma opção: ")

def main():
    """Função principal do programa."""
    while True:
        limpar_tela()
        opcao = exibir_menu()
        
        if opcao == '1':
            diretorio = obter_diretorio()
            if fazer_backup(diretorio):
                organizar_arquivos(diretorio)
                print("\nArquivos organizados com sucesso!")
            else:
                print("\nErro ao criar backup. Operação cancelada.")
            
        elif opcao == '2':
            diretorio = obter_diretorio()
            opcao_renomear = menu_renomear()
            
            if opcao_renomear == '1':
                prefixo = input("\nDigite o prefixo: ")
                renomear_arquivos(diretorio, prefixo=prefixo)
            elif opcao_renomear == '2':
                sufixo = input("\nDigite o sufixo: ")
                renomear_arquivos(diretorio, sufixo=sufixo)
            elif opcao_renomear == '3':
                texto_antigo = input("\nDigite o texto a ser substituído: ")
                texto_novo = input("Digite o novo texto: ")
                renomear_arquivos(diretorio, substituir=(texto_antigo, texto_novo))
            elif opcao_renomear == '4':
                continue
            
            print("\nArquivos renomeados com sucesso!")
            
        elif opcao == '3':
            diretorio = obter_diretorio()
            arquivos = listar_arquivos(diretorio)
            
            print("\n=== Lista de Arquivos ===")
            for arquivo in arquivos:
                print(f"\nNome: {arquivo['nome']}")
                print(f"Categoria: {arquivo['categoria']}")
                print(f"Tamanho: {arquivo['tamanho']} bytes")
                print(f"Última modificação: {arquivo['data_modificacao']}")
            
            input("\nPressione Enter para continuar...")
            
        elif opcao == '4':
            print("\nSaindo do programa...")
            sys.exit(0)
        
        else:
            print("\nOpção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main() 