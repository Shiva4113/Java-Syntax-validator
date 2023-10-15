import ply.yacc as yacc
#importing tokens
from javaCondifLex import tokens
from javaCondifLex import data
def p_if(p):
    '''
    if_statement : IF LB condition RB LF statements RF
    '''
    p[0] = ('if',p[3],p[6])#p[0] = if_statement, p[3] = condition, p[6] = statements

def p_statements(p):
    '''
    statements : ID | empty
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = []


    p[0] = p[1] #statements = ID

def p_conditions(p):
    '''
    conditions : ID
    '''
    p[0] = p[1] #conditions = ID

def p_empty(p):
    '''empty:'''
    pass
def p_error(p):
    print("Syntax error")
    

parser = yacc.yacc()
result = parser.parse(data)
print(result)