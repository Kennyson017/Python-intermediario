"""
Módulo layout - funcionalidades de layout usando rich.
"""
from rich.console import Console
from rich.text import Text

console = Console()

def titulo(texto: str, isArquivo: bool = False):
    """Exibe o texto como título em destaque."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.rule(Text(texto, style="bold purple"))

def centralizar(texto: str, isArquivo: bool = False):
    """Centraliza o texto na saída do terminal."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(texto, justify="center")

def alinhado_esquerda(texto: str, isArquivo: bool = False):
    """Centraliza o texto na saída do terminal."""
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(texto, justify="left")
