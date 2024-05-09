#este es un analizador sintactico del lenguaje PHP hecho en python con la libreria PLY
import ply.yacc as yacc
from AnalixadorLex import tokens
import AnalixadorLex
import sys

VERBOSE = 1
#todo notas
# variable_name : VARIABLE #*se puede remplazar por el token asignado que usa esta gramatica
#
#
#


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

#Variables

def p_function_static_declaration(p):
    '''function_static_declaration : STATIC static_variable_name_list SEMICOLON'''

def p_static_variable_name_list(p):
    '''static_variable_name_list : static_variable_declaration
                                    | static_variable_name_list COLON static_variable_declaration''' #colon es comma

def p_static_variable_declaration(p):
    '''static_variable_declaration : variable_name function_static_initializeropt'''

def p_function_static_initializeropt(p): #? opcionales
    '''function_static_initializeropt : function_static_initializer
                                        | '''

def p_function_static_initializer(p):
    '''function_static_initializer : EQUALS constant_expression'''

def p_global_declaration(p):
    '''global_declaration : GLOBAL variable_name_list SEMICOLON'''

def p_variable_name_list(p):
    '''variable_name_list : simple_variable
                            | variable_name_list COLON simple_variable''' #colon es comma
    
#expressions

def p_primary_expression(p):
    '''primary_expression : variable
                            | class-constant-access-expression
                            | constant-access-expression
                            | literal
                            | array-creation-expression
                            | intrinsic
                            | anonymous-function-creation-expression
                            | object-creation-expression
                            | postfix-increment-expression
                            | postfix-decrement-expression
                            | prefix-increment-expression
                            | prefix-decrement-expression
                            | byref-assignment-expression
                            | shell-command-expression
                            | LEFT_PARENTHESIS expression RIGHT_PARENTHESIS''' # ( expression )

def p_simple_variable(p):
    '''simple_variable : variable_name
                        | DOLLAR simple_variable
                        | DOLLAR LEFT_CBRAC expression RIGHT_CBRAC''' # $variable_name, $ { expression }

def p_dereferencable_expression(p):
    '''dereferencable_expression : variable
                                    | LEFT_PARENTHESIS expression RIGHT_PARENTHESIS 
                                    | array_creation_expression
                                    | string_literal'''

def p_callable_expression(p):
    '''callable_expression : callable_variable
                            | LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
                            | array_creation_expression
                            | string_literal''' 

def p_callable_variable(p):
    '''callable_variable : simple_variable
                            | subscript_expression
                            | member_call_expression
                            | scoped_call_expression
                            | function_call_expression'''

def p_variable(p):
    '''variable : callable_variable
                | scoped_property_access_expression
                | member_access_expression'''
    
def p_member_access_expression(p):
    '''member_access_expression : qualified_name'''

def p_literal(p):
    '''literal : integer_literal
                | floating_literal
                | string_literal'''

def p_integer_literal(p):
    '''integer_literal : LNUMBER'''

def p_floating_literal(p):
    '''floating_literal : DNUMBER'''

def p_string_literal(p):
    '''string_literal : STRING'''

def p_qualifier_name(p):
    '''qualified_name : STRING'''

def p_intrinsic(p):
    '''intrinsic : empty-intrinsic
                 | eval-intrinsic
                 | exit-intrinsic
                 | isset-intrinsic'''

def p_empty_intrinsic(p):
    '''empty-intrinsic : EMPTY LEFT_PARENTHESIS expression RIGHT_PARENTHESIS'''

def p_eval_intrinsic(p):
    '''eval-intrinsic : EVAL LEFT_PARENTHESIS expression RIGHT_PARENTHESIS'''

def p_exit_intrinsic(p):
    '''exit-intrinsic : EXIT
                        | EXIT LEFT_PARENTHESIS expressionopt RIGHT_PARENTHESIS'''  #el token exit tiene la palabra reservada exit como die  

def p_isset_intrinsic(p):
    '''isset-intrinsic : ISSET LEFT_PARENTHESIS variable_list colonopt RIGHT_PARENTHESIS'''

def p_expressionopt(p): #? opcionales
    '''expressionopt : expression
                    | '''

def p_colonopt(p): #? opcionales
    '''colonopt : COLON
                | '''
    
def p_variable_list(p):
    '''variable_list : variable
                    | variable_list COLON variable''' #colon es comma 

def p_anonymous_function_creation_expression(p):
    '''anonymous_function_creation_expression : staticopt FUNCTION ampersandopt LEFT_PARENTHESIS parameter_declaration_listopt RIGHT_PARENTHESIS anonymous_function_use_clauseopt   return_typeopt compound_statement'''

def p_staticopt(p): #? opcionales
    '''staticopt : STATIC
                | '''

def p_ampersandopt(p): #? opcionales
    '''ampersandopt : AMPERSAND
                    | '''

def p_parameter_declaration_listopt(p): #? opcionales
    '''parameter_declaration_listopt : parameter_declaration_list
                                    | '''

def p_anonymous_function_use_clauseopt(p): #? opcionales
    '''anonymous_function_use_clauseopt : anonymous_function_use_clause
                                        | '''

def p_return_typeopt(p): #? opcionales
    '''return_typeopt : return_type
                    | '''

def p_anonymous_function_use_clause(p):
    '''anonymous_function_use_clause : USE LEFT_PARENTHESIS use_variable_name_list RIGHT_PARENTHESIS'''

def p_use_variable_name_list(p):
    '''use_variable_name_list : ampersandopt variable_name
                                | use_variable_name_list COLON ampersandopt variable_name''' #colon es comma

def p_variable_name(p): #todo token asignado que usa esta gramatica
    '''variable_name : VARIABLE'''

def p_object_creation_expression(p):
    '''object_creation_expression : NEW class_type_designator LEFT_PARENTHESIS argument_espression_listopt RIGHT_PARENTHESIS
                                    | NEW class_type_designator LEFT_PARENTHESIS argument_espression_list colonopt RIGHT_PARENTHESIS
                                    | NEW class_type_designator
                                    | NEW CLASS LEFT_PARENTHESIS argument_expression_listopt RIGHT_PARENTHESIS class_base_clauseopt class_interface_clauseopt LEFT_CBRAC class_member_declarationsopt RIGHT_CBRAC
                                    | NEW CLASS class_base_clauseopt class_interface_clauseopt LEFT_CBRAC class_member_declarationsopt RIGHT_CBRAC'''
    
def p_argument_expression_listopt(p): #? opcionales
    '''argument_expression_listopt : argument_expression_list
                                    | '''

def p_class_base_clauseopt(p):
    '''class_base_clauseopt : class_base_clause
                            | '''

def p_class_member_declarationsopt(p):
    '''class_member_declarationsopt : class_member_declarations
                                    | '''

#--------------------------------------------------------------
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