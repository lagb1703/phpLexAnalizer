import ply.lex as lex
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
    #?no hay para + o - ni ,¿revisar?
    'AND_EQUAL',
    'ARRAY_CAST', #!tengo que verla nota
    'ATTRIBUTE',
    #----------------------------------
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
    #----------------------------------
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
    'INC', 
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
#palabras reservadas declaracion
#las que tienen revisar a un lado es porque en la lista aparece con un () y falta decidir como tomar esa exprecion
def t_HALT_COMPILER(t): #!revisar
    r'__halt_compiler\(\)'
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
def t_ENDFOR(t):
    r'endfor'
    return t
def t_ENDFOREACH(t):
    r'endforeach'
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
def t_EVAL(t): #!revisar
    r'eval'
    return t
def t_EXIT(t):
    r'exit | die'
    return t
def t_EXTENDS(t):
    r'extends'
    return t
def t_FINAL(t):
    r'final'
    return t
def t_FINALLY(t):
    r'finally'
    return t
def t_FN(t):
    r'fn'
    return t
def t_FOR(t):
    r'for'
    return t
def t_FOREACH(t):
    r'foreach'
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
def t_INCLUDE(t): #!revisar
    r'include'
    return t
def t_INCLUDE_ONCE(t): #!revisa
    r'include_once'
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
def t_ISSET(t): #!revisa
    r'isset'
    return t
def t_LIST(t): #!revisa
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
def t_PRINT(t): #!revisa
    r'print\(.*?\)'
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
def t_REQUIRE(t): #!revisar
    r'require'
    return t
def t_REQUIRE_ONCE(t): #!revisar
    r'require_once'
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
def t_UNSET(t): #!revisar
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
def t_YIELD(t):
    r'yield'
    return t
def t_YIELD_FROM(t):
    r'yield from'
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
#*FAlta la definicion de los simbolos de php
def t_AND_EQUAL(t):
    r'&='
    return t
def t_ARRAY_CAST(t):
    r'\(array\)'
    return t
def t_ATTRIBUTE(t): #!revisar por motivo de la lista 
    r'\#\[.*?\]'
    return t
# def t_BAD_CHARACTER(t): #!revisar no se como tomarlo por lo que este debajo des ascii 32 y sus excepciones
#     r'.'
#     return t
def t_BOOLEAN_AND(t):
    r'&&'
    return t
def t_BOOLEAN_OR(t):
    r'\|\|'
    return t
def t_BOOL_CAST(t):
    r'\(bool\) | \(boolean\)'
    return t
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
def t_CONSTANT_ENCAPSED_STRING(t): #!revisar la expresion regular
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
def t_DOC_COMMENT(t): #!revisar la expresion regular
    r'(/\*\*(.|\n)*?\*/)'
    return t
def t_DOLLAR_OPEN_CURLY_BRACES(t):
    r'\$\{'
    return t
def t_DOUBLE_ARROW(t):
    r'=>'
    return t
def t_DOUBLE_CAST(t):
    r'\(double\) | \(float\) | \(real\)'
    return t
def t_DOUBLE_COLON(t):
    r'::'
    return t
def t_ELLIPSIS(t):
    r'\.\.\.'
    return t
def t_DNUMBER(t): #!revisar la expresion regular (es la de la documentacion de php)
    r'([0-9]*(_[0-9]+)*[\.]{[0-9]+(_[0-9]+)*}) | ({[0-9]+(_[0-9]+)*}[\.][0-9]*(_[0-9]+)*)'
    return t
def t_ENCAPSED_AND_WHITESPACE(t): #!revisar la expresion regular y significado de este token
    r'(?<=\")((?:\\\\.|[^"])+)(?=\")(?=\s|$)'
    return t
def t_END_HEREDOC(t): #!esta no es la expresion regular hay que encontrarla
    r'\?>'
    return t
def t_INC(t):
    r'\+\+'
    return t
def t_INLINE_HTML(t): #!revisar la expresion regular y significado de este token
    r'<\?php\s+(.*?)(?:\?>|$)'
    return t
def t_INT_CAST(t): #*revisar la expresion regular y significado de este token
    r'\(int\) | \(integer\)'
    return t
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
def t_LNUMBER(t): #!revisar la expresion regular (es la de la documentacion de php)
    r'([+-]?(([1-9][0-9]* | 0) | 0[0-7]+ | 0[xX][0-9a-fA-F]+ | 0b[01]+))'
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
def t_NUM_STRING(t): #!revisar la expresion regular y significado de este token
    r'\[(\?<indices>\d+(?:,\d+)*)\]'
    return t
def t_OBJECT_CAST(t): #*revisar la expresion regular y significado de este token
    r'\(object\)'
    return t
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
def t_PAAMAYIM_NEKUDOTAYIM(t): # todo: esta se repite con T_DOUBLE_COLON revisar
    r'::'
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
def t_START_HEREDOC(t): #todo mor revisar heredoc
    r'<<<'
    return t
def t_STRING(t): #!revisar la expresion regular
    r'([a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)'
    return t
def t_STRING_CAST(t): #*revisar la expresion regular y significado de este token
    r'\(string\)'
    return t
def t_STRING_VARNAME(t): #!revisar la expresion regular y significado de este token
    r'\$\{\(?<name>[a-zA-Z_][a-zA-Z0-9_]*\)\}'
    return t
def t_VARIABLE(t): #!revisar la expresion regular
    r'\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'
    return t
def t_WHITESPACE(t): #*revisar la expresion regular (es la de la documentacion de php)
    r'\t | \n | \r'
    return t
def t_XOR_EQUAL(t):
    r'\^='
    return t

# # Ignorar espacios y tabs.

t_ignore = r'\t |\r |\n'

def t_COMMENT(t):
    r'(//.*?\n | /\*.*?\*/ | \#.*?\n)'
    t.lexer.lineno += t.value.count('\n')



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