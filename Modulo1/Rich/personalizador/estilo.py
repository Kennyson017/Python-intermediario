"""
Módulo estilo - aplica diferentes estilos ao texto com rich.
"""
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def em_negrito(texto: str, isArquivo: bool = False):
    """Exibe o texto em negrito."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(f"[bold]{texto}[/bold]")

def italico(texto: str, isArquivo: bool = False):
    """Exibe o texto em Italico."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(f"[i]{texto}[/i]")

def italico_bold(texto: str, isArquivo: bool = False):
    """Exibe o texto em negrito e italico."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(f"{texto}", style="bold italic")

def markdown(texto: str, isArquivo: bool = False):
    """Renderiza o texto como Markdown."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(Markdown(texto))
