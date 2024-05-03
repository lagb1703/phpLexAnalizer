import ply.yacc as yacc
from AnalixadorLex import tokens
import sys

VERBOSE = 1

#Galvis


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

def p_function_static_initializer_opt_1(t):
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
                           | LEFT_PARENTHESIS expression RIGHT_PARENTHESIS'''

def p_simple_variable(t):
    '''simple_variable : variable_name
                       | DOLLAR simple_variable
                       | DOLLAR LBRACE expression RIGHT_PARENTHESIS'''

def p_dereferencable_expression(t):
    '''dereferencable_expression : variable
                                  | LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
                                  | array_creation_expression
                                  | string_literal'''

def p_callable_expression(t):
    '''callable_expression : callable_variable
                            | LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
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
                | floating_literal
                | string_literal'''

def p_intrinsic_empty(t):
    '''intrinsic : empty_intrinsic
                  | eval_intrinsic
                  | exit_intrinsic
                  | isset_intrinsic'''

def p_empty_intrinsic(t):
    '''empty_intrinsic : EMPTY LEFT_PARENTHESIS expression RIGHT_PARENTHESIS'''

def p_eval_intrinsic(t):
    '''eval_intrinsic : EVAL LEFT_PARENTHESIS expression RIGHT_PARENTHESIS'''

def p_exit_intrinsic(t):
    '''exit_intrinsic : EXIT
                      | EXIT LEFT_PARENTHESIS expression_opt RIGHT_PARENTHESIS
                      | DIE
                      | DIE LEFT_PARENTHESIS expression_opt RIGHT_PARENTHESIS'''

def p_intrinsic_isset(t):
    '''intrinsic : ISSET LEFT_PARENTHESIS variable_list COMMA_opt RIGHT_PARENTHESIS'''

def p_COMMA_opt(t):
    '''COMMA_opt : COMMA
                |'''

def p_variable_list_single(t):
    'variable_list : variable'

def p_variable_list_multiple(t):
    'variable_list : variable_list COMMA variable'

def p_anonymous_function_creation_expression(t):
    '''anonymous_function_creation_expression : static_opt FUNCTION AMPERSAND_opt LEFT_PARENTHESIS parameter_declaration_list_opt RIGHT_PARENTHESIS anonymous_function_use_clause_opt return_type_opt compound_statement'''

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
    'anonymous_function_use_clause : USE LEFT_PARENTHESIS use_variable_name_list RIGHT_PARENTHESIS'

def p_use_variable_name_list_single(t):
    '''use_variable_name_list : AMPERSAND_opt variable_name'''

def p_use_variable_name_list_multiple(t):
    '''use_variable_name_list : use_variable_name_list COMMA AMPERSAND_opt variable_name'''

def p_object_creation_expression(t):
    '''object_creation_expression : NEW class_type_designator LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS
                                  | NEW class_type_designator LEFT_PARENTHESIS argument_expression_list COMMA_opt RIGHT_PARENTHESIS
                                  | NEW class_type_designator
                                  | NEW CLASS LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS class_base_clause_opt class_interface_clause_opt LBRACE class_member_declarations_opt RBRACE
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

def p_expression_opt_1(t):
    '''expression_opt : expression
                        |'''

def p_array_creation_expression_array(t):
    '''array_creation_expression : ARRAY LEFT_PARENTHESIS array_initializer_opt RIGHT_PARENTHESIS
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
    '''function_call_expression : qualified_name LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS
                                | qualified_name LEFT_PARENTHESIS argument_expression_list COMMA RIGHT_PARENTHESIS'''

def p_function_call_expression_callable_expression(t):
    '''function_call_expression : callable_expression LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS
                                | callable_expression LEFT_PARENTHESIS argument_expression_list COMMA RIGHT_PARENTHESIS'''

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
    '''member_call_expression : dereferencable_expression ARROW member_name LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS
                              | dereferencable_expression ARROW member_name LEFT_PARENTHESIS argument_expression_list COMMA RIGHT_PARENTHESIS'''

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
    '''scoped_call_expression : scope_resolution_qualifier DOUBLE_COLON member_name LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS
                               | scope_resolution_qualifier DOUBLE_COLON member_name LEFT_PARENTHESIS argument_expression_list COMMA RIGHT_PARENTHESIS'''

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
    '''cast_expression : LEFT_PARENTHESIS cast_type RIGHT_PARENTHESIS unary_expression'''

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


#Luis
#1

def p_additive_expression_multiplicative(t):
    'additive-expression : multiplicative-expression'

def p_additive_expression_addition(t):
    'additive-expression : additive-expression PLUS multiplicative-expression'

def p_additive_expression_subtraction(t):
    'additive-expression : additive-expression LESS multiplicative-expression'

def p_additive_expression_concatenation(t):
    'additive-expression : additive-expression CONCAT multiplicative-expression'

def p_shift_expression_additive(t):
    'shift-expression : additive-expression'

def p_shift_expression_left_shift(t):
    'shift-expression : shift-expression SL additive-expression'

def p_shift_expression_right_shift(t):
    'shift-expression : shift-expression SR additive-expression'

def p_relational_expression_shift(t):
    'relational-expression : shift-expression'

def p_relational_expression_less_than(t):
    'relational-expression : relational-expression LESS_THAN shift-expression'

def p_relational_expression_greater_than(t):
    'relational-expression : relational-expression IS_SMALLER_OR_EQUAL shift-expression'

def p_relational_expression_less_than_or_equal(t):
    'relational-expression : relational-expression IS_GREATER_OR_EQUAL shift-expression'

def p_relational_expression_greater_than_or_equal(t):
    'relational-expression : relational-expression GREATER_THAN_OR_EQUAL shift-expression'

def p_relational_expression_spaceship(t):
    'relational-expression : relational-expression SPACESHIP shift-expression'


#2

def p_equality_expression_relational(t):
    'equality-expression : relational-expression'

def p_equality_expression_equal(t):
    'equality-expression : equality-expression EQUAL relational-expression'

def p_equality_expression_not_equal(t):
    'equality-expression : equality-expression IS_NOT_EQUAL relational-expression'

def p_equality_expression_identical(t):
    'equality-expression : equality-expression IS_IDENTICAL relational-expression'

def p_equality_expression_not_identical(t):
    'equality-expression : equality-expression IS_NOT_IDENTICAL relational-expression'

def p_bitwise_AND_expression_equality(t):
    'bitwise-AND-expression : equality-expression'

def p_bitwise_AND_expression_AND(t):
    'bitwise-AND-expression : bitwise-AND-expression AMPERSAND equality-expression'

def p_bitwise_exc_OR_expression_AND(t):
    'bitwise-exc-OR-expression : bitwise-AND-expression'

def p_bitwise_exc_OR_expression_exc_OR(t):
    'bitwise-exc-OR-expression : bitwise-exc-OR-expression BITWISE_XOR bitwise-AND-expression'

def p_bitwise_inc_OR_expression_exc_OR(t):
    'bitwise-inc-OR-expression : bitwise-exc-OR-expression'

def p_bitwise_inc_OR_expression_inc_OR(t):
    'bitwise-inc-OR-expression : bitwise-inc-OR-expression BITWISE_OR bitwise-exc-OR-expression'

#3

def p_logical_AND_expression_1_bitwise_inc_OR(t):
    'logical-AND-expression-1 : bitwise-inc-OR-expression'

def p_logical_AND_expression_1_AND(t):
    'logical-AND-expression-1 : logical-AND-expression-1 AMPERSAND AMPERSAND bitwise-inc-OR-expression'

def p_logical_inc_OR_expression_1_logical_AND(t):
    'logical-inc-OR-expression-1 : logical-AND-expression-1'

def p_logical_inc_OR_expression_1_OR(t):
    'logical-inc-OR-expression-1 : logical-inc-OR-expression-1 BITWISE_OR BITWISE_OR logical-AND-expression-1'

def p_coalesce_expression_logical_inc_OR(t):
    'coalesce-expression : logical-inc-OR-expression-1'

def p_coalesce_expression_coalesce(t):
    'coalesce-expression : logical-inc-OR-expression-1 COALESCE coalesce-expression'

def p_conditional_expression_coalesce(t):
    'conditional-expression : coalesce-expression'

def p_conditional_expression_ternary(t):
    '''conditional-expression : conditional-expression TERNARY_OPERATION expression DOUBLE_POINT coalesce-expression
                                | conditional-expression TERNARY_OPERATION DOUBLE_POINT coalesce-expression'''

#4

def p_assignment_expression_conditional(t):
    'assignment-expression : conditional-expression'

def p_assignment_expression_simple(t):
    'assignment-expression : simple-assignment-expression'

def p_assignment_expression_compound(t):
    'assignment-expression : compound-assignment-expression'

def p_simple_assignment_expression_variable(t):
    'simple-assignment-expression : variable EQUAL assignment-expression'

def p_simple_assignment_expression_list_intrinsic(t):
    'simple-assignment-expression : list-intrinsic EQUAL assignment-expression'

def p_list_intrinsic(t):
    'list-intrinsic : LIST LEFT_PARENTHESIS list-expression-list RIGHT_PARENTHESIS'

def p_list_expression_list_unkeyed(t):
    'list-expression-list : unkeyed-list-expression-list'

def p_list_expression_list_keyed(t):
    '''list-expression-list : keyed-list-expression-list COLON
                                | keyed-list-expression-list'''

def p_unkeyed_list_expression_list_single(t):
    'unkeyed-list-expression-list : list-or-variable'

def p_unkeyed_list_expression_list_comma(t):
    'unkeyed-list-expression-list : COLON'

def p_unkeyed_list_expression_list_multiple(t):
    'unkeyed-list-expression-list : unkeyed-list-expression-list COMMA list-or-variable (COLON)?'

def p_keyed_list_expression_list_single(t):
    'keyed-list-expression-list : expression DOUBLE_ARROW list-or-variable'

def p_keyed_list_expression_list_multiple(t):
    'keyed-list-expression-list : keyed-list-expression-list COLON expression DOUBLE_ARROW list-or-variable'

#5

def p_list_or_variable_list_intrinsic(t):
    'list-or-variable : list-intrinsic'

def p_list_or_variable_variable(t):
    'list-or-variable : (AMPERSAND)? variable'

def p_byref_assignment_expression(t):
    'byref-assignment-expression : variable EQUAL AMPERSAND variable'

def p_compound_assignment_expression(t):
    'compound-assignment-expression : variable compound-assignment-operator assignment-expression'

#6

def p_compound_assignment_operator_power(t):
    'compound-assignment-operator : POW_EQUAL'

def p_compound_assignment_operator_multiply(t):
    'compound-assignment-operator : MUL_EQUAL'

def p_compound_assignment_operator_divide(t):
    'compound-assignment-operator : DIV_EQUAL'

def p_compound_assignment_operator_modulus(t):
    'compound-assignment-operator : MOD_EQUAL'

def p_compound_assignment_operator_add(t):
    'compound-assignment-operator : PLUS_EQUAL'

def p_compound_assignment_operator_subtract(t):
    'compound-assignment-operator : MINUS_EQUAL'

def p_compound_assignment_operator_concatenate(t):
    'compound-assignment-operator : CONCAT_EQUAL'

def p_compound_assignment_operator_left_shift(t):
    'compound-assignment-operator : SL_EQUAL'

def p_compound_assignment_operator_right_shift(t):
    'compound-assignment-operator : SR_EQUAL'

def p_compound_assignment_operator_bitwise_AND(t):
    'compound-assignment-operator : AND_EQUAL'

def p_compound_assignment_operator_bitwise_exc_OR(t):
    'compound-assignment-operator : XOR_EQUAL'

def p_compound_assignment_operator_bitwise_inc_OR(t):
    'compound-assignment-operator : OR_EQUAL'

#7

def p_yield_from_expression(t):
    'yield-from-expression : YIELD_FROM assignment-expression'

def p_yield_expression_yield_from(t):
    'yield-expression : yield-from-expression'

def p_yield_expression_yield(t):
    'yield-expression : YIELD'

def p_yield_expression_yield_yield(t):
    'yield-expression : YIELD yield-expression'

def p_yield_expression_yield_yield_from_yield(t):
    'yield-expression : YIELD yield-from-expression DOUBLE_ARROW yield-expression'

def p_print_expression_yield(t):
    'print-expression : yield-expression'

def p_print_expression_print(t):
    'print-expression : PRINT print-expression'

def p_logical_AND_expression_2_print(t):
    'logical-AND-expression-2 : print-expression'

def p_logical_AND_expression_2_and_yield(t):
    'logical-AND-expression-2 : logical-AND-expression-2 AND yield-expression'

#8
def p_logical_exc_OR_expression_logical_AND(t):
    'logical-exc-OR-expression : logical-AND-expression-2'

def p_logical_exc_OR_expression_xor(t):
    'logical-exc-OR-expression : logical-exc-OR-expression XOR logical-AND-expression-2'

def p_logical_inc_OR_expression_2_logical_exc_OR(t):
    'logical-inc-OR-expression-2 : logical-exc-OR-expression'

def p_logical_inc_OR_expression_2_or_logical_exc_OR(t):
    'logical-inc-OR-expression-2 : logical-inc-OR-expression-2 OR logical-exc-OR-expression'

def p_expression_logical_inc_OR(t):
    'expression : logical-inc-OR-expression-2'

def p_expression_include(t):
    'expression : include-expression'

def p_expression_include_once_expression(t):
    'expression : include-once-expression'

def p_expression_require_expression(t):
    'expression : require-expression'

def p_expression_require_once_expression(t):
    'expression : require-once-expression'

def p_include_expression(t):
    'include-expression : INCLUDE expression'

#9

def p_include_once_expression(t):
    'include-once-expression : INCLUDE_ONCE expression'

def p_require_expression(t):
    'require-expression : REQUIRE expression'

def p_require_once_expression(t):
    'require-once-expression : REQUIRE_ONCE expression'

def p_constant_expression(t):
    'constant-expression : expression'

#10

def p_statement_compound(t):
    'statement : compound-statement'

def p_statement_named_label(t):
    'statement : named-label-statement'

def p_statement_expression(t):
    'statement : expression-statement'

def p_statement_selection(t):
    'statement : selection-statement'

def p_statement_iteration(t):
    'statement : iteration-statement'

def p_statement_jump(t):
    'statement : jump-statement'

def p_statement_try(t):
    'statement : try-statement'

def p_statement_declare(t):
    'statement : declare-statement'

def p_statement_echo(t):
    'statement : echo-statement'

def p_statement_unset(t):
    'statement : unset-statement'

def p_statement_const_declaration(t):
    'statement : const-declaration'

def p_statement_function_definition(t):
    'statement : function-definition'

def p_statement_class_declaration(t):
    'statement : class-declaration'

def p_statement_interface_declaration(t):
    'statement : interface-declaration'

def p_statement_trait_declaration(t):
    'statement : trait-declaration'

def p_statement_namespace_definition(t):
    'statement : namespace-definition'

def p_statement_namespace_use_declaration(t):
    'statement : namespace-use-declaration'

def p_statement_global_declaration(t):
    'statement : global-declaration'

def p_statement_function_static_declaration(t):
    'statement : function-static-declaration'

#11

def p_compound_statement(t):
    'compound-statement : LEFT_CBRAC (statement-list)? RIGHT_CBRAC'

def p_statement_list_single(t):
    'statement-list : statement'

def p_statement_list_multiple(t):
    'statement-list : statement-list statement'

def p_named_label_statement(t):
    'named-label-statement : name DOUBLE_POINT'

def p_expression_statement(t):
    'expression-statement : (expression)? SEMICOLON'

def p_selection_statement_if(t):
    'selection-statement : if-statement'

def p_selection_statement_switch(t):
    'selection-statement : switch-statement'

#12

def p_if_statement_1(t):
    'if-statement : IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS statement (elseif-clauses-1)? (else-clause-1)?'

def p_if_statement_2(t):
    'if-statement : IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT statement-list (elseif-clauses-2)? (else-clause-2)? ENDIF SEMICOLON'

def p_elseif_clauses_1_single(t):
    'elseif-clauses-1 : elseif-clause-1'

def p_elseif_clauses_1_multiple(t):
    'elseif-clauses-1 : elseif-clauses-1 elseif-clause-1'

def p_elseif_clause_1(t):
    'elseif-clause-1 : ELSEIF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS statement'

def p_else_clause_1(t):
    'else-clause-1 : ELSE statement'

#13

def p_elseif_clauses_2_single(t):
    'elseif-clauses-2 : elseif-clause-2'

def p_elseif_clauses_2_multiple(t):
    'elseif-clauses-2 : elseif-clauses-2 elseif-clause-2'

def p_elseif_clause_2(t):
    'elseif-clause-2 : ELSEIF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT statement-list'

def p_else_clause_2(t):
    'else-clause-2 : ELSE DOUBLE_POINT statement-list'

def p_switch_statement_1(t):
    'switch-statement : SWITCH LEFT_PARENTHESIS expression RIGHT_PARENTHESIS LEFT_CBRAC (case-statements)? RIGHT_CBRAC'

def p_switch_statement_2(t):
    'switch-statement : SWITCH LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT (case-statements)? ENDSWITCH SEMICOLON'

#14

def p_case_statements_1(t):
    'case-statements : case-statement (case-statements)?'

def p_case_statements_2(t):
    'case-statements : default-statement (case-statements)?'

def p_case_statement(t):
    'case-statement : CASE expression case-default-label-terminator (statement-list)?'

def p_default_statement(t):
    'default-statement : DEFAULT case-default-label-terminator (statement-list)?'

def p_case_default_label_terminator_colon(t):
    'case-default-label-terminator : DOUBLE_POINT'

def p_case_default_label_terminator_semicolon(t):
    'case-default-label-terminator : SEMICOLON'

#15

def p_iteration_statement_while(t):
    'iteration-statement : while-statement'

def p_iteration_statement_do(t):
    'iteration-statement : do-statement'

def p_iteration_statement_for(t):
    'iteration-statement : for-statement'

def p_iteration_statement_foreach(t):
    'iteration-statement : foreach-statement'

def p_while_statement(t):
    'while-statement : WHILE LEFT_PARENTHESIS expression RIGHT_PARENTHESIS statement'

def p_while_statement_block(t):
    'while-statement : WHILE LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT statement-list ENDWHILE SEMICOLON'

def p_do_statement(t):
    'do-statement : DO statement WHILE LEFT_PARENTHESIS expression RIGHT_PARENTHESIS SEMICOLON'

#16

def p_for_statement(t):
    'for-statement : FOR LEFT_PARENTHESIS (for-initializer)? SEMICOLON (for-control)? SEMICOLON (for-end-of-loop)? RIGHT_PARENTHESIS statement'

def p_for_statement_block(t):
    'for-statement : FOR LEFT_PARENTHESIS (for-initializer)? SEMICOLON (for-control)? SEMICOLON (for-end-of-loop)? RIGHT_PARENTHESIS DOUBLE_POINT statement-list ENDFOR SEMICOLON'

def p_for_initializer(t):
    'for-initializer : for-expression-group'

def p_for_control(t):
    'for-control : for-expression-group'

def p_for_end_of_loop(t):
    'for-end-of-loop : for-expression-group'

def p_for_expression_group_single(t):
    'for-expression-group : expression'

def p_for_expression_group_multiple(t):
    'for-expression-group : for-expression-group COLON expression'

#17

def p_foreach_statement(t):
    'foreach-statement : FOREACH LEFT_PARENTHESIS foreach-collection-name AS (foreach-key)? foreach-value RIGHT_PARENTHESIS statement'

def p_foreach_statement_block(t):
    'foreach-statement : FOREACH LEFT_PARENTHESIS foreach-collection-name AS (foreach-key)? foreach-value RIGHT_PARENTHESIS DOUBLE_POINT statement-list ENDFOREACH SEMICOLON'

def p_foreach_collection_name(t):
    'foreach-collection-name : expression'

def p_foreach_key(t):
    'foreach-key : expression DOUBLE_ARROW'

def p_foreach_value(t):
    'foreach-value : foreach-value_expression'

def p_foreach_value_amp_expression(t):
    'foreach-value : AMPERSAND expression'

def p_foreach_value_list_intrinsic(t):
    'foreach-value : list-intrinsic'

#18

def p_jump_statement_goto(t):
    'jump-statement : goto-statement'

def p_jump_statement_continue(t):
    'jump-statement : continue-statement'

def p_jump_statement_break(t):
    'jump-statement : break-statement'

def p_jump_statement_return(t):
    'jump-statement : return-statement'

def p_jump_statement_throw(t):
    'jump-statement : throw-statement'

def p_goto_statement(t):
    'goto-statement : GOTO name SEMICOLON'

def p_continue_statement(t):
    'continue-statement : CONTINUE (breakout-level)? SEMICOLON'

def p_breakout_level(t):
    'breakout-level : INTEGER_LITERAL'

def p_breakout_level_expression(t):
    'breakout-level : LEFT_PARENTHESIS breakout-level RIGHT_PARENTHESIS'

#stiven

# Construcción de la gramática
def p_break_statement(p):
    '''break_statement : BREAK breakout_levelopt SEMICOLON'''

def p_breakout_levelopt(p):
    '''breakout_levelopt : breakout_level
                         |'''

def p_breakout_level_1(p):
    '''breakout_level : expression'''

def p_return_statement(p):
    '''return_statement : RETURN expressionopt SEMICOLON'''

def p_expressionopt(p):
    '''expressionopt : expression
                     |'''

def p_throw_statement(p):
    '''throw_statement : THROW expression SEMICOLON'''

def p_try_statement(p):
    '''try_statement : TRY compound_statement catch_clauses
                     | TRY compound_statement finally_clause
                     | TRY compound_statement catch_clauses finally_clause'''

def p_catch_clauses(p):
    '''catch_clauses : catch_clause
                     | catch_clauses catch_clause'''

def p_catch_clause(p):
    '''catch_clause : CATCH LEFT_PARENTHESIS catch_name_list VARIABLE RIGHT_PARENTHESIS compound_statement'''

def p_catch_name_list(p): #! ojo aca con el | del centro
    '''catch_name_list : qualified_name
                       | catch_name_list 
                       | qualified_name'''

def p_finally_clause(p):
    '''finally_clause : FINALLY compound_statement'''

def p_declare_statement(p):
    '''declare_statement : DECLARE LEFT_PARENTHESIS declare_directive RIGHT_PARENTHESIS statement
                         | DECLARE LEFT_PARENTHESIS declare_directive RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDDECLARE SEMICOLON
                         | DECLARE LEFT_PARENTHESIS declare_directive RIGHT_PARENTHESIS SEMICOLON'''

def p_declare_directive(p):
    '''declare_directive : TICKS EQUALS literal
                         | ENCODING EQUALS literal
                         | STRICT_TYPES EQUALS literal'''

def p_echo_statement(p):
    '''echo_statement : ECHO expression_list SEMICOLON'''

def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''

def p_unset_statement(p):
    '''unset_statement : UNSET LEFT_PARENTHESIS variable_list commaopt RIGHT_PARENTHESIS SEMICOLON'''

def p_commopt(p): #opcionales
    '''commaopt : COMMA
                |'''

def p_function_definition(p):
    '''function_definition : function_definition_header compound_statement'''

def p_function_definition_header(p):
    '''function_definition_header : FUNCTION ampersandopt name LEFT_PARENTHESIS parameter_declaration_listopt RIGHT_PARENTHESIS return_typeopt'''

def p_ampersandopt(p): #opcionales
    '''ampersandopt : AMPERSAND
                    |'''

def p_parameter_declaration_list(p):
    '''parameter_declaration_list : simple_parameter_declaration_list
                                   | variadic_declaration_list'''

def p_simple_parameter_declaration_list(p):
    '''simple_parameter_declaration_list : parameter_declaration
                                          | parameter_declaration_list COMMA parameter_declaration'''

def p_variadic_declaration_list(p):
    '''variadic_declaration_list : simple_parameter_declaration_list COMMA variadic_parameter
                                  | variadic_parameter'''
#-------------------------------------------------------------
def p_parameter_declaration(p):
    '''parameter_declaration : type_declarationopt ampersandopt variable_name default_argument_specifieropt'''

def p_variadic_parameter(p):
    '''variadic_parameter : type_declarationopt ampersandopt ELLIPSIS variable_name'''

def p_return_type(p):
    '''return_type : DOUBLE_POINT type_declaration
                   | DOUBLE_POINT VOID'''
#------------------------------------------------------------
def p_type_declarationopt(p): #opcionales
    '''type_declarationopt : type_declaration
                           |'''

def p_type_declaration(p):
    '''type_declaration : TERNARY_OPERATIONopt base_type_declaration'''

def p_TERNARY_OPERATIONopt(p): #opcionales
    '''TERNARY_OPERATIONopt : TERNARY_OPERATION
                        |'''

def p_base_type_declaration(p):
    '''base_type_declaration : array
                             | callable
                             | iterable
                             | scalar_type
                             | qualified_name'''

def p_scalar_type(p):
    '''scalar_type : BOOL
                   | FLOAT
                   | INT
                   | STRING'''

def p_default_argument_specifieropt(p): #opcionales
    '''default_argument_specifieropt : default_argument_specifier
                                     |'''

def p_default_argument_specifier(p):
    '''default_argument_specifier : EQUAL constant_expression'''

def p_class_declaration(p):
    '''class_declaration : class_modifieropt CLASS name class_base_clauseopt class_interface_clauseopt LEFT_CBRAC class_member_declarationsopt RIGHT_CBRAC'''

def p_class_modifieropt(p): #opcionales
    '''class_modifieropt : class_modifier
                         |'''

def p_class_base_clauseopt(p): #opcionales
    '''class_base_clauseopt : class_base_clause
                            |'''

def p_class_interface_clauseopt(p): #opcionales
    '''class_interface_clauseopt : class_interface_clause
                                    |'''

def p_class_member_declarationsopt(p): #opcionales
    '''class_member_declarationsopt : class_member_declarations
                                    |'''
#-------------------------------------------------------------
#estas no tiene opt
def p_class_modifier(p):
    '''class_modifier : ABSTRACT
                       | FINAL'''

def p_class_base_clause(p):
    '''class_base_clause : EXTENDS qualified_name'''

def p_class_interface_clause(p):
    '''class_interface_clause : IMPLEMENTS qualified_name
                               | class_interface_clause COMMA qualified_name'''

def p_class_member_declarations(p):
    '''class_member_declarations : class_member_declaration
                                  | class_member_declarations class_member_declaration'''

def p_class_member_declaration(p):
    '''class_member_declaration : class_const_declaration
                                 | property_declaration
                                 | method_declaration
                                 | constructor_declaration
                                 | destructor_declaration
                                 | trait_use_clause'''

def p_const_declaration(p):
    '''const_declaration : CONST const_elements SEMICOLON'''
#-------------------------------------------------------------
def p_class_const_declaration(p):
    '''class_const_declaration : visibility_modifieropt CONST const_elements SEMICOLON'''

def p_visibility_modifieropt(p): #opcionales
    '''visibility_modifieropt : visibility_modifier
                                |'''

def p_const_elements(p):
    '''const_elements : const_element
                      | const_elements COMMA const_element'''

def p_const_element(p):
    '''const_element : name EQUAL constant_expression'''

def p_property_declaration(p):
    '''property_declaration : property_modifier property_elements SEMICOLON'''

def p_property_modifier(p):
    '''property_modifier : VAR
                          | visibility_modifier static_modifieropt
                          | static_modifier visibility_modifieropt'''
    
def p_static_modifieropt(p): #opcionales
    '''static_modifieropt : static_modifier
                            |'''

def p_visibility_modifieropt_1(p): #opcionales
    '''visibility_modifieropt : visibility_modifier
                                |'''

def p_visibility_modifier(p):
    '''visibility_modifier : PUBLIC
                            | PROTECTED
                            | PRIVATE'''

def p_static_modifier(p):
    '''static_modifier : STATIC'''
#-------------------------------------------------------------
def p_property_elements(p):
    '''property_elements : property_element
                          | property_elements property_element'''

def p_property_element(p):
    '''property_element : variable_name property_initializeropt SEMICOLON'''

def p_property_initializeropt(p): #opcionales
    '''property_initializeropt : property_initializer
                                 |'''

def p_property_initializer(p):
    '''property_initializer : EQUAL constant_expression'''

def p_method_declaration(p):
    '''method_declaration : method_modifiersopt function_definition
                           | method_modifiers function_definition_header SEMICOLON'''

def p_method_modifiersopt(p): #opcionales
    '''method_modifiersopt : method_modifiers
                            |'''

def p_method_modifiers(p):
    '''method_modifiers : method_modifier
                        | method_modifiers method_modifier'''

def p_method_modifier(p):
    '''method_modifier : visibility_modifier
                       | static_modifier
                       | class_modifier'''

def p_constructor_declaration(p):
    '''constructor_declaration : method_modifiers FUNCTION name AMPERSANDopt __construct LEFT_PARENTHESIS parameter_declaration_listopt RIGHT_PARENTHESIS compound_statement'''

def p_destructor_declaration(p):
    '''destructor_declaration : method_modifiers FUNCTION name AMPERSANDopt __destruct LEFT_PARENTHESIS RIGHT_PARENTHESIS compound_statement'''

def p_parameter_declaration_listopt(p): #opcionales
    '''parameter_declaration_listopt : parameter_declaration_list
                                    |'''

def p_interface_declaration(p):
    '''interface_declaration : INTERFACE name interface_base_clauseopt LEFT_CBRAC interface_member_declarationsopt RIGHT_CBRAC'''

def p_interface_base_clauseopt(p): #opcionales
    '''interface_base_clauseopt : interface_base_clause
                                |'''

def p_interface_member_declarationsopt(p): #opcionales
    '''interface_member_declarationsopt : interface_member_declarations
                                        |'''

def p_interface_base_clause(p):
    '''interface_base_clause : EXTENDS qualified_name
                             | interface_base_clause COMMA qualified_name'''

def p_interface_member_declarations(p):
    '''interface_member_declarations : interface_member_declaration
                                     | interface_member_declarations interface_member_declaration'''

def p_interface_member_declaration(p):
    '''interface_member_declaration : class_const_declaration
                                     | method_declaration'''

def p_trait_declaration(p):
    '''trait_declaration : TRAIT name LEFT_CBRAC trait_member_declarationsopt RIGHT_CBRAC'''

def p_trait_member_declarationsopt(p): #opcionales
    '''trait_member_declarationsopt : trait_member_declarations
                                    |'''

def p_trait_member_declarations(p):
    '''trait_member_declarations : trait_member_declaration
                                 | trait_member_declarations trait_member_declaration'''
#-------------------------------------------------------------
def p_trait_member_declaration(p):
    '''trait_member_declaration : property_declaration
                                 | method_declaration
                                 | constructor_declaration
                                 | destructor_declaration
                                 | trait_use_clauses'''

def p_trait_use_clauses(p):
    '''trait_use_clauses : trait_use_clause
                         | trait_use_clauses trait_use_clause'''

def p_trait_use_clause(p):
    '''trait_use_clause : USE trait_name_list trait_use_specification'''

def p_trait_name_list(p):
    '''trait_name_list : qualified_name
                       | trait_name_list COMMA qualified_name'''

def p_trait_use_specification(p):
    '''trait_use_specification : SEMICOLON
                               | LEFT_CBRAC trait_select_and_alias_clausesopt RIGHT_CBRAC'''
    
def p_trait_select_and_alias_clausesopt(p): #opcionales
    '''trait_select_and_alias_clausesopt : trait_select_and_alias_clauses
                                            |'''

def p_trait_select_and_alias_clauses(p):
    '''trait_select_and_alias_clauses : trait_select_and_alias_clause
                                      | trait_select_and_alias_clauses trait_select_and_alias_clause'''

def p_trait_select_and_alias_clause(p):
    '''trait_select_and_alias_clause : trait_select_insteadof_clause SEMICOLON
                                     | trait_alias_as_clause SEMICOLON'''

def p_trait_select_insteadof_clause(p):
    '''trait_select_insteadof_clause : qualified_name DOUBLE_COLON name INSTEADOF trait_name_list'''
#-------------------------------------------------------------
def p_trait_alias_as_clause(p):
    '''trait_alias_as_clause : name AS visibility_modifieropt name
                              | name AS visibility_modifier nameopt'''

def p_visibility_modifieropt_2(p): #opcionales
    '''visibility_modifieropt : visibility_modifier
                                |'''

def p_nameopt(p): #opcionales
    '''nameopt : name
                |'''

def p_namespace_definition(p):
    '''namespace_definition : NAMESPACE namespace_name SEMICOLON
                             | NAMESPACE namespace_nameopt compound_statement'''

def p_namespace_nameopt(p): #opcionales
    '''namespace_nameopt : namespace_name
                            |'''

def p_namespace_use_declaration(p):
    '''namespace_use_declaration : USE namespace_function_or_constopt namespace_use_clauses SEMICOLON
                                  | USE namespace_function_or_const NS_SEPARATORopt namespace_name NS_SEPARATOR LEFT_CBRAC namespace_use_group_clauses_1 RIGHT_CBRAC SEMICOLON
                                  | USE NS_SEPARATORopt namespace_name NS_SEPARATOR LEFT_CBRAC namespace_use_group_clauses_2 RIGHT_CBRAC SEMICOLON'''

def p_namespace_function_or_constopt(p): #opcionales
    '''namespace_function_or_constopt : namespace_function_or_const
                                      |'''

def p_NS_SEPARATORopt(p): #opcionales
    '''NS_SEPARATORopt : NS_SEPARATOR
                    |'''

def p_namespace_use_clauses(p):
    '''namespace_use_clauses : namespace_use_clause
                              | namespace_use_clauses COMMA namespace_use_clause'''

def p_namespace_use_clause(p):
    '''namespace_use_clause : qualified_name namespace_aliasing_clauseopt'''

def p_namespace_aliasing_clauseopt(p): #opcionales
    '''namespace_aliasing_clauseopt : namespace_aliasing_clause
                                    |'''

def p_namespace_aliasing_clause(p):
    '''namespace_aliasing_clause : AS name'''

def p_namespace_function_or_const(p):
    '''namespace_function_or_const : FUNCTION
                                    | CONST'''

def p_namespace_use_group_clauses_1(p):
    '''namespace_use_group_clauses_1 : namespace_use_group_clause_1
                                      | namespace_use_group_clauses_1 COMMA namespace_use_group_clause_1'''

def p_namespace_use_group_clause_1(p):
    '''namespace_use_group_clause_1 : namespace_name namespace_aliasing_clauseopt'''


def p_namespace_use_group_clauses_2(p):
    '''namespace_use_group_clauses_2 : namespace_use_group_clause_2
                                      | namespace_use_group_clauses_2 COMMA namespace_use_group_clause_2'''

def p_namespace_use_group_clause_2(p):
    '''namespace_use_group_clause_2 : namespace_function_or_constopt namespace_name namespace_aliasing_clauseopt'''

def p_namespace_aliasing_clauseopt_1(p): #opcionales
    '''namespace_aliasing_clauseopt : namespace_aliasing_clause
                                    |'''
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
    result = parser.parse(s)
    print(result)