"""

Analizador léxico

Hecho por : 

- Luis alejandro Giraldo Bolaños
- Stiven Castro Soto
- Juan Camilo Galvis Agudelo

"""

import ply.lex as lex
import sys

tokens = (
    'ABSTRACT',
    'AMPERSAND',
    'AND_EQUAL',
    'ARRAY',
    # 'ARRAY_CAST',
    'AS',
    # 'ATTRIBUTE',
    'BOOLEAN_AND',
    'BOOLEAN_OR',
    'BREAK',
    'CALLABLE',
    'CASE',
    'CATCH',
    'CLASS',
    'CLONE',
    'CLOSE_TAG',
    'COALESCE',
    'CONCAT_EQUAL',
    'CONST',
    'CONSTANT_ENCAPSED_STRING',
    'CONTINUE',
    'DEC',
    'DECLARE',
    'DEFAULT',
    'DIV_EQUAL',
    'DNUMBER',
    'DO',
    'DOUBLE_ARROW',
    'DOUBLE_COLON',
    'ECHO',
    'ELLIPSIS',
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
    'FOR',
    'FOREACH',
    'FUNCTION',
    'GLOBAL',
    'GOTO',
    'IF',
    'IMPLEMENTS',
    'INC',
    'INCLUDE',
    'INCLUDE_ONCE',
    'INSTANCE_OF',
    'INSTEADOF',
    'INTERFACE',
    'ISSET',
    'IS_EQUAL',
    'IS_GREATER_OR_EQUAL',
    'IS_IDENTICAL',
    'IS_NOT_EQUAL',
    'IS_NOT_IDENTICAL',
    'IS_SMALLER_OR_EQUAL',
    'LIST',
    'LNUMBER',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'LOGICAL_XOR',
    'MINUS_EQUAL',
    'MUL_EQUAL',
    'MOD_EQUAL',
    'NAMESPACE',
    'NAMESPACE_NAME',
    'NEW',
    'NS_SEPARATOR',
    'OBJECT_OPERATOR',
    'OPEN_TAG',
    'OPEN_TAG_WITH_ECHO',
    'OR_EQUAL',
    'PLUS_EQUAL',
    'POW',
    'POW_EQUAL',
    'PRINT',
    'PRIVATE',
    'PROTECTED',
    'PUBLIC',
    'REQUIRE',
    'REQUIRE_ONCE',
    'RETURN',
    'SL',
    'SL_EQUAL',
    'SPACESHIP',
    'SR',
    'SR_EQUAL',
    'HEREDOC',
    'STATIC',
    'STRING',
    'SWITCH',
    'THROW',
    'TRAIT',
    'TRY',
    'UNSET',
    'USE',
    'VAR',
    'VARIABLE',
    'WHILE',
    'XOR_EQUAL',
    'YIELD',
    'YIELD_FROM',
    'OPAR',
    'CPAR',
    'ENDLINE',
    'ASSIGN',
    'OBRA',
    'CBRA',
    'CONCAT',
    'COMMA',
    'ADD',
    'SUB',
    'MUL',
    'DIV',
    'LT',
    'GT',
    'DOLLAR',
    'OBRACK',
    'CBRACK',
    'SELF',
    'PARENT',
    'NEG',
    'AT',
    'BINARY',
    'BOOL',
    'BOOLEAN',
    'DOUBLE',
    'INT',
    'INTEGER',
    'FLOAT',
    'OBJECT',
    'REAL',
    'STRINGKW',
    'NOT',
    'MOD',
    'BITWISE_XOR',
    'BITWISE_OR',
    'CONDITIONAL',
    'COLON',
    'TICKS',
    'ENCODING',
    'STRICT_TYPES',
    'ITERABLE',
    'CONSTRUCT',
    'DESTRUCT',
    'DIE',
    'VOID'
)

#Regular expression rules for simple tokens
t_AMPERSAND = r'\&'
t_OPAR = r'\('
t_CPAR = r'\)'
t_ENDLINE = r'\;'
t_ASSIGN = r'='
t_OBRA = r'\{'
t_CBRA = r'\}'
t_CONCAT = r'\.'
t_COMMA = r'\,'
t_ADD = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_MOD = r'\%'
t_LT = r'\<'
t_GT = r'\>'
t_DOLLAR = r'\$'
t_OBRACK = r'\['
t_CBRACK = r'\]'
t_NEG = r'\~'
t_AT = r'\@'
t_NOT = r'!'
t_BITWISE_XOR = r'\^'
t_BITWISE_OR = r'\|'
t_CONDITIONAL = r'\?'
t_COLON = r'\:'

def t_AND_EQUAL(t):
    r'\&='
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_AS(t):
    r'as'
    return t

def t_BOOLEAN_AND(t):
    r'\&\&'
    return t

def t_BOOLEAN_OR(t):
    r'\|\|'
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

def t_CLASS(t):
    r'class'
    return t

def t_CLONE(t):
    r'clone'
    return t

def t_CLOSE_TAG(t):
    r'\?\>'
    return t

def t_COALESCE(t):
    r'\?\?'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONCAT_EQUAL(t):
    r'\.='
    return t

def t_CONSTANT_ENCAPSED_STRING(t):
    r'("[^"]*")|(\'.*\')|(\`.*\`)'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DEC(t):
    r'--'
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

def t_DOUBLE_ARROW(t):
    r'=\>'
    return t

def t_DOUBLE_COLON(t):
    r'\:\:'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_ELLIPSIS(t):
    r'\.\.\.'
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

def t_EVAL(t):
    r'eval\(\)'
    return t

def t_EXIT(t):
    r'exit'
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

def t_INC(t):
    r'\+\+'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_INCLUDE_ONCE(t):
    r'include\_once'
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
    r'isset\(\)'
    return t

def t_IS_EQUAL(t):
    r'=='
    return t

def t_IS_GREATER_OR_EQUAL(t):
    r'\>='
    return t

def t_IS_IDENTICAL(t):
    r'==='
    return t

def t_IS_NOT_EQUAL(t):
    r'\!='
    return t

def t_IS_NOT_IDENTICAL(t):
    r'\!=='
    return t

def t_IS_SMALLER_OR_EQUAL(t):
    r'\<='
    return t

def t_LIST(t):
    r'list'
    return t

def t_LNUMBER(t):
    r'\d+'
    return t

def t_DNUMBER(t):
    r'\d+(\.\d+)?(e(\-)?\d+(.\d+)?)?'
    return t

def t_LOGICAL_AND(t):
    r'and'
    return t

def t_LOGICAL_OR(t):
    r'or'
    return t

def t_LOGICAL_XOR(t):
    r'xor'
    return t

def t_MINUS_EQUAL(t):
    r'-='
    return t

def t_MOD_EQUAL(t):
    r'\%='
    return t

def t_MUL_EQUAL(t):
    r'\*='
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_NAMESPACE_NAME(t):
    r'namespace-name'
    return t

def t_NEW(t):
    r'new'
    return t

def t_NS_SEPARATOR(t):
    r'\\'
    return t

def t_OBJECT_OPERATOR(t):
    r'-\>'
    return t

def t_OPEN_TAG(t):
    r'\<\?php'
    return t

def t_OPEN_TAG_WITH_ECHO(t):
    r'\<\?='
    return t

def t_OR_EQUAL(t):
    r'\|='
    return t

def t_PLUS_EQUAL(t):
    r'\+='
    return t

def t_DOC_COMMENT(t):
    r'/\*\*(.|\n)*\*/'
    pass

def t_POW(t):
    r'\*\*'
    return t

def t_POW_EQUAL(t):
    r'\*\*='
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

def t_REQUIRE(t):
    r'require'
    return t

def t_REQUIRE_ONCE(t):
    r'require\_once'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_HEREDOC(t):
    r'\<\<\<EOD[\S\s]*EOD'
    return t

def t_SL(t):
    r'\<\<'
    return t

def t_SL_EQUAL(t):
    r'\<\<='
    return t

def t_SPACESHIP(t):
    r'\<=\>'
    return t

def t_SR(t):
    r'\>\>'
    return t

def t_SR_EQUAL(t):
    r'\>\>='
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

def t_USE(t):
    r'use'
    return t

def t_VAR(t):
    r'var'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_XOR_EQUAL(t):
    r'\^='
    return t

def t_YIELD(t):
    r'yield'
    return t

def t_YIELD_FROM(t):
    r'yield from'
    return t

def t_BINARY(t):
    r'binary'
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_INT(t):
    r'int'
    return t

def t_INTEGER(t):
    r'integer'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_OBJECT(t):
    r'object'
    return t

def t_REAL(t):
    r'real'
    return t

def t_STRINGKW(t):
    r'string'
    return t

def t_UNSET(t):
    r'unset'
    return t

def t_TICKS(t):
    r'ticks'
    return t

def t_ENCODING(t):
    r'encoding'
    return t

def t_STRICT_TYPES(t):
    r'strict_types'
    return t

def t_ITERABLE(t):
    r'iterable'
    return t

def t_CONSTRUCT(t):
    r'\_\_construct'
    return t

def t_DESTRUCT(t):
    r'\_\_destruct'
    return t

def t_DIE(t):
    r'die'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_VOID(t):
    r'void'
    return t

def t_SELF(t):
    r'self'
    return t

def t_PARENT(t):
    r'parent'
    return t

def t_STRING(t):
    r'[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*'
    return t

def t_VARIABLE(t):
    r'\$[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*'
    return t


def t_COMMENT(t):
    r'//.*\n'
    pass


t_ignore = ' \t\n'


# Una regla para manejar errores.
def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
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


if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'test.txt'
	f = open(fin, 'r')
	data = f.read()
	lexer.input(data)
	test(data, lexer)
	#input()