#LEXER

import ply.lex as lex
#all tokens
tokens = ('DTYPE','ID','COMMA','EQUALS','NUMBER','CHAR',"STRING",'SEMICOLON')

#Regex for different expressions
# t_DTYPE = r'\b(int|char|double|String|boolean)'
# t_EQUALS = r'='
# t_SEMICOLON = r';'

#rule for identifiers
#keep everything in order ==> Data type -> ID -> Equals -> Number -> Semicolon
def t_DTYPE(t): 
    r'\b(int|char|double|String|boolean|float|long|short)\b'
    return t

def t_ID(t):
    r'\b[a-zA-z_][a-zA-Z0-9_]*\b' #this string will take any _ , uppercase, lowercase and digit 
    return t

def t_COMMA(t):
    r',' 
    return t

def t_EQUALS(t):
    r'='
    return t

def t_NUMBER(t):
    r'\d+'
    # t.value = int(t.value)
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