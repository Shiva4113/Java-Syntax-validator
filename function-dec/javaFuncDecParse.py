import ply.yacc as yacc
from javaFuncDecLex import tokens

flag = 0

def p_funcDeclaration(p):
    '''
    funcDeclaration : accessModifier statickw DTYPE funcname LBRACE params RBRACE SEMICOLON     
    '''
    p[0] = ('declaration',p[1],p[2])
    
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
             |
    '''
    if len(p)==2:
        p[0] = (p[1],)
    else:
        p[0] = ('notstatic',)
        
def p_funcname(p):
    '''
    funcname : ID
    '''
    
    p[0] = (p[1],)
    
def p_params(p):
    '''
    params : DTYPE ID COMMA params
           | DTYPE ID 
           |
    '''
    
    if len(p) == 3:
        p[0] = (p[1] , p[2])
    elif len(p) == 1:
        p[0] = tuple()
    else:
        p[0] = [(p[1],p[2])] + [p[4]]
        
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