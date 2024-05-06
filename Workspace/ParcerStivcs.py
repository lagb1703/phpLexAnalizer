import ply.yacc as yacc
from AnalixadorLex import tokens
import AnalixadorLex
import sys

VERBOSE = 1

# Basic Concepts
def p_script(t):
   '''script: script-section
                | script   script-section'''

def p_script_section(p):
    '''script_section : start_tag statement_listopt end_tagopt ''' #script_section : textopt start_tag statement_listopt end_tagopt textopt

def p_start_tag(p):
    '''start_tag : OPEN_TAG
                    | OPEN_TAG_WITH_ECHO'''

def p_end_tag(p):
    '''end_tag : CLOSE_TAG'''

# 
def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(AnalixadorLex.lexer.lineno))
	else:
		raise Exception('syntax', 'error')


parser = yacc.yacc()
if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'test.txt'
    f = open(fin, 'r')
    data = f.read()
    #print (data)
    result = parser.parse(data)
    print(result)