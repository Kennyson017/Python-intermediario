"""
Módulo painel - funcionalidades de painel usando rich.
"""
from rich.panel import Panel
from rich.console import Console
from rich import box

console = Console()

def painel_simples(texto: str, isArquivo: bool = False):
    """Exibe o texto dentro de um painel simples."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(Panel(texto))

def painel_estilizado(texto: str, isArquivo: bool = False):
    """Exibe o texto dentro de um painel com estilo personalizado."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(Panel(texto, title="Painel", border_style="blue"))

def painel_titulo(texto: str, isArquivo: bool = False, titulo: str = None):
    """Exibe o texto dentro de um painel com estilo e titulo personalizado."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    
    titulo_final = titulo if titulo else "Painel"
    console.print(Panel(
        texto,
        title=titulo_final,
        border_style="blue",
        box=box.HEAVY
        ))
