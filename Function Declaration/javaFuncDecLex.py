import ply.lex as lex

tokens = ('DTYPE',
          'ID',
          'LBRACE',
          'RBRACE',
          'COMMA',
          'SEMICOLON',
          'STATIC',
          'PUBLIC',
          'PROTECTED',
          'PRIVATE')

def t_PUBLIC(t):
    r'public'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_DTYPE(t): 
    r'\b(int|char|double|void|String|boolean|float|long|short|void)\b'
    return t

def t_ID(t):
    r'\b[a-zA-Z_][a-zA-Z0-9_]*\b' 
    return t

t_LBRACE = r'\('
t_RBRACE = r'\)'

def t_COMMA(t):
    r','
    return t

def t_SEMICOLON(t):
    r';'
    return t

t_ignore = ' \t' #to ignore all the spaces and tabs in the regex

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