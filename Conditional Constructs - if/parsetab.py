
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ELSE EQUALS GREATER ID IF LBRACE LESSER LFLOWER NOT OR RBRACE RFLOWER SEMICOLON\n    if_statement    : IF LBRACE conditions RBRACE LFLOWER statements RFLOWER\n                    | IF LBRACE conditions RBRACE statementSingle\n    \n    statements : statements statement\n               | statement\n    \n    statement : list SEMICOLON\n             | if_statement\n             | empty\n    \n    statementSingle : if_statement\n                    | list SEMICOLON\n                    | empty\n    \n    list : ID list \n         | ID\n    \n    empty :\n    \n    conditions  : ID EQUALS ID \n                | ID GREATER ID \n                | ID LESSER ID \n                | ID GREATER EQUALS ID \n                | ID LESSER EQUALS ID \n                | ID NOT EQUALS ID\n                | conditions AND conditions \n                | conditions OR conditions\n                | ID\n    '
    
_lr_action_items = {'IF':([0,6,13,14,15,17,27,28,30,31,32,37,38,39,],[2,2,2,-2,-8,-10,2,-4,-6,-7,-9,-1,-3,-5,]),'$end':([1,6,14,15,17,32,37,],[0,-13,-2,-8,-10,-9,-1,]),'LBRACE':([2,],[3,]),'ID':([3,6,7,8,9,10,11,13,14,15,17,18,23,25,26,27,28,30,31,32,37,38,39,],[5,18,5,5,21,22,24,18,-2,-8,-10,18,34,35,36,18,-4,-6,-7,-9,-1,-3,-5,]),'RBRACE':([4,5,19,20,21,22,24,34,35,36,],[6,-22,-20,-21,-14,-15,-16,-17,-18,-19,]),'AND':([4,5,19,20,21,22,24,34,35,36,],[7,-22,7,7,-14,-15,-16,-17,-18,-19,]),'OR':([4,5,19,20,21,22,24,34,35,36,],[8,-22,8,8,-14,-15,-16,-17,-18,-19,]),'EQUALS':([5,10,11,12,],[9,23,25,26,]),'GREATER':([5,],[10,]),'LESSER':([5,],[11,]),'NOT':([5,],[12,]),'LFLOWER':([6,],[13,]),'RFLOWER':([6,13,14,15,17,27,28,30,31,32,37,38,39,],[-13,-13,-2,-8,-10,37,-4,-6,-7,-9,-1,-3,-5,]),'SEMICOLON':([16,18,29,33,],[32,-12,39,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'if_statement':([0,6,13,27,],[1,15,30,30,]),'conditions':([3,7,8,],[4,19,20,]),'statementSingle':([6,],[14,]),'list':([6,13,18,27,],[16,29,33,29,]),'empty':([6,13,27,],[17,31,31,]),'statements':([13,],[27,]),'statement':([13,27,],[28,38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> if_statement","S'",1,None,None,None),
  ('if_statement -> IF LBRACE conditions RBRACE LFLOWER statements RFLOWER','if_statement',7,'p_if','javaCondifParse.py',10),
  ('if_statement -> IF LBRACE conditions RBRACE statementSingle','if_statement',5,'p_if','javaCondifParse.py',11),
  ('statements -> statements statement','statements',2,'p_statements','javaCondifParse.py',17),
  ('statements -> statement','statements',1,'p_statements','javaCondifParse.py',18),
  ('statement -> list SEMICOLON','statement',2,'p_statement','javaCondifParse.py',27),
  ('statement -> if_statement','statement',1,'p_statement','javaCondifParse.py',28),
  ('statement -> empty','statement',1,'p_statement','javaCondifParse.py',29),
  ('statementSingle -> if_statement','statementSingle',1,'p_statementSingle','javaCondifParse.py',35),
  ('statementSingle -> list SEMICOLON','statementSingle',2,'p_statementSingle','javaCondifParse.py',36),
  ('statementSingle -> empty','statementSingle',1,'p_statementSingle','javaCondifParse.py',37),
  ('list -> ID list','list',2,'p_list','javaCondifParse.py',43),
  ('list -> ID','list',1,'p_list','javaCondifParse.py',44),
  ('empty -> <empty>','empty',0,'p_empty','javaCondifParse.py',53),
  ('conditions -> ID EQUALS ID','conditions',3,'p_conditions','javaCondifParse.py',60),
  ('conditions -> ID GREATER ID','conditions',3,'p_conditions','javaCondifParse.py',61),
  ('conditions -> ID LESSER ID','conditions',3,'p_conditions','javaCondifParse.py',62),
  ('conditions -> ID GREATER EQUALS ID','conditions',4,'p_conditions','javaCondifParse.py',63),
  ('conditions -> ID LESSER EQUALS ID','conditions',4,'p_conditions','javaCondifParse.py',64),
  ('conditions -> ID NOT EQUALS ID','conditions',4,'p_conditions','javaCondifParse.py',65),
  ('conditions -> conditions AND conditions','conditions',3,'p_conditions','javaCondifParse.py',66),
  ('conditions -> conditions OR conditions','conditions',3,'p_conditions','javaCondifParse.py',67),
  ('conditions -> ID','conditions',1,'p_conditions','javaCondifParse.py',68),
]
