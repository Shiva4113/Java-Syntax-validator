import ply.lex as lex
import ply.yacc as yacc

# Define the list of Java reserved keywords
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
}

# List of token names
tokens = [
    'ID', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON',
    'EQUALS', 'LESSTHAN', 'GREATERTHAN', 'NOT',
] + list(reserved.values())

# Regular expression rules for tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_EQUALS = r'=='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_NOT = r'!'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved keywords
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Define the grammar for Java if-statements
def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE
    '''
    p[0] = 'Valid Java if-statement'

def p_expression(p):
    '''
    expression : expression EQUALS expression
               | expression LESSTHAN expression
               | expression GREATERTHAN expression
               | NOT expression
               | ID
    '''
    p[0] = 'Valid Java expression'

def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''
    p[0] = 'Valid Java statements'

def p_statement(p):
    '''
    statement : if_statement
              | ID SEMICOLON
    '''
    p[0] = 'Valid Java statement'

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

# Example Java if-statement
java_code = '''
if (x == 5) {
    y = 10;
}
'''

result = parser.parse(java_code)
print(result)
