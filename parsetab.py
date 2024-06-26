
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIG BRACL BRACR CADENA COMILLA CONTENIDO DIFER DIV DOUBLESTRING ENTERO ENTERO FUNCION ID ID IGIG IMPRIMIR INCR MAS MAY MAYIG MENIG MENO MENOS MULTI NUMB PARA PAREL PARER PUNTOCOMA SEMI SI SINO SIONO STRING VARIABLEinit : program\n                | opcion2\n                | opcion3\n                | opcion4\n                | funcadenaprintopcion2 : VARIABLE CADENA ID ASSIG ID\n                    | VARIABLE ENTERO ID ASSIG NUMBvar : VARIABLE ENTERO ID ASSIG NUMBopcion3 : opcion2 SI PAREL ID operando contentn PARER BRACL IMPRIMIR PAREL contentIF PARER BRACR SINO BRACL IMPRIMIR PAREL contentELSE PARER BRACRopcion4 : FUNCION ID PAREL ENTERO ID PARER BRACL opcion2 var ID ASSIG ID MAS ID BRACRfuncadenaprint : FUNCION ID PAREL CADENA ID PARER BRACL ID ASSIG ID IMPRIMIR PAREL ID PARER BRACRprogram : PARA PAREL value ID ASSIG NUMB PUNTOCOMA ID operando NUMB PUNTOCOMA ID INCR PUNTOCOMA PARER BRACL IMPRIMIR PAREL content PARER BRACRvalue : CADENA\n                    | ENTEROcontent : CONTENIDO\n                     | IDcontentIF : CONTENIDO\n                     | IDcontentELSE : CONTENIDO\n                     | IDoperando : MAY\n                    | MAYIG\n                    | MENIG\n                    | IGIG\n                    | MENO\n                    | DIFER\n                    | ASSIGcontentn : ID  \n                 | NUMB'
    
_lr_action_items = {'PARA':([0,],[7,]),'VARIABLE':([0,37,38,49,53,],[8,-6,-7,8,58,]),'FUNCION':([0,],[9,]),'$end':([1,2,3,4,5,6,37,38,88,89,102,104,],[0,-1,-2,-3,-4,-5,-6,-7,-10,-11,-9,-12,]),'SI':([3,37,38,],[10,-6,-7,]),'PAREL':([7,10,14,55,71,90,93,],[11,15,21,60,76,92,97,]),'CADENA':([8,11,21,],[12,17,27,]),'ENTERO':([8,11,21,58,],[13,18,26,63,]),'ID':([9,12,13,15,16,17,18,24,26,27,28,29,30,31,32,33,34,35,48,50,57,59,60,63,68,69,76,79,80,92,97,],[14,19,20,22,23,-13,-14,37,39,40,41,-21,-22,-23,-24,-25,-26,-27,52,54,62,64,65,70,73,74,81,84,-8,94,99,]),'ASSIG':([19,20,22,23,52,54,62,70,],[24,25,35,36,35,59,69,75,]),'MAY':([22,52,],[29,29,]),'MAYIG':([22,52,],[30,30,]),'MENIG':([22,52,],[31,31,]),'IGIG':([22,52,],[32,32,]),'MENO':([22,52,],[33,33,]),'DIFER':([22,52,],[34,34,]),'NUMB':([25,28,29,30,31,32,33,34,35,36,56,75,],[38,43,-21,-22,-23,-24,-25,-26,-27,44,61,80,]),'PARER':([39,40,41,42,43,65,66,67,81,83,94,95,96,99,100,101,],[45,46,-28,47,-29,-18,72,-17,85,87,-20,98,-19,-16,103,-15,]),'PUNTOCOMA':([44,61,78,],[48,68,83,]),'BRACL':([45,46,47,82,87,],[49,50,51,86,91,]),'IMPRIMIR':([51,64,86,91,],[55,71,90,93,]),'CONTENIDO':([60,92,97,],[67,96,101,]),'BRACR':([72,84,85,98,103,],[77,88,89,102,104,]),'INCR':([73,],[78,]),'MAS':([74,],[79,]),'SINO':([77,],[82,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'program':([0,],[2,]),'opcion2':([0,49,],[3,53,]),'opcion3':([0,],[4,]),'opcion4':([0,],[5,]),'funcadenaprint':([0,],[6,]),'value':([11,],[16,]),'operando':([22,52,],[28,56,]),'contentn':([28,],[42,]),'var':([53,],[57,]),'contentIF':([60,],[66,]),'contentELSE':([92,],[95,]),'content':([97,],[100,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> program','init',1,'p_init','semantico.py',12),
  ('init -> opcion2','init',1,'p_init','semantico.py',13),
  ('init -> opcion3','init',1,'p_init','semantico.py',14),
  ('init -> opcion4','init',1,'p_init','semantico.py',15),
  ('init -> funcadenaprint','init',1,'p_init','semantico.py',16),
  ('opcion2 -> VARIABLE CADENA ID ASSIG ID','opcion2',5,'p_opcion2','semantico.py',19),
  ('opcion2 -> VARIABLE ENTERO ID ASSIG NUMB','opcion2',5,'p_opcion2','semantico.py',20),
  ('var -> VARIABLE ENTERO ID ASSIG NUMB','var',5,'p_var','semantico.py',35),
  ('opcion3 -> opcion2 SI PAREL ID operando contentn PARER BRACL IMPRIMIR PAREL contentIF PARER BRACR SINO BRACL IMPRIMIR PAREL contentELSE PARER BRACR','opcion3',20,'p_opcion3','semantico.py',44),
  ('opcion4 -> FUNCION ID PAREL ENTERO ID PARER BRACL opcion2 var ID ASSIG ID MAS ID BRACR','opcion4',15,'p_opcion4','semantico.py',89),
  ('funcadenaprint -> FUNCION ID PAREL CADENA ID PARER BRACL ID ASSIG ID IMPRIMIR PAREL ID PARER BRACR','funcadenaprint',15,'p_funcadenaprint','semantico.py',110),
  ('program -> PARA PAREL value ID ASSIG NUMB PUNTOCOMA ID operando NUMB PUNTOCOMA ID INCR PUNTOCOMA PARER BRACL IMPRIMIR PAREL content PARER BRACR','program',21,'p_program','semantico.py',117),
  ('value -> CADENA','value',1,'p_value','semantico.py',134),
  ('value -> ENTERO','value',1,'p_value','semantico.py',135),
  ('content -> CONTENIDO','content',1,'p_content','semantico.py',140),
  ('content -> ID','content',1,'p_content','semantico.py',141),
  ('contentIF -> CONTENIDO','contentIF',1,'p_contentIF','semantico.py',145),
  ('contentIF -> ID','contentIF',1,'p_contentIF','semantico.py',146),
  ('contentELSE -> CONTENIDO','contentELSE',1,'p_contentELSE','semantico.py',151),
  ('contentELSE -> ID','contentELSE',1,'p_contentELSE','semantico.py',152),
  ('operando -> MAY','operando',1,'p_operando','semantico.py',157),
  ('operando -> MAYIG','operando',1,'p_operando','semantico.py',158),
  ('operando -> MENIG','operando',1,'p_operando','semantico.py',159),
  ('operando -> IGIG','operando',1,'p_operando','semantico.py',160),
  ('operando -> MENO','operando',1,'p_operando','semantico.py',161),
  ('operando -> DIFER','operando',1,'p_operando','semantico.py',162),
  ('operando -> ASSIG','operando',1,'p_operando','semantico.py',163),
  ('contentn -> ID','contentn',1,'p_contentn','semantico.py',168),
  ('contentn -> NUMB','contentn',1,'p_contentn','semantico.py',169),
]
