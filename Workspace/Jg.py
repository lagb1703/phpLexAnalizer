
#Basic concepts

def p_script_one(t):
    'script : script_section'

# def p_script_two(t):
#     'script : script script_section'

# def p_script_section(t):
#     'script_section : text_opt start_tag statement_list_opt end_tago_opt text_opt'

# def p_text_opt(t):
#     '''text_opt : text 
#                     |'''
    
def p_end_tago_opt(t):
    '''end_tago_opt : end_tago
                    |'''
    
def p_statement_list_opt(t):
    '''statement_list_opt : statement_list
                                | '''

def p_start_tag_php(t):
    'start_tag : OPEN_TAG'

def p_start_tag_echo(t):
    'start_tag : OPEN_TAG_WITH_ECHO'

def p_end_tag(t):
    'end_tag : CLOSE_TAG'

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
                           | LEFT_PARENTHESIS expression RPAREN'''

def p_simple_variable(t):
    '''simple_variable : variable_name
                       | DOLLAR simple_variable
                       | DOLLAR LBRACE expression RPAREN'''

def p_dereferencable_expression(t):
    '''dereferencable_expression : variable
                                  | LEFT_PARENTHESIS expression RPAREN
                                  | array_creation_expression
                                  | string_literal'''

def p_callable_expression(t):
    '''callable_expression : callable_variable
                            | LEFT_PARENTHESIS expression RPAREN
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
    '''empty_intrinsic : EMPTY LEFT_PARENTHESIS expression RPAREN'''

def p_eval_intrinsic(t):
    '''eval_intrinsic : EVAL LEFT_PARENTHESIS expression RPAREN'''

def p_exit_intrinsic(t):
    '''exit_intrinsic : EXIT
                      | EXIT LEFT_PARENTHESIS expression_opt RPAREN
                      | DIE
                      | DIE LEFT_PARENTHESIS expression_opt RPAREN'''

def expression_opt(t):
    '''expression_opt : expression
                    |'''

def p_intrinsic_isset(t):
    '''intrinsic : ISSET LEFT_PARENTHESIS variable_list COMMA_opt RPAREN'''

def p_COMMA_opt(t):
    '''COMMA_opt : COMMA
                |'''

def p_variable_list_single(t):
    'variable_list : variable'

def p_variable_list_multiple(t):
    'variable_list : variable_list COMMA variable'

def p_anonymous_function_creation_expression(t):
    '''anonymous_function_creation_expression : static_opt FUNCTION AMPERSAND_opt LEFT_PARENTHESIS parameter_declaration_list_opt RPAREN anonymous_function_use_clause_opt return_type_opt compound_statement'''

def p_static_opt(t):
    '''static_opt : static
                    |'''

def p_AMPERSAND_opt(t):
    '''AMPERSAND_opt : AMPERSAND
                    |'''

def p_parameter_declaration_list_opt(t):
    '''parameter_declaration_list_opt : parameter_declaration_list
                                        |'''

def p_anonymous_function_use_clause_opt(t):
    '''anonymous_function_use_clause_opt : anonymous_function_use_clause
                                        |'''

def p_return_type_opt(t):
    '''return_type_opt : return_type
                        |'''

def p_anonymous_function_use_clause(t):
    'anonymous_function_use_clause : USE LEFT_PARENTHESIS use_variable_name_list RPAREN'

def p_use_variable_name_list_single(t):
    '''use_variable_name_list : AMPERSAND_opt variable_name'''

def p_use_variable_name_list_multiple(t):
    '''use_variable_name_list : use_variable_name_list COMMA AMPERSAND_opt variable_name'''

def p_object_creation_expression(t):
    '''object_creation_expression : NEW class_type_designator LEFT_PARENTHESIS argument_expression_list_opt RPAREN
                                  | NEW class_type_designator LEFT_PARENTHESIS argument_expression_list COMMA_opt RPAREN
                                  | NEW class_type_designator
                                  | NEW CLASS LEFT_PARENTHESIS argument_expression_list_opt RPAREN class_base_clause_opt class_interface_clause_opt LBRACE class_member_declarations_opt RBRACE
                                  | NEW CLASS class_base_clause_opt class_interface_clause_opt LBRACE class_member_declarations_opt RBRACE'''

def p_argument_expression_list_opt(t):
    '''argument_expression_list_opt : argument_expression_list
                                    |'''
def p_class_base_clause_opt(t):
    '''class_base_clause_opt : class_base_clause
                            |'''

def p_class_interface_clause_opt(t):
    '''class_interface_clause_opt : class_interface_clause
                            |'''
def p_class_member_declarations_opt(t):
    '''class_member_declarations_opt : class_member_declarations
                                    |'''

def p_class_type_designator_qualified_name(t):
    'class_type_designator : qualified_name'

def p_class_type_designator_new_variable(t):
    'class_type_designator : new_variable'

def p_new_variable_simple_variable(t):
    'new_variable : simple_variable'

def p_new_variable_array_access(t):
    '''new_variable : new_variable LBRACKET expression_opt RBRACKET
                    | new_variable LBRACE expression RBRACE
                    | new_variable ARROW member_name
                    | qualified_name DOUBLE_COLON simple_variable
                    | relative_scope DOUBLE_COLON simple_variable
                    | new_variable DOUBLE_COLON simple_variable'''

def p_expression_opt(t):
    '''expression_opt : expression
                        |'''

def p_array_creation_expression_array(t):
    '''array_creation_expression : ARRAY LEFT_PARENTHESIS array_initializer_opt RPAREN
                                  | LBRACKET array_initializer_opt RBRACKET'''

def p_array_initializer_opt(t):
    '''array_initializer_opt : array_initializer
                              | '''

def p_array_initializer(t):
    '''array_initializer : array_initializer_list COMMA_opt'''

def p_array_initializer_list(t):
    '''array_initializer_list : array_element_initializer COMMA_opt'''

def p_array_element_initializer_single(t):
    '''array_element_initializer : AMPERSAND_opt element_value'''

def p_array_element_initializer_key_value(t):
    '''array_element_initializer : element_key ARROW  AMPERSAND_opt element_value'''

def p_element_key(t):
    '''element_key : expression'''

def p_element_value(t):
    '''element_value : expression'''

def p_subscript_expression_brackets(t):
    '''subscript_expression : dereferencable_expression LBRACKET expression_opt RBRACKET'''

def p_subscript_expression_deprecated(t):
    '''subscript_expression : dereferencable_expression LBRACE expression RBRACE'''

def p_function_call_expression_qualified_name(t):
    '''function_call_expression : qualified_name LEFT_PARENTHESIS argument_expression_list_opt RPAREN
                                | qualified_name LEFT_PARENTHESIS argument_expression_list COMMA RPAREN'''

def p_function_call_expression_callable_expression(t):
    '''function_call_expression : callable_expression LEFT_PARENTHESIS argument_expression_list_opt RPAREN
                                | callable_expression LEFT_PARENTHESIS argument_expression_list COMMA RPAREN'''

def p_argument_expression_list_single(t):
    '''argument_expression_list : argument_expression'''

def p_argument_expression_list_multiple(t):
    '''argument_expression_list : argument_expression_list COMMA argument_expression'''

def p_argument_expression(t):
    '''argument_expression : variadic_unpacking
                           | expression'''

def p_variadic_unpacking(t):
    '''variadic_unpacking : ELLIPSIS expression'''

def p_member_access_expression(t):
    '''member_access_expression : dereferencable_expression ARROW member_name'''

def p_member_name_name(t):
    '''member_name : NAME'''

def p_member_name_simple_variable(t):
    '''member_name : simple_variable'''

def p_member_name_expression(t):
    '''member_name : LBRACE expression RBRACE'''

def p_member_call_expression(t):
    '''member_call_expression : dereferencable_expression ARROW member_name LEFT_PARENTHESIS argument_expression_list_opt RPAREN
                              | dereferencable_expression ARROW member_name LEFT_PARENTHESIS argument_expression_list COMMA RPAREN'''

def p_postfix_increment_expression(t):
    '''postfix_increment_expression : variable INCREMENT'''

def p_postfix_decrement_expression(t):
    '''postfix_decrement_expression : variable DECREMENT'''

def p_prefix_increment_expression(t):
    '''prefix_increment_expression : INCREMENT variable'''

def p_prefix_decrement_expression(t):
    '''prefix_decrement_expression : DECREMENT variable'''

def p_shell_command_expression(t):
    '''shell_command_expression : BACKTICK dq_char_sequence_opt BACKTICK'''

def p_dq_char_sequence_opt(t):
    '''dq_char_sequence_opt : dq_char_sequence
                            |'''

def p_scoped_property_access_expression(t):
    '''scoped_property_access_expression : scope_resolution_qualifier DOUBLE_COLON simple_variable'''

def p_scoped_call_expression(t):
    '''scoped_call_expression : scope_resolution_qualifier DOUBLE_COLON member_name LEFT_PARENTHESIS argument_expression_list_opt RPAREN
                               | scope_resolution_qualifier DOUBLE_COLON member_name LEFT_PARENTHESIS argument_expression_list COMMA RPAREN'''

def p_class_constant_access_expression(t):
    '''class_constant_access_expression : scope_resolution_qualifier DOUBLE_COLON NAME'''

def p_scope_resolution_qualifier_relative_scope(t):
    '''scope_resolution_qualifier : relative_scope'''

def p_scope_resolution_qualifier_qualified_name(t):
    '''scope_resolution_qualifier : qualified_name'''

def p_scope_resolution_qualifier_dereferencable_expression(t):
    '''scope_resolution_qualifier : dereferencable_expression'''

def p_relative_scope_self(t):
    '''relative_scope : SELF'''

def p_relative_scope_parent(t):
    '''relative_scope : PARENT'''

def p_relative_scope_static(t):
    '''relative_scope : STATIC'''

def p_clone_expression_primary_expression(t):
    '''clone_expression : primary_expression'''

def p_clone_expression_clone_primary_expression(t):
    '''clone_expression : CLONE primary_expression'''

def p_exponentiation_expression(t):
    '''exponentiation_expression : clone_expression
                                  | clone_expression EXPONENTIATION exponentiation_expression'''

def p_unary_expression(t):
    '''unary_expression : exponentiation_expression
                        | unary_op_expression
                        | error_control_expression
                        | cast_expression'''

def p_unary_op_expression(t):
    '''unary_op_expression : unary_operator unary_expression'''

def p_unary_operator_plus(t):
    '''unary_operator : PLUS'''

def p_unary_operator_minus(t):
    '''unary_operator : MINUS'''

def p_unary_operator_tilde(t):
    '''unary_operator : TILDE'''

def p_error_control_expression(t):
    '''error_control_expression : AT unary_expression'''

def p_cast_expression(t):
    '''cast_expression : LEFT_PARENTHESIS cast_type RPAREN unary_expression'''

def p_cast_type(t):
    '''cast_type : ARRAY
                 | BINARY
                 | BOOL
                 | BOOLEAN
                 | DOUBLE
                 | INT
                 | INTEGER
                 | FLOAT
                 | OBJECT
                 | REAL
                 | STRING
                 | UNSET'''

def p_instanceof_expression(t):
    '''instanceof_expression : unary_expression
                             | instanceof_subj instanceof class_type_designator'''

def p_instanceof_subj(t):
    '''instanceof_subj : instanceof_expression'''

def p_logical_not_expression(t):
    '''logical_not_expression : instanceof_expression
                               | NOT instanceof_expression'''

def p_multiplicative_expression(t):
    '''multiplicative_expression : logical_not_expression
                                  | multiplicative_expression TIMES logical_not_expression
                                  | multiplicative_expression DIVIDE logical_not_expression
                                  | multiplicative_expression MODULO logical_not_expression'''
