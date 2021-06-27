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

    '''

def p_sentenciaWhile(p):
    '''sentenciaWHILE : WHILE  comparacion codigo
    '''

def p_asignacion(p):
    'asignacion : variables IGUAL expresion'

def p_expresion_aritmetica(p):
    '''expresion : valor operadorMat expresion
                | PIZQ valor operadorMat expresion PDER
    '''


def p_expresion(p):
    ''' expresion : valor
    '''

def p_comparacion(p):
    '''comparacion : expresion operadorComp expresion
        | PIZQ expresion PDER operadorComp expresion
        | PIZQ expresion operadorComp expresion PDER
        | expresion operadorComp PIZQ expresion PDER
    '''

def p_comparaciones(p):
    ''' comparaciones : comparacion
                      | sentenciaAND
                      | sentenciaOR
    '''

def p_sentenciaAnd(p):
    ''' sentenciaAND : comparacion AND comparacion
    '''
def p_sentenciaOr(p):
    ''' sentenciaOR : comparacion OR comparacion
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
    '''

def p_variables(p):
    """ variables : VARIABLE
                | CONSTANTE
    """
def p_sentenciaIf(p):
    ''' sentenciaIf : IF comparaciones codigo ELSE codigo
    '''

def p_comentarios(p):
    ''' comentarios : COMENTARIO_EN_LINEA
                    | COMENTARIO_MULTILINEA

    '''

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