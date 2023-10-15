import ply.yacc as yacc
#importing tokens
# from javaVarDecLex import data
from javaVarDecLex import tokens

flag = 0
def p_declaration(p):
    '''
    declaration : DTYPE list SEMICOLON
    list        : ID COMMA list
                | ID      
    '''

def p_error(p):
    print("Syntax error")
    global flag 
    flag = 1


parser = yacc.yacc()
while True:
   try:
       s = input('enter the declaration:')
   except EOFError:
       break
   if not s: 
            flag = 0
            continue
   result = parser.parse(s)
   if flag == 0:
    print("Errors = ",result)