import ply.lex as lex

#do{statemnets}while();
tokens = (
        'DO',
        'LFLOWER',
        'RFLOWER',
        'WHILE',
        'LBRACE',
        'LESSER',
        'GREATER',
        'NOT',
        'AND',
        'OR',
        'EQUALS',
        'RBRACE',
        'SEMICOLON',
        'ID',
)

def t_DO(t):
    r'do'
    return t

def t_WHILE(t):
    r'while'
    return t

t_LBRACE = r'\('
t_RBRACE = r'\)'
t_LFLOWER = r'\{'
t_RFLOWER = r'\}'

def t_ID(t):
    r'\b([a-zA-Z_][a-zA-Z_0-9]*)\b |\b(\d+)\b'
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

data = input()

lexer.input(data)

while(1):
    tok = lexer.token()
    if not tok:
        break
    print(tok)