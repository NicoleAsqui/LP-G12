import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from Analizador.analizador_lexico import tokens

# resultado del analisis
resultado_gramatica = []

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

def p_codigo(t):
    '''codigo : algoritmo
                | algoritmo codigo '''
    t[0] = t[1]


def p_algoritmo(t):
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
                    | expresion_aritmetica
                    | console
                    | condiciones
    '''
    t[0] = t[1]

def p_sentenciaDO(p):
    '''sentenciaDo : DO LIZQ codigo LDER WHILE PIZQ comparacionWhile PDER PCOMA
    '''

def p_estructuraMap(p):
    ''' estructuraMap : VAR VARIABLE IGUAL NEW SET PIZQ CIZQ conjunto CDER PDER PCOMA
                    | LET VARIABLE IGUAL NEW SET PIZQ CIZQ conjunto CDER PDER PCOMA
    '''

def p_funcionesMap(p):
    ''' funcionesMap : VARIABLE PUNTO ADD PIZQ expresion PDER PCOMA
                    | VARIABLE PUNTO HAS PIZQ expresion PDER PCOMA
                    | VARIABLE PUNTO FOREACH PIZQ PIZQ VARIABLE PDER DERECHA LIZQ console LDER PDER PCOMA
    '''

def p_sentenciaWhile(p):
    '''sentenciaWHILE : WHILE PIZQ comparacionWhile PDER LIZQ codigo LDER
    '''

def p_estructuraArreglo(p):
    ''' estructuraArreglo : VAR VARIABLE IGUAL CIZQ conjunto CDER PCOMA
                            | LET VARIABLE IGUAL CIZQ conjunto CDER PCOMA
                            | CONST VARIABLE IGUAL CIZQ conjunto CDER PCOMA
    '''

def p_comentarios(p):
    ''' comentarios : COMENTARIO_EN_LINEA
                    | COMENTARIO_MULTILINEA
    '''
def p_metodosArreglos(p):
    ''' metodosArreglos : VARIABLE PUNTO PUSH PIZQ expresion PDER PCOMA
                        | VARIABLE PUNTO POP PIZQ  PDER PCOMA
                        | VARIABLE PUNTO JOIN PIZQ  PDER PCOMA
    '''

def p_conjunto(p):
    '''conjunto : expresion
                | expresion COMA conjunto
    '''

def p_asignacion(p):
    '''asignacion : VAR VARIABLE tipoasignacion expresion PCOMA
                | LET VARIABLE tipoasignacion expresion PCOMA
    '''
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

def p_condiciones(t):
    '''condiciones : reglaSemanticaCondiciones
                    | PIZQ reglaSemanticaCondiciones PDER'''

def p_expresion_aritmetica(t):
    '''expresion_aritmetica : reglaSemanticaOperaciones
                | PIZQ reglaSemanticaOperaciones PDER
    '''
    t[0] = t[1]

def p_expresion(t):
    ''' expresion : valorMatematico
                | valorGramatico
                | valorBooleano
    '''


def p_comparacionWhile(p):
    '''comparacionWhile : VARIABLE operadorComp valorMatematico
                        | valorBooleano
                        | valorMatematico operadorComp valorMatematico
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

def p_operadorComp(p):
    '''operadorComp : MAYOR
                | MENOR
                | COMP_IGUAL
                | DIFERENTE
    '''


def p_valorMatematico(t):
    '''valorMatematico    : ENTERO
                    | DECIMAL'''
    t[0] = t[1]

def p_valorGramatico(p):
    '''valorGramatico : VARIABLE
                | CADENA
    '''


def p_valorBooleano(p):
    '''valorBooleano : TRUE
                | FALSE
    '''



def p_sentenciaIf(p):
    ''' sentenciaIf : IF PIZQ comparacion PDER LIZQ codigo LDER
                        | IF PIZQ comparacion PDER LIZQ codigo LDER ELSE LIZQ codigo LDER
    '''


def p_metodosTupla(p):
    ''' metodosTupla : VARIABLE PUNTO INDEX PIZQ expresion PDER PCOMA
                        | VARIABLE PUNTO COUNT PIZQ VARIABLE PDER PCOMA
                        | LEN PIZQ VARIABLE PDER PCOMA
    '''

def p_declarationSwitch(p):
    ''' switch : SWITCH PIZQ expresion PDER cuerpoSwitch'''

def p_cuerpoSwitch(p):
    ''' cuerpoSwitch : case
                    | default'''

def p_case(p):
    ''' case : CASE COMILL expresion COMILL COLON codigo BREAK PCOMA'''

def p_default(p):
    ''' default : DEFAULT COLON codigo '''

def p_console(p):
    ''' console : CONSOLE PUNTO LOG PIZQ  PDER PCOMA'''

def p_sentenciaFor(p):
    '''sentenciaFor : FOR PIZQ condicionFor PDER LIZQ codigo LDER
    '''

def p_condicionFOR(p):
    '''condicionFor : asignacion PCOMA comparacion PCOMA VARIABLE DEC '''


def p_crearVariables(p):
    ''' crearVariable : instruccionVL VARIABLE IGUAL ENTERO
                                            | CADENA'''

def p_instruccion(p):
    ''' instruccionVL : VAR
                    | LET '''

def p_crearObjeto(p):
    ''' crearObjeto : CONST VARIABLE IGUAL NEW OBJECT PIZQ PDER PCOMA '''

def p_crearFunction(p):
    ''' crearFunction : FUNCTION VARIABLE PIZQ conjunto PDER LIZQ cuerpoFunction LDER'''

def p_cuerpoFunction(p):
    ''' cuerpoFunction : THIS PUNTO VARIABLE IGUAL VARIABLE PCOMA'''

def p_reglaSemanticaOperaciones(t):
    '''reglaSemanticaOperaciones : valorMatematico MAS valorMatematico
                  | valorMatematico RESTA valorMatematico
                  | valorMatematico PROD valorMatematico
                  | valorMatematico DIVISION valorMatematico
                  | valorMatematico MOD valorMatematico
                  | valorMatematico POTENCIA valorMatematico'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1

def p_reglaSemanticaCondiciones(t):
    '''reglaSemanticaCondiciones : valorMatematico COMP_IGUAL valorMatematico
                                | valorMatematico MENOR valorMatematico
                                | valorMatematico MAYOR valorMatematico
                                | valorMatematico DIFERENTE valorMatematico
                                | valorGramatico COMP_IGUAL valorGramatico
                                | valorGramatico DIFERENTE valorGramatico
                                | valorBooleano COMP_IGUAL valorBooleano
                                | valorBooleano DIFERENTE valorBooleano
                                | valorBooleano AND valorBooleano
                                | valorBooleano OR valorBooleano'''

    if t[2] == '===':
        t[0] = t[1] == t[3]
    elif t[2] == '<':
        t[0] = t[1] < t[3]
    elif t[2] == '>':
        t[0] = t[1] > t[3]
    elif t[2] == '!==':
        t[0] = t[1] != t[3]
    elif t[2] == '===':
        t[0] = t[1] == t[3]
    elif t[2] == '!==':
        t[0] = t[1] != t[3]
    elif t[2] == '===':
        t[0] = t[1] == t[3]
    elif t[2] == '!==':
        t[0] = t[1] != t[3]
    elif t[2] == '&&':
        t[0] = t[1] and t[3]
    elif t[0] == '||':
        t[0] = t[1] or t[3]



def p_reglaSemanticEstructuras(t):
    '''reglaSemanticaEstructuras : valorBooleano COMA valorMatematico COMA valorGramatico
                                | valorBooleano COMA valorBooleano COMA valorBooleano
                                | valorMatematico COMA valorMatematico COMA valorMatematico
                                | valorGramatico COMA valorGramatico COMA valorGramatico

    '''


# Error rule for syntax errors

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Todo correcto : {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)

# Build the parser

parser = yacc.yacc()


def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica


if __name__ == '__main__':
    while True:
        try:
            s = input(' ingresa dato >>> ')
        except EOFError:
            continue
        if not s: continue
        # gram = parser.parse(s)
        # print("Resultado ", gram)
        prueba_sintactica(s)
"""
def leerAlgoritmo(file):
    s = file.read()
    print(s)
    result = parser.parse(s)
    print(result)
    file.close()
archivo1 = open("../archivos/AlgoritmoAsqui.txt")
leerAlgoritmo(archivo1)"""