import ply.lex as lex

# Aporte Nicole Asqui

reserved = {
    "var": "VAR",
    "break": "BREAK",
    "continue": "CONTINUE",
    "case": "CASE",
    "else": "ELSE",
    "if": "IF",
    "do": "DO",
    "for": "FOR",
    "in": "IN",
    "return": "RETURN",
    "let": "LET",
    "new": "NEW",
    "while":"WHILE",
    "function":"FUNCTION",
    "switch":"SWITCH",
    "typeof": "TYPEOF",
    "default" : "DEFAULT",
    "push" : "PUSH",
    "pop" : "POP"
}

tokens = [
    "VARIABLE",
    "CONSTANTE",
    "COMP_IGUAL",
    "IGUAL",
    "DIFERENTE",
    "AND",
    "OR",
    "ENTERO",
    "MAS",
    "RESTA",
    "MENOR",
    "MAYOR",
    "CADENA",
    "POTENCIA",
    "DIVISION",
    "PROD",
    "COMENTARIO",
    "PUNTO",
    "INTERROGACION",
    "CIZQ",
    "CDER",
    "LIZQ",
    "LDER",
    "PIZQ",
    "PDER",
    "COMA",
    "PCOMA",
    "MOD",
    "NOT",
    "ASIG",
    "COLON",
    "INC",
    "DEC",
    "EQ_ESTRIC",
    "NOE_ESTRIC",
    "ASIG_SUMA",
    "ASIG_MEN",
    "ASIG_DIV",
    "ASIG_MUL",
    "ASIG_BOR",
    "ASIG_BAN",
    "ASIG_XOR",


] + list(reserved.values())
t_INTERROGACION=r"\?"
t_PUNTO=r"\."
t_AND=r"&&"
t_OR=r"\|\|"
t_IGUAL= r"="
t_COMP_IGUAL=r"=="
t_DIFERENTE=r"!="
t_CIZQ = r"\["
t_CDER = r"\]"
t_LIZQ = r"\{"
t_LDER = r"\}"
t_COMA = r","
t_PCOMA = r";"
t_PIZQ = r"\("
t_PDER = r"\)"
t_MAS = r"\+"
t_ENTERO = r"\d+"
t_RESTA=r"-"
t_MENOR=r"<"
t_MAYOR=r">"
t_CADENA= r'"[a-zA-Z0-9\s,]*"'
t_PROD =r"\*"
t_POTENCIA = r"\*\*"
t_DIVISION=r"/"
t_MOD = r'%'
t_NOT = r'\!'
t_ASIG = r'\='
t_COLON = r'\:'
t_INC = r'\+\+'
t_DEC = r'--'
t_EQ_ESTRIC = r'==='
t_NOE_ESTRIC = r'\!==='


#Expresiones Regulares asignacion
t_ASIG_SUMA = r'\+='
t_ASIG_MEN = r'-='
t_ASIG_DIV = r'/='
t_ASIG_MUL = r'\*='
t_ASIG_BOR = r'\|='
t_ASIG_BAN = r'\&='
t_ASIG_XOR = r'\^='

def t_CONSTANTE(t):
    r"[A-Z][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'CONSTANTE')  # Check for reserved words
    return t
def t_VARIABLE(t):
    r"[a-z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

data = ''' a = + b'''

def analizar(data):
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


def crearArchivo(data):
    fic = open("lexico.txt", "w+")
    lexer.input(data)
    for linea in data:
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input
            fic.write(str(tok))
            fic.write("\n")
        if len(linea) == 0:
            break
    fic.close()
'''
def leerText(txt):
    data=txt.split("\n")
    for linea in data:
        print(">>")
        if len(linea)==0:
            break
        return analizar(linea)
'''
def leer(file):
    for linea in file:
        print(">>" + linea)
        analizar(linea)
        if len(linea) == 0:
            break

archivo = open("../archivos/nicole_asqui.txt")

leer(archivo)