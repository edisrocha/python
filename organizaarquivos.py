import os
import shutil
from pathlib import Path

def organizar_arquivos(diretorio):
    extensoes = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Musicas': ['.mp3', '.wav', '.aac'],
        'Compactados': ['.zip', '.rar', '.7z'],
        'Codigos': ['.py', '.js', '.html', '.css', '.java']
    }
    
    path = Path(diretorio)
    
    for arquivo in path.iterdir():
        if arquivo.is_file():
            for pasta, exts in extensoes.items():
                if arquivo.suffix.lower() in exts:
                    pasta_destino = path / pasta
                    pasta_destino.mkdir(exist_ok=True)
                    shutil.move(str(arquivo), str(pasta_destino / arquivo.name))
                    break

# organizar_arquivos('/caminho/para/diretorio')
