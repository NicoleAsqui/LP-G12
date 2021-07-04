import ply.lex as lex

# Aporte Nicole Asqui
# SPRINT 1: Listar todos los componentes lexicos
# Variables, palabras reservadas, simbolos, caracteres especiales

# resultado del analisis
resultado_lexema = []

# Lista de palabras reservadas
reserved = {
    "var": "VAR",
    "break": "BREAK",
    "case": "CASE",
    "else": "ELSE",
    "if": "IF",
    "do": "DO",
    "for": "FOR",
    "let": "LET",
    "new": "NEW",
    "while": "WHILE",
    "function": "FUNCTION",
    "switch": "SWITCH",
    "default": "DEFAULT",
    "push": "PUSH",
    "join": "JOIN",
    "pop": "POP",
    "const": "CONST",
    "this": "THIS",
    "console": "CONSOLE",
    "log": "LOG",
    "true":"TRUE",
    "false":"FALSE",
    "Set":"SET",
    "add":"ADD",
    "has":"HAS",
    "index": "INDEX",
    "count": "COUNT",
    "len": "LEN",
    "Object": "OBJECT",
    "forEach":"FOREACH"
}

# Tokens
tokens = [
    "VARIABLE",
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
    "PUNTO",
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
    "COLON",
    "DEC",
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
    "COMENTARIO_MULTILINEA",
    "DERECHA"


] + list(reserved.values())
t_PUNTO = r"\."
t_AND = r"&&"
t_OR = r"\|\|"
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
t_IGUAL = r'\='
t_COLON = r'\:'
t_DEC = r'--'
t_COMILL = r'\"'
t_COMENTARIO_EN_LINEA = r'//.*'
t_DERECHA = r'\=>'


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


def t_error( t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

data = ''' a = + b'''

def analizar(data):

    global resultado_lexema
    lexer.input(data)

    resultado_lexema.clear()
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno), str(tok.type),
                                                                          str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)
    return resultado_lexema

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        analizar(data)
        print(resultado_lexema)
"""
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
    
def leerText(txt):
    data=txt.split("\n")
    for linea in data:
        print(">>")
        if len(linea)==0:
            break
        return analizar(linea)

def leer(file):
    for linea in file:
        print(">>" + linea)
        analizar(linea)
        if len(linea) == 0:
            break

archivo = open("../archivos/AlgoritmoAsqui.txt")

leer(archivo) """