"""
Módulo progresso - funcionalidades de barra de progresso usando rich.
"""
from rich.progress import track
import time
def progresso_simples(texto: str, isArquivo: bool = False):
    """Simula progresso com texto exibido após conclusão."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    for _ in track(range(10), description="Processando..."):
        time.sleep(0.1)
    print(texto)
def progresso_longo(texto: str, isArquivo: bool = False):
    """Simula uma tarefa longa com barra de progresso."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    for _ in track(range(30), description="Executando..."):
        time.sleep(0.05)
    print(texto)
