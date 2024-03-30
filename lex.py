import ply.lex as lex

# Lista de nombres de tokens. Esto es obligatorio.
tokens = (
    'T_ABSTRACT',
    'T_AND_EQUAL',
    'T_ARRAY_CAST',
    'T_ARRAY',
    'T_AS',
    'T_ATTRIBUTE',
    'T_BAD_CHARACTER',
    'T_BOOLEAN_AND',
    'T_BOOLEAN_OR',
    'T_BOOL_CAST',
    'T_BREAK',
    'T_CALLABLE',
    'T_CASE',
    'T_CATCH',
    'T_CLASS', 
    'T_CLASS_C', 
    'T_CLONE', 
    'T_CLOSE_TAG', 
    'T_COALESCE', 
    'T_COALESCE_EQUAL', 
    'T_COMMENT', 
    'T_CONCAT_EQUAL', 
    'T_CONST', 
    'T_CONSTANT_ENCAPSED_STRING', 
    'T_CONTINUE', 
    'T_CURLY_OPEN', 
    'T_DEC', 
    'T_DECLARE', 
    'T_DEFAULT', 
    'T_DIR', 
    'T_DIV_EQUAL', 
    'T_DO', 
    'T_DOC_COMMENT', 
    'T_DOLLAR_OPEN_CURLY_BRACES', 
    'T_DOUBLE_ARROW', 
    'T_DOUBLE_CAST', 
    'T_DOUBLE_COLON', 
    'T_ECHO', 
    'T_ELLIPSIS', 
    'T_ELSE', 
    'T_ELSEIF', 
    'T_EMPTY'
    'T_DNUMBER',
    'T_ENCAPSED_AND_WHITESPACE', 
    'T_ENDDECLARE', 
    'T_ENDFOR', 
    'T_ENDFOREACH',
    'T_ENDIF', 
    'T_ENDSWITCH', 
    'T_ENDWHILE', 
    'T_END_HEREDOC', 
    'T_EVAL', 
    'T_EXIT',
    'T_EXTENDS', 
    'T_FILE', 
    'T_FINAL', 
    'T_FINALLY', 
    'T_FN', 
    'T_FOR', 
    'T_FOREACH',
    'T_FUNCTION', 
    'T_FUNC_C', 
    'T_GLOBAL', 
    'T_GOTO', 
    'T_HALT_COMPILER',
    'T_IF', 
    'T_IMPLEMENTS', 
    'T_INC', 
    'T_INCLUDE', 
    'T_INCLUDE_ONCE', 
    'T_INLINE_HTML',
    'T_INSTANCEOF', 
    'T_INSTEADOF', 
    'T_INTERFACE', 
    'T_INT_CAST', 
    'T_ISSET',
    'T_IS_EQUAL', 
    'T_IS_GREATER_OR_EQUAL', 
    'T_IS_IDENTICAL', 
    'T_IS_NOT_EQUAL',
    'T_IS_NOT_IDENTICAL', 
    'T_IS_SMALLER_OR_EQUAL', 
    'T_LINE', 
    'T_LIST',
    'T_LNUMBER',
    'T_LOGICAL_AND',
    'T_LOGICAL_OR', 
    'T_LOGICAL_XOR',
    'T_METHOD_C',
    'T_MINUS_EQUAL',
    'T_MOD_EQUAL', 
    'T_MUL_EQUAL', 
    'T_NAMESPACE', 
    'T_NEW', 
    'T_NS_C',
    'T_NS_SEPARATOR', 
    'T_NUM_STRING', 
    'T_OBJECT_CAST', 
    'T_OBJECT_OPERATOR',
    'T_NULLSAFE_OBJECT_OPERATOR', 
    'T_OPEN_TAG', 
    'T_OPEN_TAG_WITH_ECHO',
    'T_OR_EQUAL', 
    'T_PAAMAYIM_NEKUDOTAYIM', 
    'T_PLUS_EQUAL', 
    'T_POW',
    'T_POW_EQUAL',
    'T_PRINT',
    'T_PRIVATE', 
    'T_PROTECTED', 
    'T_PUBLIC', 
    'T_REQUIRE', 
    'T_REQUIRE_ONCE',
    'T_RETURN', 
    'T_SL', 
    'T_SL_EQUAL', 
    'T_SPACESHIP', 
    'T_SR', 
    'T_SR_EQUAL',
    'T_START_HEREDOC', 
    'T_STATIC',
    'T_STRING', 
    'T_STRING_CAST', 
    'T_STRING_VARNAME', 
    'T_SWITCH', 
    'T_THROW',
    'T_TRAIT', 
    'T_TRAIT_C', 
    'T_TRY', 
    'T_UNSET', 
    'T_UNSET_CAST', 
    'T_USE',
    'T_VAR'
    'T_VARIABLE',
    'T_WHILE', 
    'T_XOR_EQUAL', 
    'T_YIELD', 
    'T_YIELD_FROM',
)

# Reglas de expresiones regulares para tokens simples.
t_T_ABSTRACT = r'abstract'
t_T_AND_EQUAL = r'&='
t_T_ARRAY = r'array()'
t_T_ARRAY_CAST = r'(array)'
t_T_AS = r'as'
t_T_ATTRIBUTE = r'#['
t_T_BOOLEAN_AND = r'&&'
t_T_BOOLEAN_OR = r'\|\|'
t_T_BOOL_CAST = r'(bool)|(boolean)'
t_T_BREAK = r'break'
t_T_CALLABLE = r'callable'
t_T_CASE = r'case'
t_T_CATCH = r'catch'
t_T_CLASS = r'class'
t_T_CLASS_C = r'__CLASS__'
t_T_CLONE = r'clone'
t_T_CLOSE_TAG = r'\?>|%\>'
t_T_COALESCE = r'\?\?'
t_T_COALESCE_EQUAL = r'\?\?='
# Para comentarios, este puede ser simplificado ya que PLY maneja los comentarios de manera automática
t_T_CONCAT_EQUAL = r'\.='
t_T_CONST = r'const'
t_T_CONSTANT_ENCAPSED_STRING = r'\".*?\"|\\\'.*?\\\''
t_T_CONTINUE = r'continue'
# Las reglas para T_CURLY_OPEN y T_DOLLAR_OPEN_CURLY_BRACES pueden ser más complejas y dependen de cómo manejes la sintaxis compleja en tu analizador
t_T_DEC = r'--'
t_T_DECLARE = r'declare'
t_T_DEFAULT = r'default'
t_T_DIR = r'__DIR__'
t_T_DIV_EQUAL = r'/='
t_T_DO = r'do'
# Los comentarios tipo PHPDoc también pueden ser manejados automáticamente por PLY, dependiendo de cómo quieras procesarlos
t_T_DOUBLE_ARROW = r'=>'
t_T_DOUBLE_CAST = r'\(real\)|\(double\)|\(float\)'
# T_DOUBLE_COLON es alias de T_PAAMAYIM_NEKUDOTAYIM, que no está definido en esta lista
t_T_ECHO = r'echo'
t_T_ELLIPSIS = r'\.\.\.'
t_T_ELSE = r'else'
t_T_ELSEIF = r'elseif'
t_T_EMPTY = r'empty'
t_T_ENCAPSED_AND_WHITESPACE = r'\"\s*\$[a-zA-Z_][a-zA-Z_0-9]*\"'
t_T_ENDDECLARE = r'enddeclare'
t_T_ENDFOR = r'endfor'
t_T_ENDFOREACH = r'endforeach'
t_T_ENDIF = r'endif'
t_T_ENDSWITCH = r'endswitch'
t_T_ENDWHILE = r'endwhile'
t_T_EVAL = r'eval\(\)'
t_T_EXIT = r'exit|die'
t_T_EXTENDS = r'extends'
t_T_FILE = r'__FILE__'
t_T_FINAL = r'final'
t_T_FINALLY = r'finally'
t_T_FN = r'fn'
t_T_FOR = r'for'
t_T_FOREACH = r'foreach'
t_T_FUNCTION = r'function'
t_T_FUNC_C = r'__FUNCTION__'
t_T_GLOBAL = r'global'
t_T_GOTO = r'goto'
t_T_HALT_COMPILER = r'__halt_compiler\(\)'
t_T_IF = r'if'
t_T_IMPLEMENTS = r'implements'
t_T_INC = r'\+\+'
t_T_INCLUDE = r'include'
t_T_INCLUDE_ONCE = r'include_once'
# T_INLINE_HTML es especial y podría requerir un enfoque diferente dependiendo de cómo manejes HTML fuera de PHP
t_T_INSTANCEOF = r'instanceof'
t_T_INSTEADOF = r'insteadof'
t_T_INTERFACE = r'interface'
t_T_INT_CAST = r'\(int\)|\(integer\)'
t_T_ISSET = r'isset'
t_T_IS_EQUAL = r'=='
t_T_IS_GREATER_OR_EQUAL = r'>='
t_T_IS_IDENTICAL = r'==='
t_T_IS_NOT_EQUAL = r'!=|<>'
t_T_IS_NOT_IDENTICAL = r'!=='
t_T_IS_SMALLER_OR_EQUAL = r'<='
t_T_LINE = r'__LINE__'
t_T_LIST = r'list'
t_T_LOGICAL_AND = r'and'
t_T_LOGICAL_OR = r'or'
t_T_LOGICAL_XOR = r'xor'
t_T_METHOD_C = r'__METHOD__'
t_T_MINUS_EQUAL = r'-='
t_T_MOD_EQUAL = r'%='
t_T_MUL_EQUAL = r'\*='
t_T_NAMESPACE = r'namespace'
t_T_NEW = r'new'
t_T_NS_C = r'__NAMESPACE__'
t_T_NS_SEPARATOR = r'\\'
# T_NUM_STRING podría requerir un enfoque especial para manejar correctamente los contextos en los que aparece
t_T_OBJECT_CAST = r'\(object\)'
t_T_OBJECT_OPERATOR = r'->'
t_T_NULLSAFE_OBJECT_OPERATOR = r'\?->'
t_T_OPEN_TAG = r'<\?(php)?'
t_T_OPEN_TAG_WITH_ECHO = r'<\?='
t_T_OR_EQUAL = r'\|='
t_T_PAAMAYIM_NEKUDOTAYIM = r'::'  # También conocido como T_DOUBLE_COLON
t_T_PLUS_EQUAL = r'\+='
t_T_POW = r'**'
t_T_POW_EQUAL = r'**='
t_T_PRINT = r'print'
t_T_PRIVATE = r'private'
t_T_PROTECTED = r'protected'
t_T_PUBLIC = r'public'
t_T_REQUIRE = r'require'
t_T_REQUIRE_ONCE = r'require_once'
t_T_RETURN = r'return'
t_T_SL = r'<<'
t_T_SL_EQUAL = r'<<='
t_T_SPACESHIP = r'<=>'
t_T_SR = r'>>'
t_T_SR_EQUAL = r'>>='
# La sintaxis de Heredoc puede ser complicada de manejar; esta es una simplificación
t_T_START_HEREDOC = r'<<<'
t_T_STATIC = r'static'
t_T_STRING_CAST = r'\(string\)'
# T_STRING_VARNAME captura la sintaxis compleja de las variables dentro de strings
t_T_STRING_VARNAME = r'\$\{[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*'
t_T_SWITCH = r'switch'
t_T_THROW = r'throw'
t_T_TRAIT = r'trait'
t_T_TRAIT_C = r'__TRAIT__'
t_T_TRY = r'try'
t_T_UNSET = r'unset'
t_T_UNSET_CAST = r'\(unset\)'
t_T_USE = r'use'
t_T_VAR = r'var'
t_T_WHILE = r'while'
t_T_XOR_EQUAL = r'^='
t_T_YIELD = r'yield'
t_T_YIELD_FROM = r'yield from'

def t_T_INLINE_HTML(t):
    r'.+?(?=<\?php)|.+$'
    pass  # Aquí decides si ignorar el contenido HTML o manejarlo de alguna manera

# Una regla más compleja con una función de acción. Esto captura números enteros.
def t_T_LNUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Para números de punto flotante.
def t_T_DNUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Cadena simple para capturar palabras como identificadores/strings.
def t_T_STRING(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_T_NUM_STRING(t):
    r'\"\$[a-zA-Z_][a-zA-Z_0-9]*\[\d+\]\"'
    return t

# Variables (esto es bastante simplificado).
def t_T_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Ignorar espacios y tabs.
t_ignore = ' \t\r\n'


# Ignorar comentarios de una y varias líneas
def t_T_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*?\n)|(#.*?\n)'
    pass  # Token is ignored

# Ignorar comentarios tipo PHPDoc
def t_T_DOC_COMMENT(t):
    r'/\*\*(.|\n)*?\*/'
    pass  # Token is ignored


# Una regla para manejar errores.
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def t_T_BAD_CHARACTER(t):
    r'.'
    print(f"Bad character '{t.value}'")
    return t

# Construye el lexer
lexer = lex.lex()

# Para probarlo, vamos a alimentarlo con un string de entrada.
input_string = "if $variable1 == 10 while echo 123"
lexer.input(input_string)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
