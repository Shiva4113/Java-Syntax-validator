import ply.yacc as yacc

from javaVarDecLex import tokens

flag = 0

def p_declaration(p):
    '''
    declaration : DTYPE list SEMICOLON     
    '''
    p[0] = ('declaration',p[1],p[2])

def p_list(p):
     '''
     list : ID COMMA list 
          | ID
     '''
     if len(p) == 2:
          p[0] = [p[1]]
     else:
          p[0] = [p[1]] + p[3]
 
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