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

parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
