import ply.yacc as yacc
from AnalixadorLex import tokens
import AnalixadorLex
import sys

VERBOSE = 1

#tokens
# def p_input_file_one(t):
#     'input_file : input_element'

# def p_input_file_two(t):
#     'input_file : input_file input_element'

# def p_input_element_comment(t):
#     'input_element : comment'

# def p_input_element_whitespace(t):
#     'input_element : white_space'

# def p_input_element_token(t):
#     'input_element : token'

# def p_comment_single_line_comment(t):
#     'comment : single_line_comment'

# def p_comment_delimited_comment(t):
#     'comment : delimited_comment'

# def p_single_line_comment_one(t):
#     'single-line-comment : DIVIDE DIVIDE input-charactersopt'

# def p_single_line_comment_two(t):
#     '''single-line-comment : '#' (input-characters)?'''

# def p_input_characters_one(t):
#     'input-characters : input-character'

# def p_input_characters_two(t):
#     'input-characters : input-characters input-character'

# def p_input_character(t):
#     'input-character : STRING new-line'

# def p_new_line_CR(t):
#     '''new-line : '\r''''

# def p_new_line_LF(t):
#     ''''new-line : '\n'''''

# def p_new_line_CR_LF(t):
#     '''new-line : '\r' '\n''''

# def p_delimited_comment_empty(t):
#     '''delimited-comment : DIVIDE '' '' DIVIDE'''

# def p_delimited_comment_sequence(t):
#     '''delimited-comment : DIVIDE '' STRING '' DIVIDE'''

# def p_white_space_one(t):
#     'white-space : white-space-character'

# def p_white_space_two(t):
#     'white-space : white-space white-space-character'



# def p_white_space_character_new_line(t):
#     'white-space-character : WHITESPACE'

# def p_token_variable_name(t):
#     'token : variable-name'

# def p_token_name(t):
#     'token : name'

# def p_token_keyword(t):
#     'token : keyword'

# def p_token_integer_literal(t):
#     'token : integer-literal'

# def p_token_floating_literal(t):
#     'token : floating-literal'

# def p_token_string_literal(t):
#     'token : string-literal'

# def p_token_operator_or_punctuator(t):
#     'token : operator-or-punctuator'

# def p_variable_name(t):
#     'variable-name : VARIABLE'

# #5

# def p_namespace_name_as_a_prefix_backslash(t):
#     'namespace-name-as-a-prefix : NS_SEPARATOR '

# def p_namespace_name_as_a_prefix_backslash_opt(t):
#     'namespace-name-as-a-prefix : (NS_SEPARATOR)? namespace-name NS_SEPARATOR '

# def p_namespace_name_as_a_prefix_namespace(t):
#     'namespace-name-as-a-prefix : NAMESPACE NS_SEPARATOR '

# def p_namespace_name_as_a_prefix_namespace_backslash(t):
#     'namespace-name-as-a-prefix : NAMESPACE NS_SEPARATOR namespace-name NS_SEPARATOR '

# def p_qualified_name_namespace_name_as_a_prefix_opt(t):
#     'qualified-name : (namespace-name-as-a-prefix)? name'


# #6

# def p_name_one(t):
#     'name : name-nondigit'

# def p_name_two(t):
#     'name : name name-nondigit'

# def p_name_three(t):
#     'name : name digit'

# def p_name_nondigit(t):
#     'name-nondigit : nondigit'

# def p_name_nondigit_extended(t):
#     '''name-nondigit : '[\x80-\xff]''''

# def p_nondigit(t):
#     ''''[a-zA-Z0-9_\x7f-\xff^\$]''''

# #7

# def p_keyword_abstract(t):
#     'keyword : ABSTRACT'

# def p_keyword_and(t):
#     'keyword : AND'

# def p_keyword_array(t):
#     'keyword : ARRAY'

# def p_keyword_as(t):
#     'keyword : AS'

# def p_keyword_break(t):
#     'keyword : BREAK'

# def p_keyword_callable(t):
#     'keyword : CALLABLE'

# def p_keyword_case(t):
#     'keyword : CASE'

# def p_keyword_catch(t):
#     'keyword : CATCH'

# def p_keyword_class(t):
#     'keyword : CLASS'

# def p_keyword_clone(t):
#     'keyword : CLONE'

# def p_keyword_const(t):
#     'keyword : CONST'

# def p_keyword_continue(t):
#     'keyword : CONTINUE'

# def p_keyword_declare(t):
#     'keyword : DECLARE'

# def p_keyword_default(t):
#     'keyword : DEFAULT'

# def p_keyword_die(t):
#     'keyword : DIE'

# def p_keyword_do(t):
#     'keyword : DO'

# def p_keyword_echo(t):
#     'keyword : ECHO'

# def p_keyword_else(t):
#     'keyword : ELSE'

# def p_keyword_elseif(t):
#     'keyword : ELSEIF'

# def p_keyword_empty(t):
#     'keyword : EMPTY'

# def p_keyword_enddeclare(t):
#     'keyword : ENDDECLARE'

# def p_keyword_endfor(t):
#     'keyword : ENDFOR'

# def p_keyword_endforeach(t):
#     'keyword : ENDFOREACH'

# def p_keyword_endif(t):
#     'keyword : ENDIF'

# def p_keyword_endswitch(t):
#     'keyword : ENDSWITCH'

# def p_keyword_endwhile(t):
#     'keyword : ENDWHILE'

# def p_keyword_eval(t):
#     'keyword : EVAL'

# def p_keyword_exit(t):
#     'keyword : EXIT'

# def p_keyword_extends(t):
#     'keyword : EXTENDS'

# def p_keyword_final(t):
#     'keyword : FINAL'

# def p_keyword_finally(t):
#     'keyword : FINALLY'

# def p_keyword_for(t):
#     'keyword : FOR'

# def p_keyword_foreach(t):
#     'keyword : FOREACH'

# def p_keyword_function(t):
#     'keyword : FUNCTION'

# def p_keyword_global(t):
#     'keyword : GLOBAL'

# def p_keyword_goto(t):
#     'keyword : GOTO'

# def p_keyword_if(t):
#     'keyword : IF'

# def p_keyword_implements(t):
#     'keyword : IMPLEMENTS'

# def p_keyword_include(t):
#     'keyword : INCLUDE'

# def p_keyword_include_once(t):
#     'keyword : INCLUDE_ONCE'

# def p_keyword_instanceof(t):
#     'keyword : INSTANCEOF'

# def p_keyword_insteadof(t):
#     'keyword : INSTEADOF'

# def p_keyword_interface(t):
#     'keyword : INTERFACE'

# def p_keyword_isset(t):
#     'keyword : ISSET'

# def p_keyword_list(t):
#     'keyword : LIST'

# def p_keyword_namespace(t):
#     'keyword : NAMESPACE'

# def p_keyword_new(t):
#     'keyword : NEW'

# def p_keyword_or(t):
#     'keyword : OR'

# def p_keyword_print(t):
#     'keyword : PRINT'

# def p_keyword_private(t):
#     'keyword : PRIVATE'

# def p_keyword_protected(t):
#     'keyword : PROTECTED'

# def p_keyword_public(t):
#     'keyword : PUBLIC'

# def p_keyword_require(t):
#     'keyword : REQUIRE'

# def p_keyword_require_once(t):
#     'keyword : REQUIRE_ONCE'

# def p_keyword_return(t):
#     'keyword : RETURN'

# def p_keyword_static(t):
#     'keyword : STATIC'

# def p_keyword_switch(t):
#     'keyword : SWITCH'

# def p_keyword_throw(t):
#     'keyword : THROW'

# def p_keyword_trait(t):
#     'keyword : TRAIT'

# def p_keyword_try(t):
#     'keyword : TRY'

# def p_keyword_unset(t):
#     'keyword : UNSET'

# def p_keyword_use(t):
#     'keyword : USE'

# def p_keyword_var(t):
#     'keyword : VAR'

# def p_keyword_while(t):
#     'keyword : WHILE'

# def p_keyword_xor(t):
#     'keyword : XOR'

# def p_keyword_yield(t):
#     'keyword : YIELD'

# def p_keyword_yield_from(t):
#     'keyword : YIELD FROM'

# #8

# def p_integer_literal_decimal(t):
#     'integer-literal : decimal-literal'

# def p_integer_literal_octal(t):
#     'integer-literal : octal-literal'

# def p_integer_literal_hexadecimal(t):
#     'integer-literal : hexadecimal-literal'

# def p_integer_literal_binary(t):
#     'integer-literal : binary-literal'

# def p_decimal_literal_nonzero_digit(t):
#     'decimal-literal : nonzero-digit'

# def p_decimal_literal_multiple(t):
#     'decimal-literal : decimal-literal digit'

# def p_octal_literal_zero(t):
#     '''octal-literal : '0''''

# def p_octal_literal_multiple(t):
#     'octal-literal : octal-literal octal-digit'

# #9

# def p_hexadecimal_literal_prefix_digit(t):
#     'hexadecimal-literal : hexadecimal-prefix hexadecimal-digit'

# def p_hexadecimal_literal_multiple(t):
#     'hexadecimal-literal : hexadecimal-literal hexadecimal-digit'

# #10

# def p_hexadecimal_prefix(t):
#     '''hexadecimal-prefix: '0(x|X)''''

# #11

# def p_binary_literal_prefix_digit(t):
#     'binary-literal : binary-prefix binary-digit'

# def p_binary_literal_multiple(t):
#     'binary-literal : binary-literal binary-digit'

# #12

# def p_binary_prefix(t):
#     '''hexadecimal-prefix: '0(b|B)''''

# #13

# def p_digit(t):
#     ''''[0-9]''''

# def p_nonzero_digit(t):
#     ''''[1-9]''''

# def p_octal_digit(t):
#     ''''[0-7]''''

# def p_hexadecimal_digit(t):
#     ''''([0-9]|[a-f]|[A-F])''''

# def p_hexadecimal_digit(t):
#     ''''[0-1]''''

# #14

# def p_floating_literal_fractional(t):
#     'floating-literal : fractional-literal (exponent-part)?'

# def p_floating_literal_digit_sequence(t):
#     'floating-literal : digit-sequence exponent-part'

# def p_fractional_literal_sequence_dot_sequence(t):
#     'fractional-literal : (digit-sequence)? CONCAT digit-sequence'

# def p_fractional_literal_sequence_dot(t):
#     'fractional-literal : digit-sequence CONCAT'

# #15

# def p_exponent_part_e(t):
#     '''exponent-part : 'e' (sign)? digit-sequence'''

# def p_exponent_part_E(t):
#     '''exponent-part : 'E' (sign)? digit-sequence'''

# #16

# def p_sign(t):
#     '''sign: '+|-''''

# #17

# def p_digit_sequence_single(t):
#     'digit-sequence : digit'

# def p_digit_sequence_multiple(t):
#     'digit-sequence : digit-sequence digit'

# def p_string_literal_single_quoted(t):
#     'string-literal : single-quoted-string-literal'

# def p_string_literal_double_quoted(t):
#     'string-literal : double-quoted-string-literal'

# def p_string_literal_heredoc(t):
#     'string-literal : heredoc-string-literal'

# #18

# def p_string_literal_nowdoc(t):
#     'string-literal : nowdoc-string-literal'

# def p_single_quoted_string_literal(t):
#     'single-quoted-string-literal : b-prefixopt SINGLE_QUOTE sq-char-sequenceopt SINGLE_QUOTE'

# def p_sq_char_sequence_single(t):
#     'sq-char-sequence : sq-char'

# def p_sq_char_sequence_multiple(t):
#     'sq-char-sequence : sq-char-sequence sq-char'


#Galvis


#Basic concepts

def p_script_one(t):
    'script : script_section'

def p_script_two(t):
    'script : script script_section'

def p_script_section(t):
    'script_section : text_opt start_tag statement_list_opt end_tag_opt text_opt'

def p_text_opt(t):
    '''text_opt : STRING 
                    |'''
    
def p_end_tag_opt(t):
    '''end_tag_opt : CLOSE_TAG
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

def p_namespace_name_one(t):
    'namespace_name : NAME'

def p_namespace_name_two(t):
    'namespace_name : namespace_name NS_SEPARATOR NAME'

# def p_text(t):
#     'text : ARBITRARY_TEXT'

#variables

def p_function_static_declaration(t):
    'function_static_declaration : STATIC static_variable_name_list SEMICOLON'

def p_static_variable_name_list_single(t):
    'static_variable_name_list : static_variable_declaration'

def p_static_variable_name_list_multiple(t):
    'static_variable_name_list : static_variable_name_list  static_variable_declaration'

def p_static_variable_declaration(t):
    'static_variable_declaration : VARIABLE function_static_initializer_opt'

def p_function_static_initializer(t):
   '''function_static_initializer : EQUAL   constant_expression'''


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
    'variable_name_list : variable_name_list  simple_variable'

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
    '''simple_variable : VARIABLE
                       | DOLLAR simple_variable
                       | DOLLAR LEFT_CBRAC expression RIGHT_CBRAC'''

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

def p_integer_literal(t):
    'integer_literal : LNUMBER'

def p_floating_literal(t):
    'floating_literal : DNUMBER'

def p_string_literal(p):
    '''string_literal : STRING'''

def p_intrinsic(t):
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
    '''isset_intrinsic : ISSET LEFT_PARENTHESIS variable_list_opt RIGHT_PARENTHESIS'''

def p_variable_list_opt(t):
    """variable_list_opt : variable_list """

def p_variable_list_single(t):
    'variable_list : variable'

def p_variable_list_multiple(t):
    'variable_list : variable_list  variable'

def p_anonymous_function_creation_expression(t):
    '''anonymous_function_creation_expression : static_opt FUNCTION AMPERSAND_opt LEFT_PARENTHESIS parameter_declaration_list_opt RIGHT_PARENTHESIS anonymous_function_use_clause_opt return_type_opt compound_statement'''

def p_static_opt(t):
    '''static_opt : STATIC
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
    '''use_variable_name_list : AMPERSAND_opt VARIABLE'''

def p_use_variable_name_list_multiple(t):
    '''use_variable_name_list : use_variable_name_list  AMPERSAND_opt VARIABLE'''

def p_object_creation_expression(t):
    '''object_creation_expression : NEW class_type_designator LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS
                                  | NEW class_type_designator LEFT_PARENTHESIS argument_expression_list COLON RIGHT_PARENTHESIS
                                  | NEW class_type_designator
                                  | NEW CLASS LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS class_base_clause_opt class_interface_clause_opt LEFT_CBRAC class_member_declarations_opt RIGHT_PARENTHESIS
                                  | NEW CLASS class_base_clause_opt class_interface_clause_opt LEFT_CBRAC class_member_declarations_opt RIGHT_PARENTHESIS'''

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

def p_new_variable(t):
    '''new_variable : new_variable LEFT_CBRAC expression_opt RIGHT_CBRAC
                    | new_variable LEFT_CBRAC expression RIGHT_PARENTHESIS
                    | new_variable ARROW member_name
                    | qualified_name DOUBLE_COLON simple_variable
                    | relative_scope DOUBLE_COLON simple_variable
                    | new_variable DOUBLE_COLON simple_variable'''

def p_expression_opt_1(t):
    '''expression_opt : expression
                        |'''

def p_array_creation_expression_array(t):
    '''array_creation_expression : ARRAY LEFT_PARENTHESIS array_initializer_opt RIGHT_PARENTHESIS
                                  | LEFT_CBRAC array_initializer_opt RIGHT_CBRAC'''

def p_array_initializer_opt(t):
    '''array_initializer_opt : array_initializer
                              | '''

def p_array_initializer(t):
    '''array_initializer : array_initializer_list
                        | array_initializer_list COLON'''

def p_array_initializer_list(t):
    '''array_initializer_list : array_element_initializer
                              | array_element_initializer COLON array_element_initializer'''

def p_array_element_initializer_single(t):
    '''array_element_initializer : AMPERSAND_opt element_value'''

def p_array_element_initializer_key_value(t):
    '''array_element_initializer : element_key ARROW  AMPERSAND_opt element_value'''

def p_element_key(t):
    '''element_key : expression'''

def p_element_value(t):
    '''element_value : expression'''

def p_subscript_expression_brackets(t):
    '''subscript_expression : dereferencable_expression LEFT_CBRAC expression_opt RIGHT_CBRAC'''

def p_subscript_expression_deprecated(t):
    '''subscript_expression : dereferencable_expression LEFT_CBRAC expression RIGHT_PARENTHESIS'''

def p_function_call_expression_qualified_name(t):
    '''function_call_expression : qualified_name LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS
                                | qualified_name LEFT_PARENTHESIS argument_expression_list  RIGHT_PARENTHESIS'''

def p_function_call_expression_callable_expression(t):
    '''function_call_expression : callable_expression LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS
                                | callable_expression LEFT_PARENTHESIS argument_expression_list  RIGHT_PARENTHESIS'''

def p_argument_expression_list_single(t):
    '''argument_expression_list : argument_expression'''

def p_argument_expression_list_multiple(t):
    '''argument_expression_list : argument_expression_list  argument_expression'''

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
    '''member_name : LEFT_CBRAC expression RIGHT_PARENTHESIS'''

def p_member_call_expression(t):
    '''member_call_expression : dereferencable_expression ARROW member_name LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS
                              | dereferencable_expression ARROW member_name LEFT_PARENTHESIS argument_expression_list  RIGHT_PARENTHESIS'''

def p_postfix_increment_expression(t):
    '''postfix_increment_expression : variable DOUBLEPLUS'''

def p_postfix_decrement_expression(t):
    '''postfix_decrement_expression : variable DOUBLELESS'''

def p_prefix_increment_expression(t):
    '''prefix_increment_expression : DOUBLEPLUS variable'''

def p_prefix_decrement_expression(t):
    '''prefix_decrement_expression : DOUBLELESS variable'''

def p_shell_command_expression(t):
    '''shell_command_expression : BACKTICK dq_char_sequence_opt BACKTICK'''

def p_dq_char_sequence_opt(t):
    '''dq_char_sequence_opt : DQ_CHAR_SEQUENCE
                            |'''

def p_scoped_property_access_expression(t):
    '''scoped_property_access_expression : scope_resolution_qualifier DOUBLE_COLON simple_variable'''

def p_scoped_call_expression(t):
    '''scoped_call_expression : scope_resolution_qualifier DOUBLE_COLON member_name LEFT_PARENTHESIS argument_expression_list_opt RIGHT_PARENTHESIS
                               | scope_resolution_qualifier DOUBLE_COLON member_name LEFT_PARENTHESIS argument_expression_list  RIGHT_PARENTHESIS'''

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
                                  | clone_expression DOUBLEASTERISK exponentiation_expression'''

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
    '''unary_operator : LESS'''

def p_unary_operator_tilde(t):
    '''unary_operator : BITWISE_NOT'''

def p_error_control_expression(t):
    '''error_control_expression : AT unary_expression'''

def p_cast_expression(t):
    '''cast_expression : LEFT_PARENTHESIS RIGHT_PARENTHESIS unary_expression'''

# def p_cast_type(t):
#     '''cast_type : ARRAY
#                  | BINARY
#                  | BOOL
#                  | BOOLEAN
#                  | DOUBLE
#                  | INT
#                  | INTEGER
#                  | FLOAT
#                  | OBJECT
#                  | REAL
#                  | STRING
#                  | UNSET'''

def p_instanceof_expression(t):
    '''instanceof_expression : unary_expression
                             | instanceof_subj INSTANCEOF class_type_designator'''

def p_instanceof_subj(t):
    '''instanceof_subj : instanceof_expression'''

def p_logical_not_expression(t):
    '''logical_not_expression : instanceof_expression
                               | NEGATION instanceof_expression'''

def p_multiplicative_expression(t):
    '''multiplicative_expression : logical_not_expression
                                  | multiplicative_expression ASTERISK logical_not_expression
                                  | multiplicative_expression DIVIDE logical_not_expression
                                  | multiplicative_expression MODULO logical_not_expression'''


#Luis
#1

def p_additive_expression_multiplicative(t):
    'additive_expression : multiplicative_expression'

def p_additive_expression_addition(t):
    'additive_expression : additive_expression PLUS multiplicative_expression'

def p_additive_expression_subtraction(t):
    'additive_expression : additive_expression LESS multiplicative_expression'

def p_additive_expression_concatenation(t):
    'additive_expression : additive_expression CONCAT multiplicative_expression'

def p_shift_expression_additive(t):
    'shift_expression : additive_expression'

def p_shift_expression_left_shift(t):
    'shift_expression : shift_expression SL additive_expression'

def p_shift_expression_right_shift(t):
    'shift_expression : shift_expression SR additive_expression'

def p_relational_expression_shift(t):
    'relational_expression : shift_expression'

def p_relational_expression_less_than(t):
    'relational_expression : relational_expression LESS_THAN shift_expression'

def p_relational_expression_greater_than(t):
    'relational_expression : relational_expression IS_SMALLER_OR_EQUAL shift_expression'

def p_relational_expression_less_than_or_equal(t):
    'relational_expression : relational_expression IS_GREATER_OR_EQUAL shift_expression'

def p_relational_expression_greater_than_or_equal(t):
    'relational_expression : relational_expression GREATER_THAN_OR_EQUAL shift_expression'

def p_relational_expression_spaceship(t):
    'relational_expression : relational_expression SPACESHIP shift_expression'


#2

def p_equality_expression_relational(t):
    'equality_expression : relational_expression'

def p_equality_expression_equal(t):
    'equality_expression : equality_expression EQUAL relational_expression'

def p_equality_expression_not_equal(t):
    'equality_expression : equality_expression IS_NOT_EQUAL relational_expression'

def p_equality_expression_identical(t):
    'equality_expression : equality_expression IS_IDENTICAL relational_expression'

def p_equality_expression_not_identical(t):
    'equality_expression : equality_expression IS_NOT_IDENTICAL relational_expression'

def p_bitwise_AND_expression_equality(t):
    'bitwise_AND_expression : equality_expression'

def p_bitwise_AND_expression_AND(t):
    'bitwise_AND_expression : bitwise_AND_expression AMPERSAND equality_expression'

def p_bitwise_exc_OR_expression_AND(t):
    'bitwise_exc_OR_expression : bitwise_AND_expression'

def p_bitwise_exc_OR_expression_exc_OR(t):
    'bitwise_exc_OR_expression : bitwise_exc_OR_expression BITWISE_XOR bitwise_AND_expression'

def p_bitwise_inc_OR_expression_exc_OR(t):
    'bitwise_inc_OR_expression : bitwise_exc_OR_expression'

def p_bitwise_inc_OR_expression_inc_OR(t):
    'bitwise_inc_OR_expression : bitwise_inc_OR_expression BITWISE_OR bitwise_exc_OR_expression'

#3

def p_logical_AND_expression_1_bitwise_inc_OR(t):
    'logical_AND_expression_1 : bitwise_inc_OR_expression'

def p_logical_AND_expression_1_AND(t):
    'logical_AND_expression_1 : logical_AND_expression_1 AMPERSAND AMPERSAND bitwise_inc_OR_expression'

def p_logical_inc_OR_expression_1_logical_AND(t):
    'logical_inc_OR_expression_1 : logical_AND_expression_1'

def p_logical_inc_OR_expression_1_OR(t):
    'logical_inc_OR_expression_1 : logical_inc_OR_expression_1 BITWISE_OR BITWISE_OR logical_AND_expression_1'

def p_coalesce_expression_logical_inc_OR(t):
    'coalesce_expression : logical_inc_OR_expression_1'

def p_coalesce_expression_coalesce(t):
    'coalesce_expression : logical_inc_OR_expression_1 COALESCE coalesce_expression'

def p_conditional_expression_coalesce(t):
    'conditional_expression : coalesce_expression'

def p_conditional_expression_ternary(t):
    '''conditional_expression : conditional_expression TERNARY_OPERATION expression DOUBLE_POINT coalesce_expression
                                | conditional_expression TERNARY_OPERATION DOUBLE_POINT coalesce_expression'''

#4

def p_assignment_expression_conditional(t):
    'assignment_expression : conditional_expression'

def p_assignment_expression_simple(t):
    'assignment_expression : simple_assignment_expression'

def p_assignment_expression_compound(t):
    'assignment_expression : compound_assignment_expression'

def p_simple_assignment_expression_variable(t):
    'simple_assignment_expression : variable EQUAL assignment_expression'

def p_simple_assignment_expression_list_intrinsic(t):
    'simple_assignment_expression : list_intrinsic EQUAL assignment_expression'

def p_list_intrinsic(t):
    'list_intrinsic : LIST LEFT_PARENTHESIS list_expression_list RIGHT_PARENTHESIS'

def p_list_expression_list_unkeyed(t):
    'list_expression_list : unkeyed_list_expression_list'

def p_list_expression_list_keyed(t):
    '''list_expression_list : keyed_list_expression_list COLON
                                | keyed_list_expression_list'''

def p_unkeyed_list_expression_list_single(t):
    'unkeyed_list_expression_list : list_or_variable'

def p_unkeyed_list_expression_list_comma(t):
    'unkeyed_list_expression_list : COLON'

def p_unkeyed_list_expression_list_multiple(t):
    '''unkeyed_list_expression_list : unkeyed_list_expression_list COLON list_or_variable COLON
                                        | unkeyed_list_expression_list COLON list_or_variable'''

def p_keyed_list_expression_list_single(t):
    'keyed_list_expression_list : expression DOUBLE_ARROW list_or_variable'

def p_keyed_list_expression_list_multiple(t):
    'keyed_list_expression_list : keyed_list_expression_list COLON expression DOUBLE_ARROW list_or_variable'

#5

def p_list_or_variable_list_intrinsic(t):
    'list_or_variable : list_intrinsic'

def p_list_or_variable_variable(t):
    '''list_or_variable : AMPERSAND variable
                            | variable'''

def p_byref_assignment_expression(t):
    'byref_assignment_expression : variable EQUAL AMPERSAND variable'

def p_compound_assignment_expression(t):
    'compound_assignment_expression : variable compound_assignment_operator assignment_expression'

#6

def p_compound_assignment_operator_power(t):
    'compound_assignment_operator : POW_EQUAL'

def p_compound_assignment_operator_multiply(t):
    'compound_assignment_operator : MUL_EQUAL'

def p_compound_assignment_operator_divide(t):
    'compound_assignment_operator : DIV_EQUAL'

def p_compound_assignment_operator_modulus(t):
    'compound_assignment_operator : MOD_EQUAL'

def p_compound_assignment_operator_add(t):
    'compound_assignment_operator : PLUS_EQUAL'

def p_compound_assignment_operator_subtract(t):
    'compound_assignment_operator : MINUS_EQUAL'

def p_compound_assignment_operator_concatenate(t):
    'compound_assignment_operator : CONCAT_EQUAL'

def p_compound_assignment_operator_left_shift(t):
    'compound_assignment_operator : SL_EQUAL'

def p_compound_assignment_operator_right_shift(t):
    'compound_assignment_operator : SR_EQUAL'

def p_compound_assignment_operator_bitwise_AND(t):
    'compound_assignment_operator : AND_EQUAL'

def p_compound_assignment_operator_bitwise_exc_OR(t):
    'compound_assignment_operator : XOR_EQUAL'

def p_compound_assignment_operator_bitwise_inc_OR(t):
    'compound_assignment_operator : OR_EQUAL'

#7

def p_yield_from_expression(t):
    'yield_from_expression : YIELD_FROM assignment_expression'

def p_yield_expression_yield_from(t):
    'yield_expression : yield_from_expression'

def p_yield_expression_yield(t):
    'yield_expression : YIELD'

def p_yield_expression_yield_yield(t):
    'yield_expression : YIELD yield_expression'

def p_yield_expression_yield_yield_from_yield(t):
    'yield_expression : YIELD yield_from_expression DOUBLE_ARROW yield_expression'

def p_print_expression_yield(t):
    'print_expression : yield_expression'

def p_print_expression_print(t):
    'print_expression : PRINT print_expression'

def p_logical_AND_expression_2_print(t):
    'logical_AND_expression_2 : print_expression'

def p_logical_AND_expression_2_and_yield(t):
    'logical_AND_expression_2 : logical_AND_expression_2 AND yield_expression'

#! 8 hay que revisar estas expresiones esta muy rara
def p_logical_exc_OR_expression_logical_AND(t):
    'logical_exc_OR_expression : logical_AND_expression_2'

def p_logical_exc_OR_expression_xor(t):
    'logical_exc_OR_expression : logical_exc_OR_expression XOR logical_AND_expression_2'

def p_logical_inc_OR_expression_2_logical_exc_OR(t):
    'logical_inc_OR_expression_2 : logical_exc_OR_expression'

def p_logical_inc_OR_expression_2_or_logical_exc_OR(t):
    'logical_inc_OR_expression_2 : logical_inc_OR_expression_2 OR logical_exc_OR_expression'

def p_expression_logical_inc_OR(t):
    'expression : logical_inc_OR_expression_2'

def p_expression_include(t):
    'expression : include_expression'

def p_expression_include_once_expression(t):
    'expression : include_once_expression'

def p_expression_require_expression(t):
    'expression : require_expression'

def p_expression_require_once_expression(t):
    'expression : require_once_expression'

def p_include_expression(t):
    'include_expression : INCLUDE expression'

#9

def p_include_once_expression(t):
    'include_once_expression : INCLUDE_ONCE expression'

def p_require_expression(t):
    'require_expression : REQUIRE expression'

def p_require_once_expression(t):
    'require_once_expression : REQUIRE_ONCE expression'

def p_constant_expression(t):
    'constant_expression : expression'

#10

def p_statement_compound(t):
    'statement : compound_statement'

def p_statement_named_label(t):
    'statement : named_label_statement'

def p_statement_expression(t):
    'statement : expression_statement'

def p_statement_selection(t):
    'statement : selection_statement'

def p_statement_iteration(t):
    'statement : iteration_statement'

def p_statement_jump(t):
    'statement : jump_statement'

def p_statement_try(t):
    'statement : try_statement'

def p_statement_declare(t):
    'statement : declare_statement'

def p_statement_echo(t):
    'statement : echo_statement'

def p_statement_unset(t):
    'statement : unset_statement'

def p_statement_const_declaration(t):
    'statement : const_declaration'

def p_statement_function_definition(t):
    'statement : function_definition'

def p_statement_class_declaration(t):
    'statement : class_declaration'

def p_statement_interface_declaration(t):
    'statement : interface_declaration'

def p_statement_trait_declaration(t):
    'statement : trait_declaration'

def p_statement_namespace_definition(t):
    'statement : namespace_definition'

def p_statement_namespace_use_declaration(t):
    'statement : namespace_use_declaration'

def p_statement_global_declaration(t):
    'statement : global_declaration'

def p_statement_function_static_declaration(t):
    'statement : function_static_declaration'

#11

def p_compound_statement(t):
    '''compound_statement : LEFT_CBRAC statement_list RIGHT_CBRAC
                            | LEFT_CBRAC RIGHT_CBRAC'''

def p_statement_list(t):
    'statement_list : statement'

def p_statement_list_multiple(t):
    'statement_list : statement_list statement'

def p_named_label_statement(t):
    'named_label_statement : name DOUBLE_POINT'

def p_expression_statement(t):
    '''expression_statement : expression SEMICOLON
                            | SEMICOLON'''

def p_selection_statement_if(t):
    'selection_statement : if_statement'

def p_selection_statement_switch(t):
    'selection_statement : switch_statement'

#12

def p_if_statement_1(t):
    '''if_statement : IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS statement elseif_clauses_1 else_clause_1
                        | IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS statement elseif_clauses_1
                        | IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS statement else_clause_1
                        | IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS statement'''

def p_if_statement_2(t):
    '''if_statement : IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT statement_list elseif_clauses_2 else_clause_2 ENDIF SEMICOLON
                        | IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT statement_list elseif_clauses_2 ENDIF SEMICOLON
                        | IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT statement_list else_clause_2 ENDIF SEMICOLON'''

def p_elseif_clauses_1_single(t):
    'elseif_clauses_1 : elseif_clause_1'

def p_elseif_clauses_1_multiple(t):
    'elseif_clauses_1 : elseif_clauses_1 elseif_clause_1'

def p_elseif_clause_1(t):
    'elseif_clause_1 : ELSEIF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS statement'

def p_else_clause_1(t):
    'else_clause_1 : ELSE statement'

#13

def p_elseif_clauses_2_single(t):
    'elseif_clauses_2 : elseif_clause_2'

def p_elseif_clauses_2_multiple(t):
    'elseif_clauses_2 : elseif_clauses_2 elseif_clause_2'

def p_elseif_clause_2(t):
    'elseif_clause_2 : ELSEIF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT statement_list'

def p_else_clause_2(t):
    'else_clause_2 : ELSE DOUBLE_POINT statement_list'

def p_switch_statement_1(t):
    '''switch_statement : SWITCH LEFT_PARENTHESIS expression RIGHT_PARENTHESIS LEFT_CBRAC case_statements RIGHT_CBRAC
                            | SWITCH LEFT_PARENTHESIS expression RIGHT_PARENTHESIS LEFT_CBRAC RIGHT_CBRAC'''

def p_switch_statement_2(t):
    '''switch_statement : SWITCH LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT case_statements ENDSWITCH SEMICOLON
                            | SWITCH LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT ENDSWITCH SEMICOLON'''

#14

def p_case_statements_1(t):
    '''case_statements : case_statement case_statements
                        | case_statement'''

def p_case_statements_2(t):
    '''case_statements : default_statement case_statements
                        | default_statement'''

def p_case_statement(t):
    '''case_statement : CASE expression case_default_label_terminator statement_list
                        | CASE expression case_default_label_terminator'''

def p_default_statement(t):
    '''default_statement : DEFAULT case_default_label_terminator statement_list
                        | DEFAULT case_default_label_terminator'''

def p_case_default_label_terminator_colon(t):
    'case_default_label_terminator : DOUBLE_POINT'

def p_case_default_label_terminator_semicolon(t):
    'case_default_label_terminator : SEMICOLON'

#15

def p_iteration_statement_while(t):
    'iteration_statement : while_statement'

def p_iteration_statement_do(t):
    'iteration_statement : do_statement'

def p_iteration_statement_for(t):
    'iteration_statement : for_statement'

def p_iteration_statement_foreach(t):
    'iteration_statement : foreach_statement'

def p_while_statement(t):
    'while_statement : WHILE LEFT_PARENTHESIS expression RIGHT_PARENTHESIS statement'

def p_while_statement_block(t):
    'while_statement : WHILE LEFT_PARENTHESIS expression RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDWHILE SEMICOLON'

def p_do_statement(t):
    'do_statement : DO statement WHILE LEFT_PARENTHESIS expression RIGHT_PARENTHESIS SEMICOLON'

#16

def p_for_statement(t):
    '''for_statement : FOR LEFT_PARENTHESIS for_initializer SEMICOLON for_control SEMICOLON for_end_of_loop RIGHT_PARENTHESIS statement
                        | FOR LEFT_PARENTHESIS for_initializer SEMICOLON for_control SEMICOLON RIGHT_PARENTHESIS statement
                        | FOR LEFT_PARENTHESIS for_initializer SEMICOLON SEMICOLON for_end_of_loop RIGHT_PARENTHESIS statement
                        | FOR LEFT_PARENTHESIS for_initializer SEMICOLON SEMICOLON RIGHT_PARENTHESIS statement
                        | FOR LEFT_PARENTHESIS SEMICOLON for_control SEMICOLON for_end_of_loop RIGHT_PARENTHESIS statement
                        | FOR LEFT_PARENTHESIS SEMICOLON for_control SEMICOLON RIGHT_PARENTHESIS statement
                        | FOR LEFT_PARENTHESIS SEMICOLON SEMICOLON for_end_of_loop RIGHT_PARENTHESIS statement
                        | FOR LEFT_PARENTHESIS SEMICOLON SEMICOLON RIGHT_PARENTHESIS statement'''

def p_for_statement_block(t):
    '''for_statement : FOR LEFT_PARENTHESIS for_initializer SEMICOLON for_control SEMICOLON for_end_of_loop RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDFOR SEMICOLON
                        | FOR LEFT_PARENTHESIS for_initializer SEMICOLON for_control SEMICOLON RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDFOR SEMICOLON
                        | FOR LEFT_PARENTHESIS for_initializer SEMICOLON SEMICOLON for_end_of_loop RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDFOR SEMICOLON
                        | FOR LEFT_PARENTHESIS for_initializer SEMICOLON SEMICOLON RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDFOR SEMICOLON
                        | FOR LEFT_PARENTHESIS SEMICOLON for_control SEMICOLON for_end_of_loop RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDFOR SEMICOLON
                        | FOR LEFT_PARENTHESIS SEMICOLON for_control SEMICOLON RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDFOR SEMICOLON
                        | FOR LEFT_PARENTHESIS SEMICOLON SEMICOLON for_end_of_loop RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDFOR SEMICOLON
                        | FOR LEFT_PARENTHESIS SEMICOLON SEMICOLON RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDFOR SEMICOLON'''

def p_for_initializer(t):
    'for_initializer : for_expression_group'

def p_for_control(t):
    'for_control : for_expression_group'

def p_for_end_of_loop(t):
    'for_end_of_loop : for_expression_group'

def p_for_expression_group_single(t):
    'for_expression_group : expression'

def p_for_expression_group_multiple(t):
    'for_expression_group : for_expression_group COLON expression'

#17

def p_foreach_statement(t):
    '''foreach_statement : FOREACH LEFT_PARENTHESIS foreach_collection_name AS foreach_key foreach_value RIGHT_PARENTHESIS statement
                            | FOREACH LEFT_PARENTHESIS foreach_collection_name AS foreach_value RIGHT_PARENTHESIS statement'''

def p_foreach_statement_block(t):
    '''foreach_statement : FOREACH LEFT_PARENTHESIS foreach_collection_name AS foreach_key foreach_value RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDFOREACH SEMICOLON
                            | FOREACH LEFT_PARENTHESIS foreach_collection_name AS foreach_value RIGHT_PARENTHESIS DOUBLE_POINT statement_list ENDFOREACH SEMICOLON'''

def p_foreach_collection_name(t):
    'foreach_collection_name : expression'

def p_foreach_key(t):
    'foreach_key : expression DOUBLE_ARROW'

def p_foreach_value(t):
    'foreach_value : AMPERSAND_opt expression'

def p_foreach_value_amp_expression(t):
    'foreach_value : AMPERSAND expression'

def p_foreach_value_list_intrinsic(t):
    'foreach_value : list_intrinsic'

#18

def p_jump_statement_goto(t):
    'jump_statement : goto_statement'

def p_jump_statement_continue(t):
    'jump_statement : continue_statement'

def p_jump_statement_break(t):
    'jump_statement : break_statement'

def p_jump_statement_return(t):
    'jump_statement : return_statement'

def p_jump_statement_throw(t):
    'jump_statement : throw_statement'

def p_goto_statement(t):
    'goto_statement : GOTO name SEMICOLON'

def p_continue_statement(t):
    '''continue_statement : CONTINUE breakout_level SEMICOLON
                        | CONTINUE SEMICOLON'''

def p_breakout_level(t):
    'breakout_level : INTEGER_LITERAL'

def p_breakout_level_expression(t):
    'breakout_level : LEFT_PARENTHESIS breakout_level RIGHT_PARENTHESIS'

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

#ojo correcccion
def p_catch_name_list(p): #! ojo aca con el | del centro
    '''catch_name_list : qualified_name
                       | catch_name_list'''

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
                       | expression_list  expression'''

def p_unset_statement(p):
    '''unset_statement : UNSET LEFT_PARENTHESIS variable_list COLON RIGHT_PARENTHESIS SEMICOLON
                        | UNSET LEFT_PARENTHESIS variable_list RIGHT_PARENTHESIS SEMICOLON'''

def p_function_definition(p):
    '''function_definition : function_definition_header compound_statement'''

def p_function_definition_header(p):
    '''function_definition_header : FUNCTION ampersandopt name LEFT_PARENTHESIS parameter_declaration_listopt RIGHT_PARENTHESIS return_type_opt'''

def p_ampersandopt(p): #opcionales
    '''ampersandopt : AMPERSAND
                    |'''

def p_parameter_declaration_list(p):
    '''parameter_declaration_list : simple_parameter_declaration_list
                                   | variadic_declaration_list'''

def p_simple_parameter_declaration_list(p):
    '''simple_parameter_declaration_list : parameter_declaration
                                          | parameter_declaration_list  parameter_declaration'''

def p_variadic_declaration_list(p):
    '''variadic_declaration_list : simple_parameter_declaration_list  variadic_parameter
                                  | variadic_parameter'''
#_____________________________________________________________
def p_parameter_declaration(p):
    '''parameter_declaration : type_declarationopt ampersandopt VARIABLE default_argument_specifieropt'''

def p_variadic_parameter(p):
    '''variadic_parameter : type_declarationopt ampersandopt ELLIPSIS VARIABLE'''

def p_return_type(p):
    '''return_type : DOUBLE_POINT type_declaration
                   | DOUBLE_POINT VOID'''
#____________________________________________________________
def p_type_declarationopt(p): #opcionales
    '''type_declarationopt : type_declaration
                           |'''

def p_type_declaration(p):
    '''type_declaration : TERNARY_OPERATIONopt base_type_declaration'''

def p_TERNARY_OPERATIONopt(p): #opcionales
    '''TERNARY_OPERATIONopt : TERNARY_OPERATION
                        |'''

def p_base_type_declaration(p):
    '''base_type_declaration : ARRAY
                             | CALLABLE
                             | ITERABLE
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
#_____________________________________________________________
#estas no tiene opt
def p_class_modifier(p):
    '''class_modifier : ABSTRACT
                       | FINAL'''

def p_class_base_clause(p):
    '''class_base_clause : EXTENDS qualified_name'''

def p_class_interface_clause(p):
    '''class_interface_clause : IMPLEMENTS qualified_name
                               | class_interface_clause  qualified_name'''

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
#_____________________________________________________________
def p_class_const_declaration(p):
    '''class_const_declaration : visibility_modifier_opt CONST const_elements SEMICOLON'''

# def p_visibility_modifieropt(p): #opcionales
#     '''visibility_modifier_opt : visibility_modifier
#                                 |'''

def p_const_elements(p):
    '''const_elements : const_element
                      | const_elements  const_element'''

def p_const_element(p):
    '''const_element : name EQUAL constant_expression'''

def p_property_declaration(p):
    '''property_declaration : property_modifier property_elements SEMICOLON'''

def p_property_modifier(p):
    '''property_modifier : VAR
                          | visibility_modifier static_modifieropt
                          | static_modifier visibility_modifier_opt'''
    
def p_static_modifieropt(p): #opcionales
    '''static_modifieropt : static_modifier
                            |'''

# def p_visibility_modifieropt_1(p): #opcionales
#     '''visibility_modifier_opt : visibility_modifier
#                                 |'''

def p_visibility_modifier(p):
    '''visibility_modifier : PUBLIC
                            | PROTECTED
                            | PRIVATE'''

def p_static_modifier(p):
    '''static_modifier : STATIC'''
#_____________________________________________________________
def p_property_elements(p):
    '''property_elements : property_element
                          | property_elements property_element'''

def p_property_element(p):
    '''property_element : VARIABLE property_initializeropt SEMICOLON'''

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
    '''constructor_declaration : method_modifiers FUNCTION name AMPERSAND_opt CONSTRUCT LEFT_PARENTHESIS parameter_declaration_listopt RIGHT_PARENTHESIS compound_statement'''

def p_destructor_declaration(p):
    '''destructor_declaration : method_modifiers FUNCTION name AMPERSAND_opt DESTRUCT LEFT_PARENTHESIS RIGHT_PARENTHESIS compound_statement'''

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
                             | interface_base_clause  qualified_name'''

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
#_____________________________________________________________
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
                       | trait_name_list  qualified_name'''

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
#_____________________________________________________________
def p_trait_alias_as_clause(p):
    '''trait_alias_as_clause : name AS visibility_modifier_opt name
                              | name AS visibility_modifier nameopt'''

def p_visibility_modifieropt(p): #opcionales
    '''visibility_modifier_opt : visibility_modifier
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
                              | namespace_use_clauses  namespace_use_clause'''

def p_namespace_use_clause(p):
    '''namespace_use_clause : qualified_name namespace_aliasing_clause_opt'''

def p_namespace_aliasing_clause_opt(p):
    '''namespace_aliasing_clause_opt : namespace_aliasing_clause'''

def p_qualified_name(p):
    '''qualified_name : name'''

def p_namespace_aliasing_clause(p):
    '''namespace_aliasing_clause : AS name'''

def p_namespace_function_or_const(p):
    '''namespace_function_or_const : FUNCTION
                                    | CONST'''

def p_namespace_use_group_clauses_1(p):
    '''namespace_use_group_clauses_1 : namespace_use_group_clause_1
                                      | namespace_use_group_clauses_1  namespace_use_group_clause_1'''

def p_namespace_use_group_clause_1(p):
    '''namespace_use_group_clause_1 : namespace_name namespace_aliasing_clause_opt'''


def p_namespace_use_group_clauses_2(p):
    '''namespace_use_group_clauses_2 : namespace_use_group_clause_2
                                      | namespace_use_group_clauses_2  namespace_use_group_clause_2'''

def p_namespace_use_group_clause_2(p):
    '''namespace_use_group_clause_2 : namespace_function_or_constopt namespace_name namespace_aliasing_clause_opt'''

def p_name(p):
    '''name : STRING'''

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