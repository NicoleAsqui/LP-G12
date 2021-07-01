import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from AnalizadorLexico.lexer import tokens

'''Reglas agregadas por Nicole Asqui

p_codigo
p_algoritmo
p_sentenciaWhile
p_asignacion
p_expresion_aritmetica
p_expresion
p_comparacion
p_comparaciones
p_sentenciaAnd
p_sentenciaOr
p_operadorMat
p_operadorComp
p_sentenciaIf
p_error
p_conjunto
p_estructuraArreglo
p_metodosArreglos

Reglas agregadas por Briggitte Lopez
p_declarationSwitch
p_cuerpoSwitch
p_case
p_default
p_console
p_sentenciaFor
p_condicionFOR
p_busquedaFOR
p_listaFOR
p_variablesFOR
p_IncDecremento
p_crearVariables
p_instruccion
p_crearObjeto
p_crearFunction
p_cuerpoFunction
'''

def p_codigo(p):
    '''codigo : algoritmo
                | algoritmo codigo
    '''

def p_algoritmo(p):
    ''' algoritmo : asignacion
                    | sentenciaWHILE
                    | sentenciaIf
                    | comentarios
                    | switch
                    | sentenciaFor
                    | crearVariable
                    | crearObjeto
                    | crearFunction
                    | estructuraArreglo
                    | sentenciaOR
                    | sentenciaAND
                    | comparaciones
                    | metodosArreglos
                    | sentenciaDo
                    | estructuraMap
                    | funcionesMap
                    | metodosTupla
                    | consolep


    '''

def p_sentenciaDO(p):
    '''sentenciaDo : DO LIZQ codigo LDER WHILE PIZQ comparacion PDER PCOMA
    '''

def p_estructuraMap(p):
    ''' estructuraMap : VAR variables IGUAL NEW SET PIZQ CIZQ conjunto CDER PDER PCOMA
                    | LET variables IGUAL NEW SET PIZQ CIZQ conjunto CDER PDER PCOMA
    '''

def p_funcionesMap(p):
    ''' funcionesMap : variables PUNTO ADD PIZQ expresion PDER PCOMA
                    | variables PUNTO HAS PIZQ expresion PDER PCOMA
                    | variables PUNTO FOREACH PIZQ PIZQ VARIABLE PDER DERECHA LIZQ console LDER PDER PCOMA

    '''

def p_sentenciaWhile(p):
    '''sentenciaWHILE : WHILE PIZQ comparacion PDER LIZQ codigo LDER
    '''

def p_estructuraArreglo(p):
    ''' estructuraArreglo : VAR variables IGUAL CIZQ conjunto CDER PCOMA
    '''

def p_metodosArreglos(p):
    ''' metodosArreglos : variables PUNTO PUSH PIZQ expresion PDER PCOMA
                        | variables PUNTO POP PIZQ  PDER PCOMA
                        | variables PUNTO JOIN PIZQ  PDER PCOMA
    '''

def p_conjunto(p):
    '''conjunto : valor
                | valor COMA conjunto
    '''

def p_asignacion(p):
    'asignacion : VAR variables tipoasignacion expresion PCOMA'

def p_tipoasignacion(p):
    '''tipoasignacion : IGUAL
                    | ASIG_SUMA
                    | ASIG_MEN
                    | ASIG_DIV
                    | ASIG_MUL
                    | ASIG_BOR
                    | ASIG_BAN
                    | ASIG_XOR
                    | ASIG_RESDU
                    | ASIG_EXPO
                    | ASIG_DE_I
                    | ASIG_DE_D
                    | ASIG_DSG
                    | ASIG_OR
                    | ASIG_ANU
    '''

def p_expresion_aritmetica(p):
    '''expresion : valor operadorMat expresion
                | PIZQ valor operadorMat expresion PDER
    '''

def p_expresion(p):
    ''' expresion : valor
    '''

def p_comparacion(p):
    '''comparacion : expresion operadorComp expresion
    '''

def p_comparaciones(p):
    ''' comparaciones : comparacion PCOMA
                      | comparacion AND comparacion PCOMA
                      | comparacion OR comparacion PCOMA
    '''

def p_sentenciaAnd(p):
    ''' sentenciaAND : expresion AND expresion PCOMA
    '''
def p_sentenciaOr(p):
    ''' sentenciaOR : expresion OR expresion PCOMA
    '''

def p_operadorMat(p):
    '''operadorMat : MAS
                | RESTA
                | PROD
                | DIVISION
                | POTENCIA
    '''
def p_operadorComp(p):
    '''operadorComp : MAYOR
                | MENOR
                | COMP_IGUAL
                | DIFERENTE
    '''


def p_valor(p):
    '''valor : ENTERO
                | variables
                | CADENA
                | TRUE
                | FALSE

    '''

def p_variables(p):
    """ variables : VARIABLE
                | CONSTANTE
    """


def p_sentenciaIf(p):
    ''' sentenciaIf : IF PIZQ comparacion PDER LIZQ codigo LDER
                        | IF PIZQ comparacion PDER LIZQ codigo LDER ELSE LIZQ codigo LDER
    '''

def p_comentarios(p):
    ''' comentarios : COMENTARIO_EN_LINEA
                    | COMENTARIO_MULTILINEA

    '''

def p_metodosTupla(p):
    ''' metodosTupla : variables PUNTO INDEX PIZQ expresion PDER PCOMA
                        | variables PUNTO COUNT PIZQ variables PDER PCOMA
                        | LEN PIZQ variables PDER PCOMA
    '''

def p_declarationSwitch(p):
    ''' switch : SWITCH PIZQ expresion PDER cuerpoSwitch'''

def p_cuerpoSwitch(p):
    ''' cuerpoSwitch : case
                    | default'''

def p_case(p):
    ''' case : CASE COMILL valor COMILL COLON codigo BREAK PCOMA'''

def p_default(p):
    ''' default : DEFAULT COLON codigo '''

def p_console(p):
    ''' console : CONSOLE PUNTO LOG PIZQ  PDER PCOMA'''

def p_sentenciaFor(p):
    '''sentenciaFor : FOR PIZQ condicionFor PDER LIZQ codigo LDER
    '''

def p_condicionFOR(p):
    '''condicionFor : asignacion PCOMA comparacion PCOMA variables DEC '''


def p_crearVariables(p):
    ''' crearVariable : instruccionVL VARIABLE IGUAL CONSTANTE
                                            | ENTERO
                                            | CADENA'''

def p_instruccion(p):
    ''' instruccionVL : VAR
                    | LET '''

def p_crearObjeto(p):
    ''' crearObjeto : CONST variables IGUAL NEW OBJECT PIZQ PDER PCOMA '''

def p_crearFunction(p):
    ''' crearFunction : FUNCTION variables PIZQ conjunto PDER LIZQ cuerpoFunction LDER'''

def p_cuerpoFunction(p):
    ''' cuerpoFunction : THIS PUNTO variables IGUAL variables PCOMA'''




# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser

parser = yacc.yacc()

def leerCodigo(data):
        #print(data)
        result = parser.parse(data)
        #print(result.value)
        return result

def leerAlgoritmo(file):
    s = file.read()
    print(s)
    result = parser.parse(s)
    print(result)
    file.close()

archivo1 = open("../archivos/algoritmo.txt")

leerAlgoritmo(archivo1)