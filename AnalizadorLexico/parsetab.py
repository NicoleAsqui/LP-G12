
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIG ASIG_ANU ASIG_BAN ASIG_BOR ASIG_DE_D ASIG_DE_I ASIG_DIV ASIG_DSG ASIG_EXPO ASIG_MEN ASIG_MUL ASIG_OR ASIG_RESDU ASIG_SUMA ASIG_XOR BREAK CADENA CASE CATCH CDER CIZQ COLON COMA COMENTARIO_EN_LINEA COMENTARIO_MULTILINEA COMILL COMP_IGUAL CONSOLE CONST CONSTANTE CONTINUE DEBUGGER DEC DEFAULT DIFERENTE DIVISION DO ELSE ENTERO EQ_ESTRIC FALSE FINALY FOR FUNCTION IF IGUAL IN INC INSTANCEOF INTERROGACION LDER LET LIZQ LOG MAS MAYOR MENOR MOD NEW NOE_ESTRIC NOT OR PCOMA PDER PIZQ POP POTENCIA PROD PUNTO PUSH RESTA RETURN SWITCH THIS TRHOW TRUE TRY TYPEOF VAR VARIABLE VOID WHILEcodigo : algoritmo\n                | algoritmo codigo\n     algoritmo : asignacion\n                    | sentenciaWHILE\n                    | sentenciaIf\n                    | comentarios\n                    | switch\n                    | sentenciaFor\n                    | crearVariable\n                    | crearObjeto\n                    | crearFunction\n                    | estructuraArreglo\n                    | sentenciaOR\n                    | sentenciaAND\n\n    sentenciaWHILE : WHILE PIZQ comparacion PDER codigo\n     estructuraArreglo : VAR variables IGUAL CIZQ conjunto CDER PCOMA\n    conjunto : valor\n                | valor COMA conjunto\n    asignacion : VAR variables IGUAL expresion PCOMAexpresion : valor operadorMat expresion\n                | PIZQ valor operadorMat expresion PDER\n     expresion : valor\n    comparacion : expresion operadorComp expresion\n        | PIZQ expresion PDER operadorComp expresion\n        | PIZQ expresion operadorComp expresion PDER\n        | expresion operadorComp PIZQ expresion PDER\n     comparaciones : comparacion\n                      | comparacion AND comparacion\n                      | comparacion OR comparacion\n     sentenciaAND : expresion AND expresion PCOMA\n     sentenciaOR : expresion OR expresion PCOMA\n    operadorMat : MAS\n                | RESTA\n                | PROD\n                | DIVISION\n                | POTENCIA\n    operadorComp : MAYOR\n                | MENOR\n                | COMP_IGUAL\n                | DIFERENTE\n    valor : ENTERO\n                | variables\n                | CADENA\n                | TRUE\n                | FALSE\n\n     variables : VARIABLE\n                | CONSTANTE\n     sentenciaIf : IF comparaciones codigo ELSE codigo\n     comentarios : COMENTARIO_EN_LINEA\n                    | COMENTARIO_MULTILINEA\n\n     switch : SWITCH PIZQ expresion PDER cuerpoSwitch cuerpoSwitch : case\n                    | default case : CASE COMILL valor COMILL COLON console BREAK PCOMA default : DEFAULT COLON console console : CONSOLE PUNTO LOG PCOMAsentenciaFor : FOR condicionFor codigo\n    condicionFor : PIZQ busquedaFOR PDER  busquedaFOR : listaFor\n                        | variablesFor listaFor : variables IN variables variablesFor : asignacion PCOMA comparacion PCOMA VARIABLE incDecremento incDecremento : INC\n                        | DEC crearVariable : instruccionVL VARIABLE IGUAL CONSTANTE\n                                            | ENTERO\n                                            | CADENA instruccionVL : VAR\n                        | LET  crearObjeto : CONST VARIABLE NEW VARIABLE  crearFunction : FUNCTION variables PIZQ cuerpoFunction PDER cuerpoFunction : THIS PUNTO asignacion'
    
_lr_action_items = {'VAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,26,27,28,29,33,34,35,36,42,43,44,45,49,50,76,86,89,90,91,93,94,95,96,102,106,107,110,113,114,115,120,121,122,128,129,132,133,134,139,142,153,155,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,-41,-43,15,-27,15,82,-57,-20,-31,-30,15,15,-28,-29,-23,-58,-65,-70,-19,-15,-21,-48,-51,-52,-53,-71,82,-26,-24,-25,-16,-55,-56,-54,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,26,27,28,29,33,34,35,36,42,43,44,45,49,76,86,89,90,91,93,94,95,96,102,106,107,110,113,114,115,120,121,122,128,132,133,134,139,142,153,155,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,-41,-43,18,-27,18,-57,-20,-31,-30,18,18,-28,-29,-23,-58,-65,-70,-19,-15,-21,-48,-51,-52,-53,-71,-26,-24,-25,-16,-55,-56,-54,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,26,27,28,29,33,34,35,36,42,43,44,45,49,76,86,89,90,91,93,94,95,96,102,106,107,110,113,114,115,120,121,122,128,132,133,134,139,142,153,155,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,-41,-43,20,-27,20,-57,-20,-31,-30,20,20,-28,-29,-23,-58,-65,-70,-19,-15,-21,-48,-51,-52,-53,-71,-26,-24,-25,-16,-55,-56,-54,]),'COMENTARIO_EN_LINEA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,26,27,28,29,33,34,35,36,42,43,44,45,49,76,86,89,90,91,93,94,95,96,102,106,107,110,113,114,115,120,121,122,128,132,133,134,139,142,153,155,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,-41,-43,21,-27,21,-57,-20,-31,-30,21,21,-28,-29,-23,-58,-65,-70,-19,-15,-21,-48,-51,-52,-53,-71,-26,-24,-25,-16,-55,-56,-54,]),'COMENTARIO_MULTILINEA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,26,27,28,29,33,34,35,36,42,43,44,45,49,76,86,89,90,91,93,94,95,96,102,106,107,110,113,114,115,120,121,122,128,132,133,134,139,142,153,155,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,-41,-43,22,-27,22,-57,-20,-31,-30,22,22,-28,-29,-23,-58,-65,-70,-19,-15,-21,-48,-51,-52,-53,-71,-26,-24,-25,-16,-55,-56,-54,]),'SWITCH':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,26,27,28,29,33,34,35,36,42,43,44,45,49,76,86,89,90,91,93,94,95,96,102,106,107,110,113,114,115,120,121,122,128,132,133,134,139,142,153,155,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,-41,-43,23,-27,23,-57,-20,-31,-30,23,23,-28,-29,-23,-58,-65,-70,-19,-15,-21,-48,-51,-52,-53,-71,-26,-24,-25,-16,-55,-56,-54,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,26,27,28,29,33,34,35,36,42,43,44,45,49,76,86,89,90,91,93,94,95,96,102,106,107,110,113,114,115,120,121,122,128,132,133,134,139,142,153,155,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,-41,-43,24,-27,24,-57,-20,-31,-30,24,24,-28,-29,-23,-58,-65,-70,-19,-15,-21,-48,-51,-52,-53,-71,-26,-24,-25,-16,-55,-56,-54,]),'ENTERO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,19,20,21,22,26,27,28,29,33,34,35,36,38,39,40,42,43,44,45,47,48,49,54,55,56,57,58,59,60,64,66,67,68,69,70,71,72,76,86,88,89,90,91,93,94,95,96,97,99,100,102,104,106,107,110,113,114,115,117,120,121,122,127,128,131,132,133,134,135,139,142,153,155,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,42,42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,42,42,42,-41,-43,28,-27,42,42,28,42,-32,-33,-34,-35,-36,42,42,42,42,42,-37,-38,-39,-40,-57,-20,42,-31,-30,28,28,-28,-29,-23,42,42,42,-58,42,-65,-70,-19,-15,-21,-48,42,-51,-52,-53,42,-71,42,-26,-24,-25,42,-16,-55,-56,-54,]),'CADENA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,19,20,21,22,26,27,28,29,33,34,35,36,38,39,40,42,43,44,45,47,48,49,54,55,56,57,58,59,60,64,66,67,68,69,70,71,72,76,86,88,89,90,91,93,94,95,96,97,99,100,102,104,106,107,110,113,114,115,117,120,121,122,127,128,131,132,133,134,135,139,142,153,155,],[29,29,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,43,43,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,43,43,43,-41,-43,29,-27,43,43,29,43,-32,-33,-34,-35,-36,43,43,43,43,43,-37,-38,-39,-40,-57,-20,43,-31,-30,29,29,-28,-29,-23,43,43,43,-58,43,-65,-70,-19,-15,-21,-48,43,-51,-52,-53,43,-71,43,-26,-24,-25,43,-16,-55,-56,-54,]),'CONST':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,26,27,28,29,33,34,35,36,42,43,44,45,49,76,86,89,90,91,93,94,95,96,102,106,107,110,113,114,115,120,121,122,128,132,133,134,139,142,153,155,],[30,30,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,-41,-43,30,-27,30,-57,-20,-31,-30,30,30,-28,-29,-23,-58,-65,-70,-19,-15,-21,-48,-51,-52,-53,-71,-26,-24,-25,-16,-55,-56,-54,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,26,27,28,29,33,34,35,36,42,43,44,45,49,76,86,89,90,91,93,94,95,96,102,106,107,110,113,114,115,120,121,122,128,132,133,134,139,142,153,155,],[31,31,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,-41,-43,31,-27,31,-57,-20,-31,-30,31,31,-28,-29,-23,-58,-65,-70,-19,-15,-21,-48,-51,-52,-53,-71,-26,-24,-25,-16,-55,-56,-54,]),'LET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,26,27,28,29,33,34,35,36,42,43,44,45,49,76,86,89,90,91,93,94,95,96,102,106,107,110,113,114,115,120,121,122,128,132,133,134,139,142,153,155,],[32,32,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,-41,-43,32,-27,32,-57,-20,-31,-30,32,32,-28,-29,-23,-58,-65,-70,-19,-15,-21,-48,-51,-52,-53,-71,-26,-24,-25,-16,-55,-56,-54,]),'PIZQ':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,20,21,22,23,24,26,27,28,29,33,34,35,36,38,39,40,42,43,44,45,47,48,49,53,54,55,56,57,58,59,60,64,66,67,68,69,70,71,72,76,86,89,90,91,93,94,95,96,97,99,100,102,104,106,107,110,113,114,115,117,120,121,122,127,128,132,133,134,139,142,153,155,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,40,47,-49,-50,48,50,-46,-47,-66,-67,-22,-44,-45,-2,19,19,47,-41,-43,19,-27,19,19,19,85,19,-32,-33,-34,-35,-36,19,19,47,47,97,-37,-38,-39,-40,-57,-20,-31,-30,19,19,-28,-29,-23,19,19,19,-58,47,-65,-70,-19,-15,-21,-48,19,-51,-52,-53,19,-71,-26,-24,-25,-16,-55,-56,-54,]),'TRUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,19,20,21,22,26,27,28,29,33,34,35,36,38,39,40,42,43,44,45,47,48,49,54,55,56,57,58,59,60,64,66,67,68,69,70,71,72,76,86,88,89,90,91,93,94,95,96,97,99,100,102,104,106,107,110,113,114,115,117,120,121,122,127,128,131,132,133,134,135,139,142,153,155,],[34,34,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,34,34,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,34,34,34,-41,-43,34,-27,34,34,34,34,-32,-33,-34,-35,-36,34,34,34,34,34,-37,-38,-39,-40,-57,-20,34,-31,-30,34,34,-28,-29,-23,34,34,34,-58,34,-65,-70,-19,-15,-21,-48,34,-51,-52,-53,34,-71,34,-26,-24,-25,34,-16,-55,-56,-54,]),'FALSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,19,20,21,22,26,27,28,29,33,34,35,36,38,39,40,42,43,44,45,47,48,49,54,55,56,57,58,59,60,64,66,67,68,69,70,71,72,76,86,88,89,90,91,93,94,95,96,97,99,100,102,104,106,107,110,113,114,115,117,120,121,122,127,128,131,132,133,134,135,139,142,153,155,],[35,35,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-42,35,35,-49,-50,-46,-47,-66,-67,-22,-44,-45,-2,35,35,35,-41,-43,35,-27,35,35,35,35,-32,-33,-34,-35,-36,35,35,35,35,35,-37,-38,-39,-40,-57,-20,35,-31,-30,35,35,-28,-29,-23,35,35,35,-58,35,-65,-70,-19,-15,-21,-48,35,-51,-52,-53,35,-71,35,-26,-24,-25,35,-16,-55,-56,-54,]),'VARIABLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,20,21,22,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,42,43,44,45,47,48,49,50,54,55,56,57,58,59,60,64,66,67,68,69,70,71,72,76,82,84,86,88,89,90,91,93,94,95,96,97,99,100,102,103,104,106,107,110,113,114,115,117,120,121,122,127,128,131,132,133,134,135,137,139,142,153,155,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,26,-42,26,26,-49,-50,51,-46,-47,-66,-67,52,26,-69,-22,-44,-45,-2,26,26,26,-41,-43,26,-27,26,26,26,26,26,-32,-33,-34,-35,-36,26,26,26,26,26,-37,-38,-39,-40,-57,26,107,-20,26,-31,-30,26,26,-28,-29,-23,26,26,26,-58,26,26,-65,-70,-19,-15,-21,-48,26,-51,-52,-53,26,-71,26,-26,-24,-25,26,144,-16,-55,-56,-54,]),'CONSTANTE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,20,21,22,26,27,28,29,31,33,34,35,36,38,39,40,42,43,44,45,47,48,49,50,54,55,56,57,58,59,60,64,66,67,68,69,70,71,72,76,82,83,86,88,89,90,91,93,94,95,96,97,99,100,102,103,104,106,107,110,113,114,115,117,120,121,122,127,128,131,132,133,134,135,139,142,153,155,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,27,-42,27,27,-49,-50,-46,-47,-66,-67,27,-22,-44,-45,-2,27,27,27,-41,-43,27,-27,27,27,27,27,27,-32,-33,-34,-35,-36,27,27,27,27,27,-37,-38,-39,-40,-57,27,106,-20,27,-31,-30,27,27,-28,-29,-23,27,27,27,-58,27,27,-65,-70,-19,-15,-21,-48,27,-51,-52,-53,27,-71,27,-26,-24,-25,27,-16,-55,-56,-54,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,21,22,28,29,36,76,89,90,106,107,110,113,115,120,121,122,128,139,142,153,155,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-49,-50,-66,-67,-2,-57,-31,-30,-65,-70,-19,-15,-48,-51,-52,-53,-71,-16,-55,-56,-54,]),'ELSE':([2,3,4,5,6,7,8,9,10,11,12,13,14,21,22,28,29,36,65,76,89,90,106,107,110,113,115,120,121,122,128,139,142,153,155,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-49,-50,-66,-67,-2,93,-57,-31,-30,-65,-70,-19,-15,-48,-51,-52,-53,-71,-16,-55,-56,-54,]),'MAS':([16,26,27,28,29,33,34,35,41,42,43,74,],[-42,-46,-47,-41,-43,55,-44,-45,55,-41,-43,55,]),'RESTA':([16,26,27,28,29,33,34,35,41,42,43,74,],[-42,-46,-47,-41,-43,56,-44,-45,56,-41,-43,56,]),'PROD':([16,26,27,28,29,33,34,35,41,42,43,74,],[-42,-46,-47,-41,-43,57,-44,-45,57,-41,-43,57,]),'DIVISION':([16,26,27,28,29,33,34,35,41,42,43,74,],[-42,-46,-47,-41,-43,58,-44,-45,58,-41,-43,58,]),'POTENCIA':([16,26,27,28,29,33,34,35,41,42,43,74,],[-42,-46,-47,-41,-43,59,-44,-45,59,-41,-43,59,]),'OR':([16,17,26,27,28,29,33,34,35,42,43,45,86,96,114,132,133,134,],[-42,38,-46,-47,-41,-43,-22,-44,-45,-41,-43,67,-20,-23,-21,-26,-24,-25,]),'AND':([16,17,26,27,28,29,33,34,35,42,43,45,86,96,114,132,133,134,],[-42,39,-46,-47,-41,-43,-22,-44,-45,-41,-43,66,-20,-23,-21,-26,-24,-25,]),'MAYOR':([16,26,27,33,34,35,42,43,46,73,74,86,98,114,119,],[-42,-46,-47,-22,-44,-45,-41,-43,69,69,-22,-20,69,-21,-20,]),'MENOR':([16,26,27,33,34,35,42,43,46,73,74,86,98,114,119,],[-42,-46,-47,-22,-44,-45,-41,-43,70,70,-22,-20,70,-21,-20,]),'COMP_IGUAL':([16,26,27,33,34,35,42,43,46,73,74,86,98,114,119,],[-42,-46,-47,-22,-44,-45,-41,-43,71,71,-22,-20,71,-21,-20,]),'DIFERENTE':([16,26,27,33,34,35,42,43,46,73,74,86,98,114,119,],[-42,-46,-47,-22,-44,-45,-41,-43,72,72,-22,-20,72,-21,-20,]),'PCOMA':([16,26,27,33,34,35,42,43,61,62,81,86,87,96,110,114,126,130,132,133,134,151,154,],[-42,-46,-47,-22,-44,-45,-41,-43,89,90,104,-20,110,-23,-19,-21,137,139,-26,-24,-25,153,155,]),'PDER':([16,26,27,33,34,35,42,43,63,73,74,75,77,78,79,86,92,96,108,110,114,116,118,119,125,132,133,134,138,147,148,149,],[-42,-46,-47,-22,-44,-45,-41,-43,91,98,-22,101,102,-59,-60,-20,114,-23,128,-19,-21,132,134,114,-61,-26,-24,-25,-72,-62,-63,-64,]),'COMA':([16,26,27,34,35,42,43,112,],[-42,-46,-47,-44,-45,-41,-43,131,]),'CDER':([16,26,27,34,35,42,43,111,112,140,],[-42,-46,-47,-44,-45,-41,-43,130,-17,-18,]),'COMILL':([16,26,27,34,35,42,43,123,141,],[-42,-46,-47,-44,-45,-41,-43,135,145,]),'IGUAL':([26,27,37,51,105,],[-46,-47,60,83,127,]),'IN':([26,27,80,],[-46,-47,103,]),'NEW':([52,],[84,]),'CIZQ':([60,],[88,]),'THIS':([85,],[109,]),'CASE':([101,],[123,]),'DEFAULT':([101,],[124,]),'PUNTO':([109,143,],[129,146,]),'COLON':([124,145,],[136,150,]),'CONSOLE':([136,150,],[143,143,]),'INC':([144,],[148,]),'DEC':([144,],[149,]),'LOG':([146,],[151,]),'BREAK':([152,153,],[154,-56,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,2,44,49,91,93,],[1,36,65,76,113,115,]),'algoritmo':([0,2,44,49,91,93,],[2,2,2,2,2,2,]),'asignacion':([0,2,44,49,50,91,93,129,],[3,3,3,3,81,3,3,138,]),'sentenciaWHILE':([0,2,44,49,91,93,],[4,4,4,4,4,4,]),'sentenciaIf':([0,2,44,49,91,93,],[5,5,5,5,5,5,]),'comentarios':([0,2,44,49,91,93,],[6,6,6,6,6,6,]),'switch':([0,2,44,49,91,93,],[7,7,7,7,7,7,]),'sentenciaFor':([0,2,44,49,91,93,],[8,8,8,8,8,8,]),'crearVariable':([0,2,44,49,91,93,],[9,9,9,9,9,9,]),'crearObjeto':([0,2,44,49,91,93,],[10,10,10,10,10,10,]),'crearFunction':([0,2,44,49,91,93,],[11,11,11,11,11,11,]),'estructuraArreglo':([0,2,44,49,91,93,],[12,12,12,12,12,12,]),'sentenciaOR':([0,2,44,49,91,93,],[13,13,13,13,13,13,]),'sentenciaAND':([0,2,44,49,91,93,],[14,14,14,14,14,14,]),'variables':([0,2,15,19,20,31,38,39,40,44,47,48,49,50,54,60,64,66,67,68,82,88,91,93,97,99,100,103,104,117,127,131,135,],[16,16,37,16,16,53,16,16,16,16,16,16,16,80,16,16,16,16,16,16,105,16,16,16,16,16,16,125,16,16,16,16,16,]),'expresion':([0,2,20,38,39,40,44,47,48,49,54,60,64,66,67,68,91,93,97,99,100,104,117,127,],[17,17,46,61,62,46,17,73,75,17,86,87,92,46,46,96,17,17,116,118,119,46,133,87,]),'instruccionVL':([0,2,44,49,91,93,],[25,25,25,25,25,25,]),'valor':([0,2,19,20,38,39,40,44,47,48,49,54,60,64,66,67,68,88,91,93,97,99,100,104,117,127,131,135,],[33,33,41,33,33,33,33,33,74,33,33,33,33,33,33,33,33,112,33,33,74,33,33,33,33,33,112,141,]),'comparaciones':([20,],[44,]),'comparacion':([20,40,66,67,104,],[45,63,94,95,126,]),'condicionFor':([24,],[49,]),'operadorMat':([33,41,74,],[54,64,100,]),'operadorComp':([46,73,98,],[68,99,117,]),'busquedaFOR':([50,],[77,]),'listaFor':([50,],[78,]),'variablesFor':([50,],[79,]),'cuerpoFunction':([85,],[108,]),'conjunto':([88,131,],[111,140,]),'cuerpoSwitch':([101,],[120,]),'case':([101,],[121,]),'default':([101,],[122,]),'console':([136,150,],[142,152,]),'incDecremento':([144,],[147,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> algoritmo','codigo',1,'p_codigo','sintactico_yacc.py',45),
  ('codigo -> algoritmo codigo','codigo',2,'p_codigo','sintactico_yacc.py',46),
  ('algoritmo -> asignacion','algoritmo',1,'p_algoritmo','sintactico_yacc.py',50),
  ('algoritmo -> sentenciaWHILE','algoritmo',1,'p_algoritmo','sintactico_yacc.py',51),
  ('algoritmo -> sentenciaIf','algoritmo',1,'p_algoritmo','sintactico_yacc.py',52),
  ('algoritmo -> comentarios','algoritmo',1,'p_algoritmo','sintactico_yacc.py',53),
  ('algoritmo -> switch','algoritmo',1,'p_algoritmo','sintactico_yacc.py',54),
  ('algoritmo -> sentenciaFor','algoritmo',1,'p_algoritmo','sintactico_yacc.py',55),
  ('algoritmo -> crearVariable','algoritmo',1,'p_algoritmo','sintactico_yacc.py',56),
  ('algoritmo -> crearObjeto','algoritmo',1,'p_algoritmo','sintactico_yacc.py',57),
  ('algoritmo -> crearFunction','algoritmo',1,'p_algoritmo','sintactico_yacc.py',58),
  ('algoritmo -> estructuraArreglo','algoritmo',1,'p_algoritmo','sintactico_yacc.py',59),
  ('algoritmo -> sentenciaOR','algoritmo',1,'p_algoritmo','sintactico_yacc.py',60),
  ('algoritmo -> sentenciaAND','algoritmo',1,'p_algoritmo','sintactico_yacc.py',61),
  ('sentenciaWHILE -> WHILE PIZQ comparacion PDER codigo','sentenciaWHILE',5,'p_sentenciaWhile','sintactico_yacc.py',66),
  ('estructuraArreglo -> VAR variables IGUAL CIZQ conjunto CDER PCOMA','estructuraArreglo',7,'p_estructuraArreglo','sintactico_yacc.py',70),
  ('conjunto -> valor','conjunto',1,'p_conjunto','sintactico_yacc.py',74),
  ('conjunto -> valor COMA conjunto','conjunto',3,'p_conjunto','sintactico_yacc.py',75),
  ('asignacion -> VAR variables IGUAL expresion PCOMA','asignacion',5,'p_asignacion','sintactico_yacc.py',79),
  ('expresion -> valor operadorMat expresion','expresion',3,'p_expresion_aritmetica','sintactico_yacc.py',82),
  ('expresion -> PIZQ valor operadorMat expresion PDER','expresion',5,'p_expresion_aritmetica','sintactico_yacc.py',83),
  ('expresion -> valor','expresion',1,'p_expresion','sintactico_yacc.py',87),
  ('comparacion -> expresion operadorComp expresion','comparacion',3,'p_comparacion','sintactico_yacc.py',91),
  ('comparacion -> PIZQ expresion PDER operadorComp expresion','comparacion',5,'p_comparacion','sintactico_yacc.py',92),
  ('comparacion -> PIZQ expresion operadorComp expresion PDER','comparacion',5,'p_comparacion','sintactico_yacc.py',93),
  ('comparacion -> expresion operadorComp PIZQ expresion PDER','comparacion',5,'p_comparacion','sintactico_yacc.py',94),
  ('comparaciones -> comparacion','comparaciones',1,'p_comparaciones','sintactico_yacc.py',98),
  ('comparaciones -> comparacion AND comparacion','comparaciones',3,'p_comparaciones','sintactico_yacc.py',99),
  ('comparaciones -> comparacion OR comparacion','comparaciones',3,'p_comparaciones','sintactico_yacc.py',100),
  ('sentenciaAND -> expresion AND expresion PCOMA','sentenciaAND',4,'p_sentenciaAnd','sintactico_yacc.py',104),
  ('sentenciaOR -> expresion OR expresion PCOMA','sentenciaOR',4,'p_sentenciaOr','sintactico_yacc.py',107),
  ('operadorMat -> MAS','operadorMat',1,'p_operadorMat','sintactico_yacc.py',111),
  ('operadorMat -> RESTA','operadorMat',1,'p_operadorMat','sintactico_yacc.py',112),
  ('operadorMat -> PROD','operadorMat',1,'p_operadorMat','sintactico_yacc.py',113),
  ('operadorMat -> DIVISION','operadorMat',1,'p_operadorMat','sintactico_yacc.py',114),
  ('operadorMat -> POTENCIA','operadorMat',1,'p_operadorMat','sintactico_yacc.py',115),
  ('operadorComp -> MAYOR','operadorComp',1,'p_operadorComp','sintactico_yacc.py',118),
  ('operadorComp -> MENOR','operadorComp',1,'p_operadorComp','sintactico_yacc.py',119),
  ('operadorComp -> COMP_IGUAL','operadorComp',1,'p_operadorComp','sintactico_yacc.py',120),
  ('operadorComp -> DIFERENTE','operadorComp',1,'p_operadorComp','sintactico_yacc.py',121),
  ('valor -> ENTERO','valor',1,'p_valor','sintactico_yacc.py',126),
  ('valor -> variables','valor',1,'p_valor','sintactico_yacc.py',127),
  ('valor -> CADENA','valor',1,'p_valor','sintactico_yacc.py',128),
  ('valor -> TRUE','valor',1,'p_valor','sintactico_yacc.py',129),
  ('valor -> FALSE','valor',1,'p_valor','sintactico_yacc.py',130),
  ('variables -> VARIABLE','variables',1,'p_variables','sintactico_yacc.py',135),
  ('variables -> CONSTANTE','variables',1,'p_variables','sintactico_yacc.py',136),
  ('sentenciaIf -> IF comparaciones codigo ELSE codigo','sentenciaIf',5,'p_sentenciaIf','sintactico_yacc.py',139),
  ('comentarios -> COMENTARIO_EN_LINEA','comentarios',1,'p_comentarios','sintactico_yacc.py',143),
  ('comentarios -> COMENTARIO_MULTILINEA','comentarios',1,'p_comentarios','sintactico_yacc.py',144),
  ('switch -> SWITCH PIZQ expresion PDER cuerpoSwitch','switch',5,'p_declarationSwitch','sintactico_yacc.py',149),
  ('cuerpoSwitch -> case','cuerpoSwitch',1,'p_cuerpoSwitch','sintactico_yacc.py',152),
  ('cuerpoSwitch -> default','cuerpoSwitch',1,'p_cuerpoSwitch','sintactico_yacc.py',153),
  ('case -> CASE COMILL valor COMILL COLON console BREAK PCOMA','case',8,'p_case','sintactico_yacc.py',156),
  ('default -> DEFAULT COLON console','default',3,'p_default','sintactico_yacc.py',159),
  ('console -> CONSOLE PUNTO LOG PCOMA','console',4,'p_console','sintactico_yacc.py',162),
  ('sentenciaFor -> FOR condicionFor codigo','sentenciaFor',3,'p_sentenciaFor','sintactico_yacc.py',165),
  ('condicionFor -> PIZQ busquedaFOR PDER','condicionFor',3,'p_condicionFOR','sintactico_yacc.py',169),
  ('busquedaFOR -> listaFor','busquedaFOR',1,'p_busquedaFOR','sintactico_yacc.py',172),
  ('busquedaFOR -> variablesFor','busquedaFOR',1,'p_busquedaFOR','sintactico_yacc.py',173),
  ('listaFor -> variables IN variables','listaFor',3,'p_listaFOR','sintactico_yacc.py',176),
  ('variablesFor -> asignacion PCOMA comparacion PCOMA VARIABLE incDecremento','variablesFor',6,'p_variablesFOR','sintactico_yacc.py',179),
  ('incDecremento -> INC','incDecremento',1,'p_IncDecremento','sintactico_yacc.py',183),
  ('incDecremento -> DEC','incDecremento',1,'p_IncDecremento','sintactico_yacc.py',184),
  ('crearVariable -> instruccionVL VARIABLE IGUAL CONSTANTE','crearVariable',4,'p_crearVariables','sintactico_yacc.py',187),
  ('crearVariable -> ENTERO','crearVariable',1,'p_crearVariables','sintactico_yacc.py',188),
  ('crearVariable -> CADENA','crearVariable',1,'p_crearVariables','sintactico_yacc.py',189),
  ('instruccionVL -> VAR','instruccionVL',1,'p_instruccion','sintactico_yacc.py',192),
  ('instruccionVL -> LET','instruccionVL',1,'p_instruccion','sintactico_yacc.py',193),
  ('crearObjeto -> CONST VARIABLE NEW VARIABLE','crearObjeto',4,'p_crearObjeto','sintactico_yacc.py',196),
  ('crearFunction -> FUNCTION variables PIZQ cuerpoFunction PDER','crearFunction',5,'p_crearFunction','sintactico_yacc.py',199),
  ('cuerpoFunction -> THIS PUNTO asignacion','cuerpoFunction',3,'p_cuerpoFunction','sintactico_yacc.py',202),
]
