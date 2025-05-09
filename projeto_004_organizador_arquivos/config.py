from pathlib import Path

# Diretório base do projeto
BASE_DIR = Path(__file__).parent

# Diretórios para logs e backups
LOGS_DIR = BASE_DIR / 'logs'
BACKUP_DIR = BASE_DIR / 'backups'

# Arquivo de log
LOG_ARQUIVO = LOGS_DIR / 'operacoes.log'

# Criação dos diretórios necessários
LOGS_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)

# Categorias e extensões de arquivos
EXTENSOES = {
    'imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
    'documentos': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
    'planilhas': ['.xls', '.xlsx', '.csv', '.ods'],
    'apresentacoes': ['.ppt', '.pptx', '.odp'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'audios': ['.mp3', '.wav', '.ogg', '.flac', '.m4a'],
    'compactados': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'programas': ['.exe', '.msi', '.bat', '.sh'],
    'codigo': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h'],
    'outros': []  # Arquivos que não se encaixam nas categorias acima
} 