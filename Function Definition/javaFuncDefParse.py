import ply.yacc as yacc
from javaFuncDefLex import tokens

flag = 0

def p_funcDefinition(p):
    '''
    funcDefinition  : accessModifier statickw DTYPE funcname LBRACE params RBRACE LFLOWER statements RFLOWER 
                    | accessModifier DTYPE funcname LBRACE params RBRACE LFLOWER statements RFLOWER
    '''
    if len(p) == 11:
        p[0] = ('declaration',p[1],p[2],p[3],p[4],p[6],p[9])
    else:
        p[0] = ('declaration',p[1],p[2],p[3],p[5],p[8])
    
def p_accessModifier(p):
    '''
    accessModifier : PUBLIC
                   | PROTECTED
                   | PRIVATE
                   | 
    '''
    if len(p)==2:
        p[0] = ('access Modifier', p[1])
    else:
        p[0] = ('access Modifier','default')
    
def p_statickw(p):
    '''
    statickw : STATIC
    '''
    if len(p)==2:
        p[0] = (p[1],)
        
def p_funcname(p):
    '''
    funcname : ID
    '''
    
    p[0] = ('Function name',p[1])
    
def p_params(p):
    '''
    params : DTYPE ID COMMA params
           | DTYPE ID 
           |
    '''
    
    if len(p) == 3:
        p[0] = ('parameters',(p[1] , p[2]))
    elif len(p) == 1:
        p[0] = ('parameters : None',)
    else:
        p[0] = 'parameters',[(p[1],p[2])] + [p[4]]

def p_statements(p):
    '''
    statements  : statements statement
                | statement
                |
    '''
    if len(p) == 2:
        p[0] = (p[1],)
    elif len(p) == 3:
        p[0] = p[1]+(p[2],)
    else:
        p[0] = ()

def p_statement(p):
    '''
    statement   : list SEMICOLON 
    '''
    if len(p) == 3:
        p[0] = (p[1],)
    else:
        p[0] = p[1]

def p_list(p):
    '''
    list    : ID list
            | ID
            
    '''

    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]]+p[2]

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
       s = input('enter the declaration:')
   except EOFError:
       break
   if not s: 
            flag = 0
            continue
   result = parser.parse(s)
   if flag == 0:
        print("Result:", result)
        print("VALID SYNTAX")