import ply.lex as lex

tokens = ('IF','LBRACE','LESSER','GREATER','EQUALS','NOT','RBRACE','LFLOWER','SEMICOLON','RFLOWER','ID')

def t_IF(t):
    r'if'
    return t

t_LBRACE = r'\('
t_RBRACE = r'\)'
t_LFLOWER = r'\{'
t_RFLOWER = r'\}'

def t_ID(t):
    r'\w+'
    return t

t_LESSER = r'<'
t_GREATER = r'>'
t_EQUALS = r'==|='
t_NOT = r'!'
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character found '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = input()

lexer.input(data)

while(1):
    tok = lexer.token()
    if not tok:
        break
    print(tok)