import argparse
from personalizador import layout, painel, progresso, estilo

modulos = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

funcoes = {
    "layout": ["titulo", "centralizar", "alinhado_esquerda"],
    "painel": ["painel_simples", "painel_estilizado", "painel_titulo"],
    "progresso": ["progresso_simples", "progresso_longo"],
    "estilo": ["em_negrito", "italico", "italico_bold", "markdown"]
}

parser = argparse.ArgumentParser(description="Utilitário para formatar texto com rich.")
parser.add_argument("texto", help="Texto ou caminho para arquivo")
parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento é um arquivo")
parser.add_argument("-m", "--modulo", required=True, choices=modulos.keys(), help="Escolha o módulo: layout, painel, progresso, estilo")
parser.add_argument("-f", "--funcao", required=True, help="Função disponível no módulo selecionado")
parser.add_argument("-t", "--titulo", help="Título personalizado para painéis ou outras funções que suportam")

args = parser.parse_args()

if args.funcao not in funcoes[args.modulo]:
    print(f"Função inválida. Opções para {args.modulo}: {funcoes[args.modulo]}")
else:
    func = getattr(modulos[args.modulo], args.funcao)
    if hasattr(func, '__code__') and 'titulo' in func.__code__.co_varnames:
        func(args.texto, args.arquivo, args.titulo)
    else:
        func(args.texto, args.arquivo)
