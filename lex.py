import ply.lex as lex
import sys

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
    'T_EMPTY',
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
    'T_VAR',
    'T_VARIABLE',
    'T_WHILE', 
    'T_XOR_EQUAL', 
    'T_YIELD', 
    'T_YIELD_FROM',
)

# Reglas de expresiones regulares para tokens simples.
def t_T_ABSTRACT(t):
    r'abstract'
    return t

def t_T_AND_EQUAL(t):
    r'&='
    return t

def t_T_ARRAY(t):
    r'array\(\)'
    return t

def t_T_ARRAY_CAST(t):
    r'\(array\)'
    return t

def t_T_AS(t):
    r'as'
    return t

def t_T_ATTRIBUTE(t):
    r'\#\['
    return t

def t_T_BOOLEAN_AND(t):
    r'&&'
    return t

def t_T_BOOLEAN_OR(t):
    r'\|\|'
    return t

def t_T_BOOL_CAST(t):
    r'(bool)|(boolean)'
    return t

def t_T_BREAK(t):
    r'break'
    return t

def t_T_CALLABLE(t):
    r'callable'
    return t

def t_T_CASE(t):
    r'case'
    return t

def t_T_CATCH(t):
    r'catch'
    return t

def t_T_CLASS(t):
    r'class'
    return t

def t_T_CLASS_C(t):
    r'__CLASS__'
    return t

def t_T_CLONE(t):
    r'clone'
    return t

def t_T_CLOSE_TAG(t):
    r'\?>|%\>'
    return t

def t_T_COALESCE(t):
    r'\?\?'
    return t

def t_T_COALESCE_EQUAL(t):
    r'\?\?='
    return t

def t_T_CONCAT_EQUAL(t):
    r'\.='
    return t

def t_T_CONST(t):
    r'const'
    return t

def t_T_CONSTANT_ENCAPSED_STRING(t):
    r'\".*?\"|\\\'.*?\\\''
    return t

def t_T_CONTINUE(t):
    r'continue'
    return t

def t_T_DEC(t):
    r'--'
    return t

def t_T_DECLARE(t):
    r'declare'
    return t

def t_T_DEFAULT(t):
    r'default'
    return t

def t_T_DIR(t):
    r'__DIR__'
    return t

def t_T_DIV_EQUAL(t):
    r'/='
    return t

def t_T_DO(t):
    r'do'
    return t

def t_T_DOUBLE_ARROW(t):
    r'=>'
    return t

def t_T_DOUBLE_CAST(t):
    r'\(real\)|\(double\)|\(float\)'
    return t

def t_T_ECHO(t):
    r'echo'
    return t

def t_T_ELLIPSIS(t):
    r'\.\.\.'
    return t

def t_T_ELSE(t):
    r'else'
    return t

def t_T_ELSEIF(t):
    r'elseif'
    return t

def t_T_EMPTY(t):
    r'empty'
    return t

def t_T_ENCAPSED_AND_WHITESPACE(t):
    r'\"\s*\$[a-zA-Z_][a-zA-Z_0-9]*\"'
    return t

def t_T_ENDDECLARE(t):
    r'enddeclare'
    return t

def t_T_ENDFOR(t):
    r'endfor'
    return t

def t_T_ENDFOREACH(t):
    r'endforeach'
    return t

def t_T_ENDIF(t):
    r'endif'
    return t

def t_T_ENDSWITCH(t):
    r'endswitch'
    return t

def t_T_ENDWHILE(t):
    r'endwhile'
    return t

def t_T_EVAL(t):
    r'eval\(\)'
    return t

def t_T_EXIT(t):
    r'exit|die'
    return t

def t_T_EXTENDS(t):
    r'extends'
    return t

def t_T_FILE(t):
    r'__FILE__'
    return t

def t_T_FINAL(t):
    r'final'
    return t

def t_T_FINALLY(t):
    r'finally'
    return t

def t_T_FN(t):
    r'fn'
    return t

def t_T_FOR(t):
    r'for'
    return t

def t_T_FOREACH(t):
    r'foreach'
    return t

def t_T_FUNCTION(t):
    r'function'
    return t

def t_T_FUNC_C(t):
    r'__FUNCTION__'
    return t

def t_T_GLOBAL(t):
    r'global'
    return t

def t_T_GOTO(t):
    r'goto'
    return t

def t_T_HALT_COMPILER(t):
    r'__halt_compiler\(\)'
    return t
def t_T_IF(t):
    r'if'
    return t
def t_T_IMPLEMENTS(t):
    r'implements'
    return t

def t_T_INC(t):
    r'\+\+'
    return t

def t_T_INCLUDE(t):
    r'include'
    return t

def t_T_INCLUDE_ONCE(t):
    r'include_once'
    return t

def t_T_INSTANCEOF(t):
    r'instanceof'
    return t

def t_T_INSTEADOF(t):
    r'insteadof'
    return t

def t_T_INTERFACE(t):
    r'interface'
    return t

def t_T_INT_CAST(t):
    r'\(int\)|\(integer\)'
    return t

def t_T_ISSET(t):
    r'isset'
    return t

def t_T_IS_EQUAL(t):
    r'=='
    return t

def t_T_IS_GREATER_OR_EQUAL(t):
    r'>='
    return t

def t_T_IS_IDENTICAL(t):
    r'==='
    return t

def t_T_IS_NOT_EQUAL(t):
    r'!=|<>'
    return t

def t_T_IS_NOT_IDENTICAL(t):
    r'!=='
    return t

def t_T_IS_SMALLER_OR_EQUAL(t):
    r'<='
    return t

def t_T_LINE(t):
    r'__LINE__'
    return t

def t_T_LIST(t):
    r'list'
    return t

def t_T_LOGICAL_AND(t):
    r'and'
    return t

def t_T_LOGICAL_OR(t):
    r'or'
    return t

def t_T_LOGICAL_XOR(t):
    r'xor'
    return t

def t_T_METHOD_C(t):
    r'__METHOD__'
    return t

def t_T_MINUS_EQUAL(t):
    r'-='
    return t

def t_T_MOD_EQUAL(t):
    r'%='
    return t

def t_T_MUL_EQUAL(t):
    r'\*='
    return t

def t_T_NAMESPACE(t):
    r'namespace'
    return t

def t_T_NEW(t):
    r'new'
    return t

def t_T_NS_C(t):
    r'__NAMESPACE__'
    return t

def t_T_NS_SEPARATOR(t):
    r'\\'
    return t

def t_T_OBJECT_CAST(t):
    r'\(object\)'
    return t

def t_T_OBJECT_OPERATOR(t):
    r'->'
    return t

def t_T_NULLSAFE_OBJECT_OPERATOR(t):
    r'\?->'
    return t

def t_T_OPEN_TAG(t):
    r'<\?(php)?'
    return t

def t_T_OPEN_TAG_WITH_ECHO(t):
    r'<\?='
    return t

def t_T_OR_EQUAL(t):
    r'\|='
    return t

def t_T_PLUS_EQUAL(t):
    r'\+='
    return t

def t_T_POW(t):
    r'\*\*'
    return t

def t_T_POW_EQUAL(t):
    r'\*\*='
    return t

def t_T_PRINT(t):
    r'print'
    return t

def t_T_PRIVATE(t):
    r'private'
    return t

def t_T_PROTECTED(t):
    r'protected'
    return t

def t_T_PUBLIC(t):
    r'public'
    return t

def t_T_REQUIRE(t):
    r'require'
    return t

def t_T_REQUIRE_ONCE(t):
    r'require_once'
    return t

def t_T_RETURN(t):
    r'return'
    return t

def t_T_SL(t):
    r'<<'
    return t

def t_T_SL_EQUAL(t):
    r'<<='
    return t

def t_T_SPACESHIP(t):
    r'<=>'
    return t

def t_T_SR(t):
    r'>>'
    return t

def t_T_SR_EQUAL(t):
    r'>>='
    return t

def t_T_START_HEREDOC(t):
    r'<<<'
    return t

def t_T_STATIC(t):
    r'static'
    return t

def t_T_STRING_CAST(t):
    r'\(string\)'
    return t

def t_T_STRING_VARNAME(t):
    r'\$\{[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*'
    return t


def t_T_SWITCH(t):
    r'switch'
    return t

def t_T_THROW(t):
    r'throw'
    return t

def t_T_TRAIT(t):
    r'trait'
    return t

def t_T_TRAIT_C(t):
    r'__TRAIT__'
    return t

def t_T_TRY(t):
    r'try'
    return t

def t_T_UNSET(t):
    r'unset'
    return t

def t_T_UNSET_CAST(t):
    r'\(unset\)'
    return t

def t_T_USE(t):
    r'use'
    return t

def t_T_VAR(t):
    r'var'
    return t

def t_T_WHILE(t):
    r'while'
    return t

def t_T_XOR_EQUAL(t):
    r'^='
    return t

def t_T_YIELD(t):
    r'yield'
    return t

def t_T_YIELD_FROM(t):
    r'yield from'
    return t

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
t_ignore = ' \t\n'


# Ignorar comentarios de una y varias líneas
def t_T_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*?\n)|(\#.*?\n)'
    pass  # Token is ignored

# Ignorar comentarios tipo PHPDoc
def t_T_DOC_COMMENT(t):
    r'/\*\*(.|\n)*?\*/'
    pass  # Token is ignored

def t_T_INLINE_HTML(t):
    r'.+?(?=<\?php)|.+$'
    pass  # Aquí decides si ignorar el contenido HTML o manejarlo de alguna manera

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construye el lexer
lexer = lex.lex()

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

# Para probarlo, vamos a alimentarlo con un string de entrada.
input_string = "<?php for ($i = 0; $i < 10; $i++){} ?>"

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
