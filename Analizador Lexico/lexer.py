import ply.lex as lex

# Aporte Nicole Asqui
# SPRINT 1: Listar todos los componentes lexicos
# Variables, palabras reservadas, simbolos, caracteres especiales

# Lista de palabras reservadas
reserved = {
    "var": "VAR",
    "break": "BREAK",
    "case": "CASE",
    "else": "ELSE",
    "if": "IF",
    "do": "DO",
    "for": "FOR",
    "in": "IN",
    "return": "RETURN",
    "let": "LET",
    "new": "NEW",
    "while": "WHILE",
    "function": "FUNCTION",
    "switch": "SWITCH",
    "typeof": "TYPEOF",
    "default": "DEFAULT",
    "push": "PUSH",
    "pop": "POP",
    "catch": "CATCH",
    "const": "CONST",
    "continue": "CONTINUE",
    "debugger": "DEBUGGER",
    "finally": "FINALY",
    "instanceof": "INSTANCEOF",
    "this": "THIS",
    "throw": "TRHOW",
    "void": "VOID",
    "try": "TRY",
    "console": "CONSOLE",
    "log": "LOG"
}

# Tokens
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
    "COMILL",
    "ASIG_RESDU",
    "ASIG_EXPO",
    "ASIG_DE_I",
    "ASIG_DE_D",
    "ASIG_DSG",
    "ASIG_OR",
    "ASIG_ANU",
    "COMENTARIO_EN_LINEA",
    "COMENTARIO_MULTILINEA"


] + list(reserved.values())
t_INTERROGACION = r"\?"
t_PUNTO = r"\."
t_AND = r"&&"
t_OR = r"\|\|"
t_IGUAL = r"="
t_COMP_IGUAL = r"=="
t_DIFERENTE = r"!="
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
t_RESTA = r"-"
t_MENOR = r"<"
t_MAYOR = r">"
t_CADENA = r'"[a-zA-Z0-9\s,]*"'
t_PROD = r"\*"
t_POTENCIA = r"\*\*"
t_DIVISION = r"/"
t_MOD = r'%'
t_ASIG = r'\='
t_COLON = r'\:'
t_INC = r'\+\+'
t_DEC = r'--'
t_EQ_ESTRIC = r'==='
t_NOE_ESTRIC = r'\!==='
t_COMILL = r'\"'
t_COMENTARIO_EN_LINEA = r'//.*'



# Expresiones Regulares Asignacion
t_ASIG_SUMA = r'\+='
t_ASIG_MEN = r'-='
t_ASIG_DIV = r'/='
t_ASIG_MUL = r'\*='
t_ASIG_BOR = r'\|='
t_ASIG_BAN = r'\&='
t_ASIG_XOR = r'\^='
t_ASIG_RESDU = r'%='
t_ASIG_EXPO = r'\*\*='
t_ASIG_DE_I = r'<<='
t_ASIG_DE_D = r'>>='
t_ASIG_DSG = r'>>>='
t_ASIG_OR = r'\|\|='
T_ASIG_ANU = r'??='



def t_COMENTARIO_MULTILINEA(t):
    r"/\*(.|\n)*?\*/"
    t.lexer.lineno += t.value.count('\n')
    return t



def t_CONSTANTE(t):
    r"[A-Z][a-zA-Z0-9_!]*"
    t.type = reserved.get(t.value, 'CONSTANTE')  # Check for reserved words
    return t

def t_NOT(t):
    r'(![a-zA-Z]\w*)'
    t.type = reserved.get(t.value, 'NOT')
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

archivo = open("../archivos/grupo12.txt")

leer(archivo)