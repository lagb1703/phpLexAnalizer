import ply.lex as lex

# Lista de nombres de tokens. Esto es obligatorio.
tokens = (
    #palabras reservadas de php
    '__halt_compiler',
    'abstract',
    'and',
    'array',
    'as',
    'break',
    'callable',
    'case',
    'catch',
    'class',
    'clone',
    'const',
    'continue',
    'declare',
    'default',
    'die',
    'do',
    'echo',
    'else',
    'elseif',
    'empty',
    'enddeclare',
    'endfor',
    'endforeach',
    'endif',
    'endswitch',
    'endwhile',
    'eval',
    'exit',
    'extends',
    'final',
    'for',
    'foreach',
    'function',
    'global',
    'goto',
    'if',
    'implements',
    'include', 
    'include_once',
    'instanceof',
    'insteadof',
    'interface',
    'isset',
    'list',
    'namespace',
    'new',
    'or',
    'print',
    'private',
    'protected',
    'public',
    'require',
    'require_once',
    'return',
    'static',
    'switch',
    'throw',
    'trait',
    'try',
    'unset',
    'use',
    'var',
    'while',
    'xor',
    'yield',
    'yield from',
    #palabras reservadas de constantes en el tiempo de compilacion
    '__CLASS__',
    '__DIR__',
    '__FILE__',
    '__FUNCTION__',
    '__LINE__',
    '__METHOD__',
    '__NAMESPACE__',
    '__TRAIT__',
    #toca ver pero son tokens de php
    #creo que son symbols
    #falta 
    'T_AND_EQUAL',
    'T_ARRAY_CAST', #!tengo que verla nota
    'T_ARRAY',  #!tengo que verla nota
    'T_ATTRIBUTE',
    'T_BAD_CHARACTER',
    'T_BOOLEAN_AND',
    'T_BOOLEAN_OR',
    'T_BOOL_CAST',
    'T_CLOSE_TAG', 
    'T_COALESCE', 
    'T_COALESCE_EQUAL', 
    'T_COMMENT', 
    'T_CONCAT_EQUAL', 
    
    'T_CONSTANT_ENCAPSED_STRING', 
   
    'T_CURLY_OPEN', 
    'T_DEC', 

    'T_DIV_EQUAL', 
    'T_DO', 
    'T_DOC_COMMENT', 
    'T_DOLLAR_OPEN_CURLY_BRACES', 
    'T_DOUBLE_ARROW', 
    'T_DOUBLE_CAST', 
    'T_DOUBLE_COLON', 

    'T_ELLIPSIS', 
    
    'T_DNUMBER',
    'T_ENCAPSED_AND_WHITESPACE', 
    
    'T_END_HEREDOC', 
    'T_EVAL', #!tengo que verla nota
    
    'T_HALT_COMPILER', #!tengo que verla nota
    
    'T_INC', 
    'T_INCLUDE', #!tengo que verla nota
    'T_INCLUDE_ONCE', #!tengo que verla nota
    'T_INLINE_HTML',
    
    'T_INT_CAST', 
    'T_ISSET', #!tengo que verla nota
    'T_IS_EQUAL', 
    'T_IS_GREATER_OR_EQUAL', 
    'T_IS_IDENTICAL', 
    'T_IS_NOT_EQUAL',
    'T_IS_NOT_IDENTICAL', 
    'T_IS_SMALLER_OR_EQUAL', 

    'T_LIST',#!tengo que verla nota
    'T_LNUMBER',
    
    
    'T_MINUS_EQUAL',
    'T_MOD_EQUAL', 
    'T_MUL_EQUAL', 
    
    'T_NS_SEPARATOR', 
    'T_NUM_STRING', 
    'T_OBJECT_CAST', #!tengo que verla nota
    'T_OBJECT_OPERATOR',
    'T_NULLSAFE_OBJECT_OPERATOR', 
    'T_OPEN_TAG', 
    'T_OPEN_TAG_WITH_ECHO',
    'T_OR_EQUAL', 
    'T_PAAMAYIM_NEKUDOTAYIM', 
    'T_PLUS_EQUAL', 
    'T_POW',
    'T_POW_EQUAL',
    'T_PRINT', #!tengo que verla nota
    
    'T_SL', 
    'T_SL_EQUAL', 
    'T_SPACESHIP', 
    'T_SR', 
    'T_SR_EQUAL',
    'T_START_HEREDOC', 

    'T_STRING', 
    'T_STRING_CAST', 
    'T_STRING_VARNAME', 
    
    'T_VARIABLE',

    'T_XOR_EQUAL', 
)

# Reglas de expresiones regulares para tokens simples.
t_T_AND_EQUAL = r'&='
t_T_ARRAY = r'array()' #!tengo que verla nota
t_T_ARRAY_CAST = r'(array)' #!tengo que verla nota
t_T_ATTRIBUTE = r'#['
t_T_BOOLEAN_AND = r'&&'
t_T_BOOLEAN_OR = r'\|\|'
t_T_BOOL_CAST = r'(bool)|(boolean)' #!tengo que verla nota
t_T_CLOSE_TAG = r'\?>|%\>'
t_T_COALESCE = r'\?\?'
t_T_COALESCE_EQUAL = r'\?\?='
# Para comentarios, este puede ser simplificado ya que PLY maneja los comentarios de manera automática
t_T_CONCAT_EQUAL = r'\.='
t_T_CONSTANT_ENCAPSED_STRING = r'\".*?\"|\\\'.*?\\\''
# Las reglas para T_CURLY_OPEN y T_DOLLAR_OPEN_CURLY_BRACES pueden ser más complejas y dependen de cómo manejes la sintaxis compleja en tu analizador
t_T_DEC = r'--'
t_T_DIV_EQUAL = r'/='
# Los comentarios tipo PHPDoc también pueden ser manejados automáticamente por PLY, dependiendo de cómo quieras procesarlos
t_T_DOUBLE_ARROW = r'=>'
t_T_DOUBLE_CAST = r'\(real\)|\(double\)|\(float\)'
# T_DOUBLE_COLON es alias de T_PAAMAYIM_NEKUDOTAYIM, que no está definido en esta lista
t_T_ELLIPSIS = r'\.\.\.'
t_T_ENCAPSED_AND_WHITESPACE = r'\"\s*\$[a-zA-Z_][a-zA-Z_0-9]*\"'
t_T_EVAL = r'eval\(\)' #!tengo que verla nota
t_T_EXIT = r'exit|die'  #!tengo que verla nota
t_T_HALT_COMPILER = r'__halt_compiler\(\)' #!tengo que verla nota
t_T_INC = r'\+\+'
# T_INLINE_HTML es especial y podría requerir un enfoque diferente dependiendo de cómo manejes HTML fuera de PHP
t_T_INT_CAST = r'\(int\)|\(integer\)'
t_T_IS_EQUAL = r'=='
t_T_IS_GREATER_OR_EQUAL = r'>='
t_T_IS_IDENTICAL = r'==='
t_T_IS_NOT_EQUAL = r'!=|<>'
t_T_IS_NOT_IDENTICAL = r'!=='
t_T_IS_SMALLER_OR_EQUAL = r'<='
t_T_MINUS_EQUAL = r'-='
t_T_MOD_EQUAL = r'%='
t_T_MUL_EQUAL = r'\*='
t_T_NS_SEPARATOR = r'\\'
# T_NUM_STRING podría requerir un enfoque especial para manejar correctamente los contextos en los que aparece
t_T_OBJECT_CAST = r'\(object\)' #!tengo que verla nota
t_T_OBJECT_OPERATOR = r'->'
t_T_NULLSAFE_OBJECT_OPERATOR = r'\?->'
t_T_OPEN_TAG = r'<\?(php)?'
t_T_OPEN_TAG_WITH_ECHO = r'<\?='
t_T_OR_EQUAL = r'\|='
t_T_PAAMAYIM_NEKUDOTAYIM = r'::'  # También conocido como T_DOUBLE_COLON
t_T_PLUS_EQUAL = r'\+='
t_T_POW = r'**'
t_T_POW_EQUAL = r'**='
t_T_SL = r'<<'
t_T_SL_EQUAL = r'<<='
t_T_SPACESHIP = r'<=>'
t_T_SR = r'>>'
t_T_SR_EQUAL = r'>>='
# La sintaxis de Heredoc puede ser complicada de manejar; esta es una simplificación
t_T_START_HEREDOC = r'<<<'
t_T_STRING_CAST = r'\(string\)'
# T_STRING_VARNAME captura la sintaxis compleja de las variables dentro de strings
t_T_STRING_VARNAME = r'\$\{[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*'
t_T_UNSET_CAST = r'\(unset\)'
t_T_XOR_EQUAL = r'^='

#palabras reservadas declaracion
def t_abstract(t):
    r'abstract'
    return t
def t_and(t):
    r'and'
    return t
def t_array(t):
    r'array'
    return t
def t_as(t):
    r'as'
    return t
def t_break(t):
    r'break'
    return t
def t_callable(t):
    r'callable'
    return t
def t_case(t):
    r'case'
    return t
def t_catch(t):
    r'catch'
    return t
def t_class(t):
    r'class'
    return t
def t_clone(t):
    r'clone'
    return t
def t_const(t):
    r'const'
    return t
def t_continue(t):
    r'continue'
    return t
def t_declare(t):
    r'declare'
    return t
def t_default(t):
    r'default'
    return t
def t_die(t):
    r'die'
    return t
def t_do(t):
    r'do'
    return t
def t_echo(t):
    r'echo'
    return t
def t_else(t):
    r'else'
    return t
def t_elseif(t):
    r'elseif'
    return t
def t_empty(t):
    r'empty'
    return t
def t_enddeclare(t):
    r'enddeclare'
    return t
def t_endfor(t):
    r'endfor'
    return t
def t_endforeach(t):
    r'endforeach'
    return t
def t_endif(t):
    r'endif'
    return t
def t_endswitch(t):
    r'endswitch'
    return t
def t_endwhile(t):
    r'endwhile'
    return t
def t_eval(t):
    r'eval'
    return t
def t_exit(t):
    r'exit'
    return t
def t_extends(t):
    r'extends'
    return t
def t_final(t):
    r'final'
    return t
def t_for(t):
    r'for'
    return t
def t_foreach(t):
    r'foreach'
    return t
def t_function(t):
    r'function'
    return t
def t_global(t):
    r'global'
    return t
def t_goto(t):
    r'goto'
    return t
def t_if(t):
    r'if'
    return t
def t_implements(t):
    r'implements'
    return t
def t_include(t):
    r'include'
    return t
def t_include_once(t):
    r'include_once'
    return t
def t_instanceof(t):
    r'instanceof'
    return t
def t_insteadof(t):
    r'insteadof'
    return t
def t_interface(t):
    r'interface'
    return t
def t_isset(t):
    r'isset'
    return t
def t_list(t):
    r'list'
    return t
def t_namespace(t):
    r'namespace'
    return t
def t_new(t):
    r'new'
    return t
def t_or(t):
    r'or'
    return t
def t_print(t):
    r'print'
    return t
def t_private(t):
    r'private'
    return t
def t_protected(t):
    r'protected'
    return t
def t_public(t):
    r'public'
    return t
def t_require(t):
    r'require'
    return t
def t_require_once(t):
    r'require_once'
    return t
def t_return(t):
    r'return'
    return t
def t_static(t):
    r'static'
    return t
def t_switch(t):
    r'switch'
    return t
def t_throw(t):
    r'throw'
    return t
def t_trait(t):
    r'trait'
    return t
def t_try(t):
    r'try'
    return t
def t_unset(t):
    r'unset'
    return t
def t_use(t):
    r'use'
    return t
def t_var(t):
    r'var'
    return t
def t_while(t):
    r'while'
    return t
def t_xor(t):
    r'xor'
    return t
def t_yield(t):
    r'yield'
    return t
def t_yield_from(t):
    r'yield from'
    return t
def t___CLASS__(t):
    r'__CLASS__'
    return t
def t___DIR__(t):
    r'__DIR__'
    return t
def t___FILE__(t):
    r'__FILE__'
    return t
def t___FUNCTION__(t):
    r'__FUNCTION__'
    return t
def t___LINE__(t):
    r'__LINE__'
    return t
def t___METHOD__(t):
    r'__METHOD__'
    return t
def t___NAMESPACE__(t):
    r'__NAMESPACE__'
    return t
def t___TRAIT__(t):
    r'__TRAIT__'
    return t
#hasta qui las palabras reservadas de php


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