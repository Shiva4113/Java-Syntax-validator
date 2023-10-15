import ply.yacc as yacc
#importing tokens
import javaVarDecLex as myLexer
from javaVarDecLex import tokens

def p_declaration(p):
    '''
    declaration : DTYPE list SEMICOLON
    list        : ID COMMA list
                | ID      
    '''

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

parser.parse(myLexer.data)