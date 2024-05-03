
#Basic concepts

def p_script_one(t):
    'script : script_section'

def p_script_two(t):
    'script : script script_section'

def p_script_section(t):
    'script_section : text_opt start_tag statement_list_opt end_tago_opt text_opt'

def p_text_opt(t):
    '''text_opt : text 
                    |'''
    
def p_end_tago_opt(t):
    '''end_tago_opt : end_tago
                    |'''
    
def p_statement_list_opt(t):
    '''statement_list_opt : statement_list
                                | '''

def p_start_tag_php(t):
    'start_tag : PHP_OPEN'

def p_start_tag_echo(t):
    'start_tag : ECHO_OPEN'

def p_end_tag(t):
    'end_tag : PHP_CLOSE'

def p_end_tag_empty(t):
    'end_tag : '

def p_text(t):
    'text : ARBITRARY_TEXT'

#variables

def p_function_static_declaration(t):
    'function_static_declaration : STATIC static_variable_name_list SEMICOLON'

def p_static_variable_name_list_single(t):
    'static_variable_name_list : static_variable_declaration'

def p_static_variable_name_list_multiple(t):
    'static_variable_name_list : static_variable_name_list COMMA static_variable_declaration'

def p_static_variable_declaration(t):
    'static_variable_declaration : variable_name function_static_initializer_opt'

def p_function_static_initializer_opt(t):
    '''function_static_initializer_opt : function_static_initializer
                                         | '''

def p_function_static_initializer_opt(t):
    '''function_static_initializer_opt : EQUAL constant_expression'''

def p_global_declaration(t):
    'global_declaration : GLOBAL variable_name_list SEMICOLON'

def p_variable_name_list_single(t):
    'variable_name_list : simple_variable'

def p_variable_name_list_multiple(t):
    'variable_name_list : variable_name_list COMMA simple_variable'

#Expressions

def p_primary_expression_variable(t):
    '''primary_expression : variable
                           | class_constant_access_expression
                           | constant_access_expression
                           | literal
                           | array_creation_expression
                           | intrinsic
                           | anonymous_function_creation_expression
                           | object_creation_expression
                           | postfix_increment_expression
                           | postfix_decrement_expression
                           | prefix_increment_expression
                           | prefix_decrement_expression
                           | byref_assignment_expression
                           | shell_command_expression
                           | LPAREN expression RPAREN'''

def p_simple_variable(t):
    '''simple_variable : variable_name
                       | DOLLAR simple_variable
                       | DOLLAR LBRACE expression RPAREN'''

def p_dereferencable_expression(t):
    '''dereferencable_expression : variable
                                  | LPAREN expression RPAREN
                                  | array_creation_expression
                                  | string_literal'''

def p_callable_expression(t):
    '''callable_expression : callable_variable
                            | LPAREN expression RPAREN
                            | array_creation_expression
                            | string_literal'''

def p_callable_variable(t):
    '''callable_variable : simple_variable
                         | subscript_expression
                         | member_call_expression
                         | scoped_call_expression
                         | function_call_expression'''

def p_variable(t):
    '''variable : callable_variable
                | scoped_property_access_expression
                | member_access_expression'''

def p_constant_access_expression(t):
    'constant_access_expression : qualified_name'

def p_literal_integer(t):
    '''literal : integer_literal
                |floating_literal
                |string_literal'''

def p_intrinsic_empty(t):
    '''intrinsic : empty_intrinsic
                  | eval_intrinsic
                  | exit_intrinsic
                  | isset_intrinsic'''

def p_empty_intrinsic(t):
    '''empty_intrinsic : EMPTY LPAREN expression RPAREN'''

def p_eval_intrinsic(t):
    '''eval_intrinsic : EVAL LPAREN expression RPAREN'''

def p_exit_intrinsic(t):
    '''exit_intrinsic : EXIT
                      | EXIT LPAREN expression_opt RPAREN
                      | DIE
                      | DIE LPAREN expression_opt RPAREN'''

def expression_opt(t):
    '''expression_opt : expression
                    |'''

def p_intrinsic_isset(t):
    '''intrinsic : ISSET LPAREN variable_list COMMA_opt RPAREN'''

def p_COMMA_opt(t):
    '''COMMA_opt : COMMA
                |'''

def p_variable_list_single(t):
    'variable_list : variable'

def p_variable_list_multiple(t):
    'variable_list : variable_list COMMA variable'

#Hasta aqui voy 

def p_anonymous_function_creation_expression(t):
    '''anonymous_function_creation_expression : staticopt FUNCTION AMPERSAND? LPAREN parameter_declaration_list? RPAREN anonymous_function_use_clause? return_type? compound_statement'''

def p_anonymous_function_use_clause(t):
    'anonymous_function_use_clause : USE LPAREN use_variable_name_list RPAREN'

def p_use_variable_name_list_single(t):
    '''use_variable_name_list : AMPERSANDopt variable_name'''

def p_use_variable_name_list_multiple(t):
    '''use_variable_name_list : use_variable_name_list COMMA AMPERSAND? variable_name'''

def p_object_creation_expression(t):
    '''object_creation_expression : NEW class_type_designator LPAREN argument_expression_listopt RPAREN
                                  | NEW class_type_designator LPAREN argument_expression_list COMMAopt RPAREN
                                  | NEW class_type_designator
                                  | NEW CLASS LPAREN argument_expression_list? RPAREN class_base_clause? class_interface_clause? LBRACE class_member_declarations? RBRACE
                                  | NEW CLASS class_base_clause? class_interface_clause? LBRACE class_member_declarations? RBRACE'''

def p_class_type_designator_qualified_name(t):
    'class_type_designator : qualified_name'

def p_class_type_designator_new_variable(t):
    'class_type_designator : new_variable'

def p_new_variable_simple_variable(t):
    'new_variable : simple_variable'

def p_new_variable_array_access(t):
    '''new_variable : new_variable LBRACKET expression? RBRACKET
                    | new_variable LBRACE expression RBRACE
                    | new_variable ARROW member_name
                    | qualified_name DOUBLE_COLON simple_variable
                    | relative_scope DOUBLE_COLON simple_variable
                    | new_variable DOUBLE_COLON simple_variable'''

def p_array_creation_expression_array(t):
    'array-creation-expression : ARRAY LEFT_PAREN array-initializeropt RIGHT_PAREN'

def p_array_creation_expression_bracket(t):
    'array-creation-expression : LEFT_BRACKET array-initializeropt RIGHT_BRACKET'

def p_array_initializer(t):
    'array-initializer : array-initializer-list COMMAopt'

def p_array_initializer_list_single(t):
    'array-initializer-list : array-element-initializer'

def p_array_initializer_list_multiple(t):
    'array-initializer-list : array-element-initializer COMMA array-initializer-list'

def p_array_element_initializer_value(t):
    'array-element-initializer : AMPERSANDopt element-value'

def p_array_element_initializer_key_value(t):
    'array-element-initializer : element-key DOUBLE_ARROW AMPERSANDopt element-value'

def p_element_key(t):
    '''element_key : expression'''

def p_element_value(t):
    '''element_value : expression'''

def p_subscript_expression_brackets(t):
    '''subscript_expression : dereferencable_expression LBRACKET expression? RBRACKET'''

def p_subscript_expression_braces(t):
    '''subscript_expression : dereferencable_expression LBRACE expression RBRACE'''

def p_function_call_expression_qualified_name(t):
    '''function_call_expression : qualified_name LPAREN argument_expression_listopt RPAREN
                                | qualified_name LPAREN argument_expression_list COMMA RPAREN'''

def p_function_call_expression_callable_expression(t):
    '''function_call_expression : callable_expression LPAREN argument_expression_listopt RPAREN
                                | callable_expression LPAREN argument_expression_list COMMA RPAREN'''

def p_argument_expression_list_single(t):
    '''argument_expression_list : argument_expression'''

def p_argument_expression_list_multiple(t):
    '''argument_expression_list : argument_expression_list COMMA argument_expression'''
