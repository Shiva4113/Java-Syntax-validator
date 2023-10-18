import ply.lex as lex

#defining tokens  --> while(condition){statements}
tokens = ('WHILE','LBRACE','LESSER','GREATER','NOT','AND','OR','EQUALS','RBRACE','LFLOWER','RFLOWER','SEMICOLON','ID')

def t_WHILE(t):
    r'while'
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
t_EQUALS = r'=(=)?'
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character found {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

data = '''while(a>b){}'''

lexer.input(data)

while(1):
    tok = lexer.token()
    if not tok:
        break
    print(tok)