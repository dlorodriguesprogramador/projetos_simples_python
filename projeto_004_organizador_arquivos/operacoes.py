import os
import shutil
import logging
from datetime import datetime
from pathlib import Path
from config import EXTENSOES, LOG_ARQUIVO, BACKUP_DIR

# Configuração do logging
logging.basicConfig(
    filename=LOG_ARQUIVO,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def obter_categoria_arquivo(arquivo):
    """Retorna a categoria do arquivo baseado em sua extensão."""
    extensao = arquivo.suffix.lower()
    for categoria, extensoes in EXTENSOES.items():
        if extensao in extensoes:
            return categoria
    return 'outros'

def criar_pastas_categorias(diretorio):
    """Cria as pastas para cada categoria no diretório especificado."""
    for categoria in EXTENSOES.keys():
        pasta = diretorio / categoria
        if not pasta.exists():
            pasta.mkdir()
            logging.info(f"Pasta criada: {pasta}")

def organizar_arquivos(diretorio):
    """Organiza os arquivos em pastas por categoria."""
    diretorio = Path(diretorio)
    criar_pastas_categorias(diretorio)
    
    for arquivo in diretorio.iterdir():
        if arquivo.is_file() and arquivo.name != 'Thumbs.db':
            categoria = obter_categoria_arquivo(arquivo)
            destino = diretorio / categoria / arquivo.name
            
            try:
                shutil.move(str(arquivo), str(destino))
                logging.info(f"Arquivo movido: {arquivo.name} -> {categoria}")
            except Exception as e:
                logging.error(f"Erro ao mover {arquivo.name}: {str(e)}")

def renomear_arquivos(diretorio, prefixo='', sufixo='', substituir=None):
    """Renomeia arquivos em lote com prefixo, sufixo ou substituição."""
    diretorio = Path(diretorio)
    
    for arquivo in diretorio.iterdir():
        if arquivo.is_file():
            novo_nome = arquivo.stem
            
            if substituir:
                novo_nome = novo_nome.replace(substituir[0], substituir[1])
            
            novo_nome = f"{prefixo}{novo_nome}{sufixo}{arquivo.suffix}"
            novo_caminho = arquivo.parent / novo_nome
            
            try:
                arquivo.rename(novo_caminho)
                logging.info(f"Arquivo renomeado: {arquivo.name} -> {novo_nome}")
            except Exception as e:
                logging.error(f"Erro ao renomear {arquivo.name}: {str(e)}")

def fazer_backup(diretorio):
    """Cria um backup do diretório antes de operações importantes."""
    diretorio = Path(diretorio)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_nome = f"backup_{timestamp}"
    backup_caminho = BACKUP_DIR / backup_nome
    
    try:
        shutil.copytree(diretorio, backup_caminho)
        logging.info(f"Backup criado: {backup_caminho}")
        return True
    except Exception as e:
        logging.error(f"Erro ao criar backup: {str(e)}")
        return False

def listar_arquivos(diretorio):
    """Lista todos os arquivos no diretório e suas categorias."""
    diretorio = Path(diretorio)
    arquivos = []
    
    for arquivo in diretorio.iterdir():
        if arquivo.is_file():
            categoria = obter_categoria_arquivo(arquivo)
            arquivos.append({
                'nome': arquivo.name,
                'categoria': categoria,
                'tamanho': arquivo.stat().st_size,
                'data_modificacao': datetime.fromtimestamp(arquivo.stat().st_mtime)
            })
    
    return arquivos
