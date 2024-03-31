import ply.lex as lex

# Lista de nombres de tokens. Esto es obligatorio.
tokens = (
    #palabras reservadas de php
    '__HALT_COMPILER',
    'ABSTRACT',
    'AND',
    'ARRAY',
    'AS',
    'BREAK',
    'CALLABLE',
    'CASE',
    'CATCH',
    'CLASS',
    'CLONE',
    'CONST',
    'CONTINUE',
    'DECLARE',
    'DEFAULT',
    'DIE',
    'DO',
    'ECHO',
    'ELSE',
    'ELSEIF',
    'EMPTY',
    'ENDDECLARE',
    'ENDFOR',
    'ENDFOREACH',
    'ENDIF',
    'ENDSWITCH',
    'ENDWHILE',
    'EVAL',
    'EXIT',
    'EXTENDS',
    'FINAL',
    'FINALLY',
    'FN',
    'FOR',
    'FOREACH',
    'FUNCTION',
    'GLOBAL',
    'GOTO',
    'IF',
    'IMPLEMENTS',
    'INCLUDE',
    'INCLUDE_ONCE',
    'INSTANCEOF',
    'INSTEADOF',
    'INTERFACE',
    'ISSET',
    'LIST',
    'NAMESPACE',
    'NEW',
    'OR',
    'PRINT',
    'PRIVATE',
    'PROTECTED',
    'PUBLIC',
    'REQUIRE',
    'REQUIRE_ONCE',
    'RETURN',
    'STATIC',
    'SWITCH',
    'THROW',
    'TRAIT',
    'TRY',
    'UNSET',
    'USE',
    'VAR',
    'WHILE',
    'XOR',
    'YIELD',
    'YIELD FROM',
    #palabras reservadas de constantes en el tiempo de compilacion
    '__CLASS__',
    '__DIR__',
    '__FILE__',
    '__FUNCTION__',
    '__LINE__',
    '__METHOD__',
    '__NAMESPACE__',
    '__TRAIT__',
    #symbols de php
    #falta revisar que no falte alguno
    #?no hay para + o - o ( o ) ¿revisar?
    'AND_EQUAL',
    'ARRAY_CAST', #!tengo que verla nota
    'ATTRIBUTE',
    'BAD_CHARACTER',
    'BOOLEAN_AND',
    'BOOLEAN_OR',
    'BOOL_CAST',
    'CLOSE_TAG', 
    'COALESCE', 
    'COALESCE_EQUAL', 
    'COMMENT', 
    'CONCAT_EQUAL', 
    'CONSTANT_ENCAPSED_STRING', 
    'CURLY_OPEN', 
    'DEC', 
    'DIV_EQUAL',  
    'DOC_COMMENT', 
    'DOLLAR_OPEN_CURLY_BRACES', 
    'DOUBLE_ARROW', 
    'DOUBLE_CAST', 
    'DOUBLE_COLON', 
    'ELLIPSIS',    
    'DNUMBER',
    'ENCAPSED_AND_WHITESPACE', 
    'END_HEREDOC', 
    'T_INC', 
    'INLINE_HTML',
    'INT_CAST', 
    'IS_EQUAL', 
    'IS_GREATER_OR_EQUAL', 
    'IS_IDENTICAL', 
    'IS_NOT_EQUAL',
    'IS_NOT_IDENTICAL', 
    'IS_SMALLER_OR_EQUAL', 
    'LNUMBER',
    'MINUS_EQUAL',
    'MOD_EQUAL', 
    'MUL_EQUAL', 
    'NS_SEPARATOR', 
    'NUM_STRING', 
    'OBJECT_CAST', #?tengo que verla nota(object no es palabra reservda de php)
    'OBJECT_OPERATOR',
    'NULLSAFE_OBJECT_OPERATOR', 
    'OPEN_TAG', 
    'OPEN_TAG_WITH_ECHO',
    'OR_EQUAL', 
    'PAAMAYIM_NEKUDOTAYIM', 
    'PLUS_EQUAL', 
    'POW',
    'POW_EQUAL',
    'SL', 
    'SL_EQUAL', 
    'SPACESHIP', 
    'SR', 
    'SR_EQUAL',
    'START_HEREDOC', 
    'STRING', 
    'STRING_CAST', 
    'STRING_VARNAME', 
    'VARIABLE',
    'WHITESPACE',
    'XOR_EQUAL', 
)

# Reglas de expresiones regulares para tokens simples.
#?hay que encontrarlas

#palabras reservadas declaracion
#las que tienen revisar a un lado es porque en la lista aparece con un () y falta decidir como tomar esa exprecion
def T_HALT_COMPILER(t):
    r'__halt_compiler\(\)'
    return t
def T_ABSTRACT(t):
    r'abstract'
    return t
def T_LOGICAL_AND(t):
    r'and'
    return t
def T_ARRAY(t):
    r'array'
    return t
def T_AS(t):
    r'as'
    return t
def T_BREAK(t):
    r'break'
    return t
def T_CALLABLE(t):
    r'callable'
    return t
def T_CASE(t):
    r'case'
    return t
def T_CATCH(t):
    r'catch'
    return t
def T_CLASS(t):
    r'class'
    return t
def T_CLONE(t):
    r'clone'
    return t
def T_CONST(t):
    r'const'
    return t
def T_CONTINUE(t):
    r'continue'
    return t
def T_DECLARE(t):
    r'declare'
    return t
def T_DEFAULT(t):
    r'default'
    return t
def T_DO(t):
    r'do'
    return t
def T_ECHO(t):
    r'echo'
    return t
def T_ELSE(t):
    r'else'
    return t
def T_ELSEIF(t):
    r'elseif'
    return t
def T_EMPTY(t):
    r'empty'
    return t
def T_ENDDECLARE(t):
    r'enddeclare'
    return t
def T_ENDFOR(t):
    r'endfor'
    return t
def T_ENDFOREACH(t):
    r'endforeach'
    return t
def T_ENDIF(t):
    r'endif'
    return t
def T_ENDSWITCH(t):
    r'endswitch'
    return t
def T_ENDWHILE(t):
    r'endwhile'
    return t
def T_EVAL(t): #!revisar
    r'eval'
    return t
def T_EXIT(t):
    r'exit | die'
    return t
def T_EXTENDS(t):
    r'extends'
    return t
def T_FINAL(t):
    r'final'
    return t
def T_FINALLY(t):
    r'finally'
    return t
def T_FN(t):
    r'fn'
    return t
def T_FOR(t):
    r'for'
    return t
def T_FOREACH(t):
    r'foreach'
    return t
def T_FUNCTION(t):
    r'function'
    return t
def T_GLOBAL(t):
    r'global'
    return t
def T_GOTO(t):
    r'goto'
    return t
def T_IF(t):
    r'if'
    return t
def T_IMPLEMENTS(t):
    r'implements'
    return t
def T_INCLUDE(t): #!revisar
    r'include'
    return t
def T_INCLUDE_ONCE(t): #!revisa
    r'include_once'
    return t
def T_INSTANCEOF(t):
    r'instanceof'
    return t
def T_INSTEADOF(t):
    r'insteadof'
    return t
def T_INTERFACE(t):
    r'interface'
    return t
def T_ISSET(t): #!revisa
    r'isset'
    return t
def T_LIST(t): #!revisa
    r'list'
    return t
def T_NAMESPACE(t):
    r'namespace'
    return t
def T_NEW(t):
    r'new'
    return t
def T_LOGICAL_OR(t):
    r'or'
    return t
def T_PRINT(t): #!revisa
    r'print\(.*?\)'
    return t
def T_PRIVATE(t):
    r'private'
    return t
def T_PROTECTED(t):
    r'protected'
    return t
def T_PUBLIC(t):
    r'public'
    return t
def T_REQUIRE(t): #!revisar
    r'require'
    return t
def T_REQUIRE_ONCE(t): #!revisar
    r'require_once'
    return t
def T_RETURN(t):
    r'return'
    return t
def T_STATIC(t):
    r'static'
    return t
def T_SWITCH(t):
    r'switch'
    return t
def T_THROW(t):
    r'throw'
    return t
def T_TRAIT(t):
    r'trait'
    return t
def T_TRY(t):
    r'try'
    return t
def T_UNSET(t): #!revisar
    r'unset'
    return t
def T_USE(t):
    r'use'
    return t
def T_VAR(t):
    r'var'
    return t
def T_WHILE(t):
    r'while'
    return t
def T_LOGICAL_XOR(t):
    r'xor'
    return t
def T_YIELD(t):
    r'yield'
    return t
def T_YIELD_FROM(t):
    r'yield from'
    return t
def T_CLASS_C(t):
    r'__CLASS__'
    return t
def T_DIR(t):
    r'__DIR__'
    return t
def T_FILE(t):
    r'__FILE__'
    return t
def T_FUNC_C(t):
    r'__FUNCTION__'
    return t
def T_LINE(t):
    r'__LINE__'
    return t
def T_METHOD_C(t):
    r'__METHOD__'
    return t
def T_NS_C(t):
    r'__NAMESPACE__'
    return t
def T_TRAIT_C(t):
    r'__TRAIT__'
    return t
#hasta qui las palabras reservadas de php
#*FAlta la definicion de los simbolos de php

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