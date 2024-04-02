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

se llama lola 

# Reglas de expresiones regulares para tokens simples.
#?hay que encontrarlas
T_NS_SEPARATOR = r'\\'
#palabras reservadas declaracion
#las que tienen revisar a un lado es porque en la lista aparece con un () y falta decidir como tomar esa exprecion
def T_HALT_COMPILER(t): #!revisar
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
def T_AND_EQUAL(t):
    r'&='
    return t
def T_ARRAY_CAST(t):
    r'\(array\)'
    return t
def T_ATTRIBUTE(t): #!revisar por motivo de la lista 
    r'\#\[.*?\]'
    return t
def T_BAD_CHARACTER(t): #!revisar no se como tomarlo por lo que este debajo des ascii 32 y sus excepciones
    r'.'
    return t
def T_BOOLEAN_AND(t):
    r'&&'
    return t
def T_BOOLEAN_OR(t):
    r'\|\|'
    return t
def T_BOOL_CAST(t):
    r'\(bool\) | \(boolean\)'
    return t
def T_CLOSE_TAG(t):
    r'\?> | \%\>'
    return t
def T_COALESCE(t):
    r'\?\?'
    return t
def T_COALESCE_EQUAL(t):
    r'\?\?='
    return t
def T_COMMENT(t):
    r'//.*?\n | /\*.*?\*/ | #.*?\n'
    return t
def T_CONCAT_EQUAL(t):
    r'\.='
    return t
def T_CONSTANT_ENCAPSED_STRING(t): #!revisar la expresion regular
    r'\'[^\']*\' | \"[^\"]*\"'
    return t
def T_CURLY_OPEN(t):
    r'\$\{'
    return t
def T_DEC(t):
    r'--'
    return t
def T_DIV_EQUAL(t):
    r'/='
    return t
def T_DOC_COMMENT(t): #!revisar la expresion regular
    r'/\*\*(.|\n)*?\*/'
    return t
def T_DOLLAR_OPEN_CURLY_BRACES(t):
    r'\$\{'
    return t
def T_DOUBLE_ARROW(t):
    r'=>'
    return t
def T_DOUBLE_CAST(t):
    r'\(double\) | \(float\) | \(real\)'
    return t
def T_DOUBLE_COLON(t):
    r'::'
    return t
def T_ELLIPSIS(t):
    r'\.\.\.'
    return t
def T_DNUMBER(t): #!revisar la expresion regular (es la de la documentacion de php)
    r'([0-9]*(_[0-9]+)*[\.]{[0-9]+(_[0-9]+)*}) | ({[0-9]+(_[0-9]+)*}[\.][0-9]*(_[0-9]+)*)'
    return t
def T_ENCAPSED_AND_WHITESPACE(t): #!revisar la expresion regular y significado de este token
    r'(?<=\")((?:\\\\.|[^"])+)(?=\")(?=\s|$)'
    return t
def T_END_HEREDOC(t): #!esta no es la expresion regular hay que encontrarla
    r'\?>'
    return t
def T_INC(t):
    r'\+\+'
    return t
def T_INLINE_HTML(t): #!revisar la expresion regular y significado de este token
    r'<\?php\s+(.*?)(?:\?>|$)'
    return t
def T_INT_CAST(t): #*revisar la expresion regular y significado de este token
    r'\(int\) | \(integer\)'
    return t
def T_IS_EQUAL(t):
    r'=='
    return t
def T_IS_GREATER_OR_EQUAL(t):
    r'>='
    return t
def T_IS_IDENTICAL(t):
    r'==='
    return t
def T_IS_NOT_EQUAL(t):
    r'!= | <>'
    return t
def T_IS_NOT_IDENTICAL(t):
    r'!=='
    return t
def T_IS_SMALLER_OR_EQUAL(t):
    r'<='
    return t
def T_LNUMBER(t): #!revisar la expresion regular (es la de la documentacion de php)
    r'([+-]?(([1-9][0-9]* | 0) | 0[0-7]+ | 0[xX][0-9a-fA-F]+ | 0b[01]+))'
    return t
def T_MINUS_EQUAL(t):
    r'-='
    return t
def T_MOD_EQUAL(t):
    r'%='
    return t
def T_MUL_EQUAL(t):
    r'\*='
    return t
def T_NUM_STRING(t): #!revisar la expresion regular y significado de este token
    r'\[(?<indices>\d+(?:,\d+)*)\]'
    return t
def T_OBJECT_CAST(t): #*revisar la expresion regular y significado de este token
    r'\(object\)'
    return t
def T_OBJECT_OPERATOR(t):
    r'->'
    return t
def T_NULLSAFE_OBJECT_OPERATOR(t):
    r'\?->'
    return t
def T_OPEN_TAG(t):
    r'<\?php | <% | <\?'
    return t
def T_OPEN_TAG_WITH_ECHO(t):
    r'<\?= | <%='
    return t
def T_OR_EQUAL(t):
    r'\|='
    return t
def T_PAAMAYIM_NEKUDOTAYIM(t): # todo: esta se repite con T_DOUBLE_COLON revisar
    r'::'
    return t
def T_PLUS_EQUAL(t):
    r'\+='
    return t
def T_POW(t):
    r'\*\*'
    return t
def T_POW_EQUAL(t):
    r'\*\*='
    return t
def T_SL(t):
    r'<<'
    return t
def T_SL_EQUAL(t):
    r'<<='
    return t
def T_SPACESHIP(t):
    r'<=>'
    return t
def T_SR(t):
    r'>>'
    return t
def T_SR_EQUAL(t):
    r'>>='
    return t
def T_START_HEREDOC(t): #todo mor revisar heredoc
    r'<<<'
    return t
def T_STRING(t): #!revisar la expresion regular
    r'([a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)'
    return t
def T_STRING_CAST(t): #*revisar la expresion regular y significado de este token
    r'\(string\)'
    return t
def T_STRING_VARNAME(t): #!revisar la expresion regular y significado de este token
    r'\$\{(?<name>[a-zA-Z_][a-zA-Z0-9_]*)\}'
    return t
def T_VARIABLE(t): #!revisar la expresion regular
    r'\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'
    return t
def T_WHITESPACE(t): #*revisar la expresion regular (es la de la documentacion de php)
    r'\t | \n | \r'
    return t
def T_XOR_EQUAL(t):
    r'\^='
    return t

# # Ignorar espacios y tabs.
# t_ignore = r'\t |\r |\n'




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