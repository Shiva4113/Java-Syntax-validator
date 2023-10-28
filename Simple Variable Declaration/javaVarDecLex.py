

import ply.lex as lex

tokens = ('DTYPE',
        'ID',
        'COMMA',
        'EQUALS',
        'NUMBER',
        'CHAR',
        "STRING",
        'SEMICOLON')

def t_DTYPE(t): 
    r'\b(int|char|double|String|boolean|float|long|short)\b'
    return t

def t_ID(t):
    r'\b[a-zA-z_][a-zA-Z0-9_]*\b' 
    return t

def t_COMMA(t):
    r',' 
    return t

def t_EQUALS(t):
    r'='
    return t

def t_NUMBER(t):
    r'\d+'
    return t

def t_CHAR(t):
    r"'.'"
    t.value = t.value[1]
    return t


def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_SEMICOLON(t):
    r';'
    return t
t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character encountered {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

data = input()

lexer.input(data)

while(1):
     tok = lexer.token()
     if not tok:
         break
     print(tok)