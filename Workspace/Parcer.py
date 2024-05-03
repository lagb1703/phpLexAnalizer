import ply.yacc as yacc
from AnalixadorLex import tokens
import AnalixadorLex
import sys

VERBOSE = 1

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
#     '''delimited-comment : DIVIDE '*' '*' DIVIDE'''

# def p_delimited_comment_sequence(t):
#     '''delimited-comment : DIVIDE '*' STRING '*' DIVIDE'''

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

# def p_namespace_name_one(t):
#     'namespace-name : name'

# def p_namespace_name_two(t):
#     'namespace-name : namespace-name NS_SEPARATOR name'

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
    'conditional-expression : conditional-expression TERNARY_OPERATION expressionopt DOUBLE_POINT coalesce-expression'

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
    'list-expression-list : keyed-list-expression-list (COLON)?'

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
    'compound-statement : LEFT_CBRAC statement-listopt RIGHT_CBRAC'

def p_statement_list_single(t):
    'statement-list : statement'

def p_statement_list_multiple(t):
    'statement-list : statement-list statement'

def p_named_label_statement(t):
    'named-label-statement : name DOUBLE_POINT'

def p_expression_statement(t):
    'expression-statement : expressionopt SEMICOLON'

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
    'for-expression-group : for-expression-group COMMA expression'



parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
