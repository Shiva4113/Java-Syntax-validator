import ply.yacc as yacc

from javaCondifLex import tokens
from javaCondifLex import data

flag = 0

def p_if(p):
    '''
    if_statement    : IF LBRACE conditions RBRACE LFLOWER statements RFLOWER
                    | IF LBRACE conditions RBRACE statementSingle
    '''
    
    if len(p) == 6:
        p[0] = (p[1],p[3],p[5])
    else:
        p[0] = (p[1],p[3],p[6])

def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''
    if len(p) == 2:
        p[0] = (p[1],)
    else:
        p[0] = p[1]+(p[2],)

def p_statement(p):
    '''
    statement : list SEMICOLON
             | if_statement
             | empty
    '''
    p[0] = (p[1],) if len(p) == 2 else p[1]

def p_statementSingle(p):
    '''
    statementSingle : if_statement
                    | list SEMICOLON
                    | empty
    '''
    if len(p) == 3:
        p[0] = (p[1],)
    else:
        p[0] = p[1]

def p_list(p):
    '''
    list : ID list 
         | ID
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


def p_conditions(p):
    '''
    conditions  : ID EQUALS ID 
                | ID GREATER ID 
                | ID LESSER ID 
                | ID GREATER EQUALS ID 
                | ID LESSER EQUALS ID 
                | ID NOT EQUALS ID
                | conditions AND conditions 
                | conditions OR conditions
                | ID
    '''
    
    if len(p) == 2:
        p[0] = ('condition',p[1])
    else:
        p[0] = ('condition',(p[1],p[2],p[3]))
    
def p_error(p):
    print("Syntax error")
    global flag
    flag = 1


#From here, just copy paste and change the input statement for every other construct
#Don't forget to globally declare flag and also make flag 1 at error 
parser = yacc.yacc()
while True:
   flag = 0
   try:
       s = input('enter the conditional statement:')
   except EOFError:
       break
   if not s: 
            flag = 0
            continue
   result = parser.parse(s)
   if flag == 0:
        print("Valid syntax")
        print("Result:", result)
