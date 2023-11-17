from ply.lex import lex
import sys

__all__ = ["lexer", "tokens", "tokenize"]

# Lista de tokens reconocibles por el lexer
# TODO: Agregar tokens faltantes
# tokens = ['PLUS', 'STAR', 'MINUS', 'DIV', 'POPEN', 'PCLOSE', 'NUM']
tokens = ['PLUS', 'STAR', 'UNI', 'ID', 'OPT', 'OPEN', 'CLOSE', 'NUM', 'COMMA', 'POPEN', 'PCLOSE']

# Reglas para el analizador léxico

# Ignoramos espacios y tabulaciones
t_ignore = ' \t'

# Regexes para reconocer tokens simples
# TODO: Definir regexes y/o funciones para los tokens faltantes
t_PLUS = r'\+'
t_STAR = r'\*'
t_UNI = r'\|'
t_OPT = r'\?'
t_POPEN = r'\('
t_PCLOSE = r'\)'
t_OPEN = r'\{'
t_CLOSE = r'\}'
t_COMMA = r'\,'
t_NUM = r'[0-9]+'
t_ID = r'[a-zA-Z]'

# Ignoramos saltos de línea y llevamos registro del número de línea actual
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


# Manejo básico de errores: omitimos caracteres extraños
def t_error(t):
    print(
        f'Ignoring illegal character {t.value[0]!r} at position {t.lexpos}', file=sys.stderr)
    t.lexer.skip(1)


# Construimos el lexer
lexer = lex()


# Aplicamos el lexer e imprimimos una lista de tokens
def tokenize_and_print(string):
    lexer.input(string)
    print(list(map(lambda token: (token.type, token.value), lexer)))
