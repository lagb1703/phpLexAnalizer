"""

Analizador léxico

Hecho por : 

- Luis alejandro Giraldo Bolaños
- Stiven Castro Soto
- Juan Camilo Galvis Agudelo

"""

import ply.lex as lex
from ply.lex import TOKEN
import sys

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
    'YIELDFROM',
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
    'AND_EQUAL',
    # 'ARRAY_CAST',
    'ATTRIBUTE',
    #----------------------------------
    'BOOLEAN_AND',
    'BOOLEAN_OR',
    # 'BOOL_CAST',
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
    # 'DOUBLE_CAST', 
    'DOUBLE_COLON', 
    'ELLIPSIS',    
    'DNUMBER', 
    'INC', 
    # 'INLINE_HTML',
    # 'INT_CAST', 
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
    # 'NUM_STRING', 
    # 'OBJECT_CAST', 
    'OBJECT_OPERATOR',
    'NULLSAFE_OBJECT_OPERATOR', 
    'OPEN_TAG', 
    'OPEN_TAG_WITH_ECHO',
    'OR_EQUAL', 
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
    # 'STRING_CAST', 
    # 'STRING_VARNAME', 
    'VARIABLE',
    'WHITESPACE',
    'XOR_EQUAL', 
    # Tokens que no maneja php de por si
    'EQUAL',
    'RIGHT_PARENTHESIS',
    'LEFT_PARENTHESIS',
    'SEMICOLON',
    'COLON',
    'RIGHT_CBRAC',
    'LEFT_CBRAC',
    'RIGHT_SQRBRAC',
    'LEFT_SQRBRAC',
    'ASTERISK',
    'CONCAT',
    'DIVIDE',
    'DQUOTATION_MARK',
    'AMPERSAND',
    'NEGATION',
    'MORE_THAN',
    'LESS_THAN' ,
    'BITWISE_XOR',
    'BITWISE_NOT',
    'BITWISE_OR',
    'TERNARY_OPERATION' ,
    'DOUBLE_POINT' ,
    'BAD_CARACTER',
    'EXPONENT_DNUMBER',
    #----------------------------------
    'PLUS',
    'LESS'
)

#palabras reservadas declaracion de php
def t_HALT_COMPILER(t): 
    r'__halt_compiler'
    return t
def t_ABSTRACT(t):
    r'abstract'
    return t
def t_LOGICAL_AND(t):
    r'and'
    return t
def t_ARRAY(t):
    r'array'
    return t
def t_AS(t):
    r'as'
    return t
def t_BREAK(t):
    r'break'
    return t
def t_CALLABLE(t):
    r'callable'
    return t
def t_CASE(t):
    r'case'
    return t
def t_CATCH(t):
    r'catch'
    return t
def t_CLASS(t):
    r'class'
    return t
def t_CLONE(t):
    r'clone'
    return t
def t_CONST(t):
    r'const'
    return t
def t_CONTINUE(t):
    r'continue'
    return t
def t_DECLARE(t):
    r'declare'
    return t
def t_DEFAULT(t):
    r'default'
    return t
def t_DO(t):
    r'do'
    return t
def t_ECHO(t):
    r'echo'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_ELSEIF(t):
    r'elseif'
    return t
def t_EMPTY(t):
    r'empty'
    return t
def t_ENDDECLARE(t):
    r'enddeclare'
    return t
def t_ENDFOREACH(t):
    r'endforeach'
    return t
def t_ENDFOR(t):
    r'endfor'
    return t
def t_ENDIF(t):
    r'endif'
    return t
def t_ENDSWITCH(t):
    r'endswitch'
    return t
def t_ENDWHILE(t):
    r'endwhile'
    return t
def t_EVAL(t): 
    r'eval'
    return t
def t_EXIT(t):
    r'exit | die'
    return t
def t_EXTENDS(t):
    r'extends'
    return t
def t_FINALLY(t):
    r'finally'
    return t
def t_FINAL(t):
    r'final'
    return t
def t_FN(t):
    r'fn'
    return t
def t_FOREACH(t):
    r'foreach'
    return t
def t_FOR(t):
    r'for'
    return t
def t_FUNCTION(t):
    r'function'
    return t
def t_GLOBAL(t):
    r'global'
    return t
def t_GOTO(t):
    r'goto'
    return t
def t_IF(t):
    r'if'
    return t
def t_IMPLEMENTS(t):
    r'implements'
    return t
def t_INCLUDE_ONCE(t):
    r'include_once'
    return t
def t_INCLUDE(t):
    r'include'
    return t
def t_INSTANCEOF(t):
    r'instanceof'
    return t
def t_INSTEADOF(t):
    r'insteadof'
    return t
def t_INTERFACE(t):
    r'interface'
    return t
def t_ISSET(t):
    r'isset'
    return t
def t_LIST(t):
    r'list'
    return t
def t_NAMESPACE(t):
    r'namespace'
    return t
def t_NEW(t):
    r'new'
    return t
def t_LOGICAL_OR(t):
    r'or'
    return t
def t_PRINT(t):
    r'print'
    return t
def t_PRIVATE(t):
    r'private'
    return t
def t_PROTECTED(t):
    r'protected'
    return t
def t_PUBLIC(t):
    r'public'
    return t
def t_REQUIRE_ONCE(t): 
    r'require_once'
    return t
def t_REQUIRE(t): 
    r'require'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_STATIC(t):
    r'static'
    return t
def t_SWITCH(t):
    r'switch'
    return t
def t_THROW(t):
    r'throw'
    return t
def t_TRAIT(t):
    r'trait'
    return t
def t_TRY(t):
    r'try'
    return t
def t_UNSET(t):
    r'unset'
    return t
def t_USE(t):
    r'use'
    return t
def t_VAR(t):
    r'var'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_LOGICAL_XOR(t):
    r'xor'
    return t
def t_YIELD_FROM(t):
    r'yield from'
    return t
def t_YIELD(t):
    r'yield'
    return t
def t_CLASS_C(t):
    r'__CLASS__'
    return t
def t_DIR(t):
    r'__DIR__'
    return t
def t_FILE(t):
    r'__FILE__'
    return t
def t_FUNC_C(t):
    r'__FUNCTION__'
    return t
def t_LINE(t):
    r'__LINE__'
    return t
def t_METHOD_C(t):
    r'__METHOD__'
    return t
def t_NS_C(t):
    r'__NAMESPACE__'
    return t
def t_TRAIT_C(t):
    r'__TRAIT__'
    return t
#hasta qui las palabras reservadas de php
#simbolos no simples de php
def t_AND_EQUAL(t):
    r'&='
    return t
# def t_ARRAY_CAST(t):
#     r'\(array\)'
#     return t
def t_ATTRIBUTE(t): 
    r'\#\[.*?\]'
    return t
def t_BOOLEAN_AND(t):
    r'&&'
    return t
def t_BOOLEAN_OR(t):
    r'\|\|'
    return t
# def t_BOOL_CAST(t):
#     r'\(bool\) | \(boolean\)'
#     return t
def t_CLOSE_TAG(t):
    r'\?> | \%\>'
    return t
def t_COALESCE(t):
    r'\?\?'
    return t
def t_COALESCE_EQUAL(t):
    r'\?\?='
    return t
def t_CONCAT_EQUAL(t):
    r'\.='
    return t
# def t_STRING_VARNAME(t): #nombre de variable dentro de un string
#     r'\"(. | \b)*?\$\{[a-zA-Z_][a-zA-Z0-9_]*\}'
#     return t
def t_CONSTANT_ENCAPSED_STRING(t): #captura strings dentro de comillas simples o dobles 
    r'(\'[^\']*\' | \"[^\"]*\")'
    return t
def t_CURLY_OPEN(t):
    r'\$\{'
    return t
def t_DEC(t):
    r'--'
    return t
def t_DIV_EQUAL(t):
    r'/='
    return t
def t_DOLLAR_OPEN_CURLY_BRACES(t):
    r'\$\{'
    return t
def t_DOUBLE_ARROW(t):
    r'=>'
    return t
# def t_DOUBLE_CAST(t):
#     r'\(double\) | \(float\) | \(real\)'
#     return t
def t_DOUBLE_COLON(t):
    r'::'
    return t
def t_ELLIPSIS(t):
    r'\.\.\.'
    return t
def t_VARIABLE(t):
    r'\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9 _\x7f-\xff]*'
    return t

number = r'([+-]?(([1-9][0-9]* | 0) | 0[0-7]+ | 0[xX][0-9a-fA-F]+ | 0b[01]+))'
dnumber = r'(' + number + r'(\. [0-9]*))'   
exponent_dnumber = r'(' + dnumber + r'(e[-]?[0-9]+))' 

#Para t_BAD_CARACTER ---------------------------------

bad_exponent_dnumber = r'(' + dnumber + r'(e))'
bad_number = r'(([a-zA-Z_\x7f-\xff])*\$[a-zA-Z0-9_\x7f-\xff]*|[0-9]+[a-zA-Z_\x7f-\xff]+[0-9]*)'
lex_error = r'(' + bad_exponent_dnumber + r'|' + bad_number + r')'

@TOKEN(lex_error)
def t_BAD_CARACTER(t):
    print ("Lexical error: " + str(t.value))
    t.lexer.skip(1)

#----------------------------------------------------

@TOKEN(exponent_dnumber)
def t_EXPONENT_DNUMBER(t): #numero decimal con exponente  
    return t

@TOKEN(dnumber)
def t_DNUMBER(t): #numero decimal
    return t

@TOKEN(number)
def t_LNUMBER(t): #numero entero
    return t

def t_INC(t):
    r'\+\+'
    return t
# def t_INLINE_HTML(t): 
#     r'<\?php\s+(.*?)(?:\?>|$)'
#     return t
def t_IS_EQUAL(t):
    r'=='
    return t
def t_IS_GREATER_OR_EQUAL(t):
    r'>='
    return t
def t_IS_IDENTICAL(t):
    r'==='
    return t
def t_IS_NOT_EQUAL(t):
    r'!= | <>'
    return t
def t_IS_NOT_IDENTICAL(t):
    r'!=='
    return t
def t_IS_SMALLER_OR_EQUAL(t):
    r'<='
    return t
def t_MINUS_EQUAL(t):
    r'-='
    return t
def t_MOD_EQUAL(t):
    r'%='
    return t
def t_MUL_EQUAL(t):
    r'\*='
    return t
# def t_NUM_STRING(t): 
#     r'\[(\?<indices>\d+(?:,\d+)*)\]'
#     return t
# def t_OBJECT_CAST(t): 
#     r'\(object\)'
#     return t
def t_OBJECT_OPERATOR(t):
    r'->'
    return t
def t_NULLSAFE_OBJECT_OPERATOR(t):
    r'\?->'
    return t
def t_OPEN_TAG(t):
    r'<\?php | <% | <\?'
    return t
def t_OPEN_TAG_WITH_ECHO(t):
    r'<\?= | <%='
    return t
def t_OR_EQUAL(t):
    r'\|='
    return t
def t_PLUS_EQUAL(t):
    r'\+='
    return t
def t_POW(t):
    r'\*\*'
    return t
def t_POW_EQUAL(t):
    r'\*\*='
    return t
def t_START_HEREDOC(t): 
    r'<<<'
    return t
def t_SL(t):
    r'<<'
    return t
def t_SL_EQUAL(t):
    r'<<='
    return t
def t_SPACESHIP(t):
    r'<=>'
    return t
def t_SR(t):
    r'>>'
    return t
def t_SR_EQUAL(t):
    r'>>='
    return t
def t_STRING(t):
    r'([a-zA-Z_\x7f-\xff^\$][a-zA-Z0-9_\x7f-\xff^\$]*)'
    return t

def t_WHITESPACE(t):
    r'\t | \n | \r'
    return t
def t_XOR_EQUAL(t):
    r'\^='
    return t

# # Ignorar espacios y tabs.

t_ignore = r'\t '

#ignora los comentarios de php

def t_COMMENT(t):
    r'(//.*?\n | /\*.*?\*/ | \#.*?\n)'
    t.lexer.lineno += t.value.count('\n')
def t_DOC_COMMENT(t):
    r'(/\*\*(.|\n)*?\*/)'
    t.lexer.lineno += t.value.count('\n')

# Reglas de expresiones regulares para tokens simples.

t_NS_SEPARATOR = r'\\'
t_EQUAL = r'='
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_RIGHT_CBRAC= r'\}'
t_LEFT_CBRAC= r'\{'
t_RIGHT_SQRBRAC= r'\]'
t_LEFT_SQRBRAC= r'\['
t_SEMICOLON = r'\;'
t_COLON = r'\,'
t_ASTERISK = r'\*'
t_CONCAT = r'\.'
t_DIVIDE = r'/'
t_DQUOTATION_MARK = r'\"'
t_AMPERSAND = r'\&'
t_NEGATION = r'\!'
t_MORE_THAN = r'\>'
t_LESS_THAN = r'\<'
t_BITWISE_XOR = r'\^'
t_BITWISE_NOT = r'\~'
t_BITWISE_OR = r'\|'
t_TERNARY_OPERATION = r'\?'
t_DOUBLE_POINT = r'\:'
t_PLUS = r'\+'
t_LESS = r'-'


# Una regla para manejar errores.
def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)


def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

# Construye el lexer
lexer = lex.lex()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'test.txt'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	#input()