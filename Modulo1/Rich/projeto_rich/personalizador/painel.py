"""
Módulo painel - funcionalidades de painel usando rich.
"""
from rich.panel import Panel
from rich.console import Console
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
