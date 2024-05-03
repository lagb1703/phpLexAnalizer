import ply.yacc as yacc
from AnalixadorLex import tokens
import AnalixadorLex
import sys

VERBOSE = 1

def p_input_file_one(t):
    'input_file : input_element'

def p_input_file_two(t):
    'input_file : input_file input_element'

def p_input_element_comment(t):
    'input_element : comment'

def p_input_element_whitespace(t):
    'input_element : white_space'

def p_input_element_token(t):
    'input_element : token'

def p_comment_single_line_comment(t):
    'comment : single_line_comment'

def p_comment_delimited_comment(t):
    'comment : delimited_comment'

def p_single_line_comment_one(t):
    'single-line-comment : DIVIDE DIVIDE input-charactersopt'

def p_single_line_comment_two(t):
    '''single-line-comment : '#' (input-characters)?'''

def p_input_characters_one(t):
    'input-characters : input-character'

def p_input_characters_two(t):
    'input-characters : input-characters input-character'

def p_input_character(t):
    'input-character : STRING new-line'

def p_new_line_CR(t):
    '''new-line : '\r''''

def p_new_line_LF(t):
    ''''new-line : '\n'''''

def p_new_line_CR_LF(t):
    '''new-line : '\r' '\n''''

def p_delimited_comment_empty(t):
    '''delimited-comment : DIVIDE '*' '*' DIVIDE'''

def p_delimited_comment_sequence(t):
    '''delimited-comment : DIVIDE '*' STRING '*' DIVIDE'''

def p_white_space_one(t):
    'white-space : white-space-character'

def p_white_space_two(t):
    'white-space : white-space white-space-character'



def p_white_space_character_new_line(t):
    'white-space-character : WHITESPACE'

def p_token_variable_name(t):
    'token : variable-name'

def p_token_name(t):
    'token : name'

def p_token_keyword(t):
    'token : keyword'

def p_token_integer_literal(t):
    'token : integer-literal'

def p_token_floating_literal(t):
    'token : floating-literal'

def p_token_string_literal(t):
    'token : string-literal'

def p_token_operator_or_punctuator(t):
    'token : operator-or-punctuator'

def p_variable_name(t):
    'variable-name : VARIABLE'

#5

def p_namespace_name_one(t):
    'namespace-name : name'

def p_namespace_name_two(t):
    'namespace-name : namespace-name NS_SEPARATOR name'

def p_namespace_name_as_a_prefix_backslash(t):
    'namespace-name-as-a-prefix : NS_SEPARATOR '

def p_namespace_name_as_a_prefix_backslash_opt(t):
    'namespace-name-as-a-prefix : (NS_SEPARATOR)? namespace-name NS_SEPARATOR '

def p_namespace_name_as_a_prefix_namespace(t):
    'namespace-name-as-a-prefix : NAMESPACE NS_SEPARATOR '

def p_namespace_name_as_a_prefix_namespace_backslash(t):
    'namespace-name-as-a-prefix : NAMESPACE NS_SEPARATOR namespace-name NS_SEPARATOR '

def p_qualified_name_namespace_name_as_a_prefix_opt(t):
    'qualified-name : (namespace-name-as-a-prefix)? name'


#6

def p_name_one(t):
    'name : name-nondigit'

def p_name_two(t):
    'name : name name-nondigit'

def p_name_three(t):
    'name : name digit'

def p_name_nondigit(t):
    'name-nondigit : nondigit'

def p_name_nondigit_extended(t):
    '''name-nondigit : '[\x80-\xff]''''

def p_nondigit(t):
    ''''[a-zA-Z0-9_\x7f-\xff^\$]''''

#7

def p_keyword_abstract(t):
    'keyword : ABSTRACT'

def p_keyword_and(t):
    'keyword : AND'

def p_keyword_array(t):
    'keyword : ARRAY'

def p_keyword_as(t):
    'keyword : AS'

def p_keyword_break(t):
    'keyword : BREAK'

def p_keyword_callable(t):
    'keyword : CALLABLE'

def p_keyword_case(t):
    'keyword : CASE'

def p_keyword_catch(t):
    'keyword : CATCH'

def p_keyword_class(t):
    'keyword : CLASS'

def p_keyword_clone(t):
    'keyword : CLONE'

def p_keyword_const(t):
    'keyword : CONST'

def p_keyword_continue(t):
    'keyword : CONTINUE'

def p_keyword_declare(t):
    'keyword : DECLARE'

def p_keyword_default(t):
    'keyword : DEFAULT'

def p_keyword_die(t):
    'keyword : DIE'

def p_keyword_do(t):
    'keyword : DO'

def p_keyword_echo(t):
    'keyword : ECHO'

def p_keyword_else(t):
    'keyword : ELSE'

def p_keyword_elseif(t):
    'keyword : ELSEIF'

def p_keyword_empty(t):
    'keyword : EMPTY'

def p_keyword_enddeclare(t):
    'keyword : ENDDECLARE'

def p_keyword_endfor(t):
    'keyword : ENDFOR'

def p_keyword_endforeach(t):
    'keyword : ENDFOREACH'

def p_keyword_endif(t):
    'keyword : ENDIF'

def p_keyword_endswitch(t):
    'keyword : ENDSWITCH'

def p_keyword_endwhile(t):
    'keyword : ENDWHILE'

def p_keyword_eval(t):
    'keyword : EVAL'

def p_keyword_exit(t):
    'keyword : EXIT'

def p_keyword_extends(t):
    'keyword : EXTENDS'

def p_keyword_final(t):
    'keyword : FINAL'

def p_keyword_finally(t):
    'keyword : FINALLY'

def p_keyword_for(t):
    'keyword : FOR'

def p_keyword_foreach(t):
    'keyword : FOREACH'

def p_keyword_function(t):
    'keyword : FUNCTION'

def p_keyword_global(t):
    'keyword : GLOBAL'

def p_keyword_goto(t):
    'keyword : GOTO'

def p_keyword_if(t):
    'keyword : IF'

def p_keyword_implements(t):
    'keyword : IMPLEMENTS'

def p_keyword_include(t):
    'keyword : INCLUDE'

def p_keyword_include_once(t):
    'keyword : INCLUDE_ONCE'

def p_keyword_instanceof(t):
    'keyword : INSTANCEOF'

def p_keyword_insteadof(t):
    'keyword : INSTEADOF'

def p_keyword_interface(t):
    'keyword : INTERFACE'

def p_keyword_isset(t):
    'keyword : ISSET'

def p_keyword_list(t):
    'keyword : LIST'

def p_keyword_namespace(t):
    'keyword : NAMESPACE'

def p_keyword_new(t):
    'keyword : NEW'

def p_keyword_or(t):
    'keyword : OR'

def p_keyword_print(t):
    'keyword : PRINT'

def p_keyword_private(t):
    'keyword : PRIVATE'

def p_keyword_protected(t):
    'keyword : PROTECTED'

def p_keyword_public(t):
    'keyword : PUBLIC'

def p_keyword_require(t):
    'keyword : REQUIRE'

def p_keyword_require_once(t):
    'keyword : REQUIRE_ONCE'

def p_keyword_return(t):
    'keyword : RETURN'

def p_keyword_static(t):
    'keyword : STATIC'

def p_keyword_switch(t):
    'keyword : SWITCH'

def p_keyword_throw(t):
    'keyword : THROW'

def p_keyword_trait(t):
    'keyword : TRAIT'

def p_keyword_try(t):
    'keyword : TRY'

def p_keyword_unset(t):
    'keyword : UNSET'

def p_keyword_use(t):
    'keyword : USE'

def p_keyword_var(t):
    'keyword : VAR'

def p_keyword_while(t):
    'keyword : WHILE'

def p_keyword_xor(t):
    'keyword : XOR'

def p_keyword_yield(t):
    'keyword : YIELD'

def p_keyword_yield_from(t):
    'keyword : YIELD FROM'

#8

def p_integer_literal_decimal(t):
    'integer-literal : decimal-literal'

def p_integer_literal_octal(t):
    'integer-literal : octal-literal'

def p_integer_literal_hexadecimal(t):
    'integer-literal : hexadecimal-literal'

def p_integer_literal_binary(t):
    'integer-literal : binary-literal'

def p_decimal_literal_nonzero_digit(t):
    'decimal-literal : nonzero-digit'

def p_decimal_literal_multiple(t):
    'decimal-literal : decimal-literal digit'

def p_octal_literal_zero(t):
    '''octal-literal : '0''''

def p_octal_literal_multiple(t):
    'octal-literal : octal-literal octal-digit'

#9

def p_hexadecimal_literal_prefix_digit(t):
    'hexadecimal-literal : hexadecimal-prefix hexadecimal-digit'

def p_hexadecimal_literal_multiple(t):
    'hexadecimal-literal : hexadecimal-literal hexadecimal-digit'

#10

def p_hexadecimal_prefix(t):
    '''hexadecimal-prefix: '0(x|X)''''

#11

def p_binary_literal_prefix_digit(t):
    'binary-literal : binary-prefix binary-digit'

def p_binary_literal_multiple(t):
    'binary-literal : binary-literal binary-digit'

#12

def p_binary_prefix(t):
    '''hexadecimal-prefix: '0(b|B)''''

#13

def p_digit(t):
    ''''[0-9]''''

def p_nonzero_digit(t):
    ''''[1-9]''''

def p_octal_digit(t):
    ''''[0-7]''''

def p_hexadecimal_digit(t):
    ''''([0-9]|[a-f]|[A-F])''''

def p_hexadecimal_digit(t):
    ''''[0-1]''''

#14

def p_floating_literal_fractional(t):
    'floating-literal : fractional-literal (exponent-part)?'

def p_floating_literal_digit_sequence(t):
    'floating-literal : digit-sequence exponent-part'

def p_fractional_literal_sequence_dot_sequence(t):
    'fractional-literal : (digit-sequence)? CONCAT digit-sequence'

def p_fractional_literal_sequence_dot(t):
    'fractional-literal : digit-sequence CONCAT'

#15

def p_exponent_part_e(t):
    '''exponent-part : 'e' (sign)? digit-sequence'''

def p_exponent_part_E(t):
    '''exponent-part : 'E' (sign)? digit-sequence'''

#16

def p_sign(t):
    '''sign: '+|-''''

#17

def p_digit_sequence_single(t):
    'digit-sequence : digit'

def p_digit_sequence_multiple(t):
    'digit-sequence : digit-sequence digit'

def p_string_literal_single_quoted(t):
    'string-literal : single-quoted-string-literal'

def p_string_literal_double_quoted(t):
    'string-literal : double-quoted-string-literal'

def p_string_literal_heredoc(t):
    'string-literal : heredoc-string-literal'

def p_string_literal_nowdoc(t):
    'string-literal : nowdoc-string-literal'


parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

#trabajo hecho si acaso
# def p_start(p):
#     'start: top_statement_list'

# def top_statement_list_ex(p):
#     'top_statement_list_ex: top_statement_list_ex top_statement'

# def p_top_statement_list(p):
#     'top_statement_list: top_statement_list_ex'

# def p_ampersand(p):
#     'ampersand: AMPERSAND'

# def p_ampersand_variable(p):
#     'ampersand: ampersand VARIABLE'

# def p_reserved_non_modifiers_INCLUDE(p):
#     'reserved_non_modifiers: INCLUDE'

# def p_reserved_non_modifiers_INCLUDE_ONCE(p):
#     'reserved_non_modifiers: INCLUDE_ONCE'

# def p_reserved_non_modifiers_EVAL(p):
#     'reserved_non_modifiers: EVAL'

# def p_reserved_non_modifiers_REQUIRE(p):
#     'reserved_non_modifiers: REQUIRE'

# def p_reserved_non_modifiers_REQUIRE_ONCE(p):
#     'reserved_non_modifiers: REQUIRE_ONCE'

# def p_reserved_non_modifiers_LOGICAL_OR(p):
#     'reserved_non_modifiers: LOGICAL_OR'

# def p_reserved_non_modifiers_LOGICAL_XOR(p):
#     'reserved_non_modifiers: LOGICAL_XOR'

# def p_reserved_non_modifiers_LOGICAL_AND(p):
#     'reserved_non_modifiers: LOGICAL_AND'

# def p_reserved_non_modifiers_INSTANCEOF(p):
#     'reserved_non_modifiers: INSTANCEOF'

# def p_reserved_non_modifiers_NEW(p):
#     'reserved_non_modifiers: NEW'

# def p_reserved_non_modifiers_CLONE(p):
#     'reserved_non_modifiers: CLONE'

# def p_reserved_non_modifiers_EXIT(p):
#     'reserved_non_modifiers: EXIT'

# def p_reserved_non_modifiers_IF(p):
#     'reserved_non_modifiers: IF'

# def p_reserved_non_modifiers_ELSEIF(p):
#     'reserved_non_modifiers: ELSEIF'

# def p_reserved_non_modifiers_ELSE(p):
#     'reserved_non_modifiers: ELSE'

# def p_reserved_non_modifiers_ENDIF(p):
#     'reserved_non_modifiers: ENDIF'

# def p_reserved_non_modifiers_DO(p):
#     'reserved_non_modifiers: DO'

# def p_reserved_non_modifiers_WHILE(p):
#     'reserved_non_modifiers: WHILE'

# def p_reserved_non_modifiers_ENDWHILE(p):
#     'reserved_non_modifiers: ENDWHILE'

# def p_reserved_non_modifiers_FOR(p):
#     'reserved_non_modifiers: FOR'

# def p_reserved_non_modifiers_ENDFOR(p):
#     'reserved_non_modifiers: ENDFOR'

# def p_reserved_non_modifiers_FOREACH(p):
#     'reserved_non_modifiers: FOREACH'

# def p_reserved_non_modifiers_ENDFOREACH(p):
#     'reserved_non_modifiers: ENDFOREACH'

# def p_reserved_non_modifiers_DECLARE(p):
#     'reserved_non_modifiers: DECLARE'

# def p_reserved_non_modifiers_ENDDECLARE(p):
#     'reserved_non_modifiers: ENDDECLARE'

# def p_reserved_non_modifiers_AS(p):
#     'reserved_non_modifiers: AS'

# def p_reserved_non_modifiers_TRY(p):
#     'reserved_non_modifiers: TRY'

# def p_reserved_non_modifiers_CATCH(p):
#     'reserved_non_modifiers: CATCH'

# def p_reserved_non_modifiers_FINALLY(p):
#     'reserved_non_modifiers: FINALLY'

# def p_reserved_non_modifiers_THROW(p):
#     'reserved_non_modifiers : THROW'

# def p_reserved_non_modifiers_USE(p):
#     'reserved_non_modifiers : USE'

# def p_reserved_non_modifiers_INSTEADOF(p):
#     'reserved_non_modifiers : INSTEADOF'

# def p_reserved_non_modifiers_GLOBAL(p):
#     'reserved_non_modifiers : GLOBAL'

# def p_reserved_non_modifiers_VAR(p):
#     'reserved_non_modifiers : VAR'

# def p_reserved_non_modifiers_UNSET(p):
#     'reserved_non_modifiers : UNSET'

# def p_reserved_non_modifiers_ISSET(p):
#     'reserved_non_modifiers : ISSET'

# def p_reserved_non_modifiers_EMPTY(p):
#     'reserved_non_modifiers : EMPTY'

# def p_reserved_non_modifiers_CONTINUE(p):
#     'reserved_non_modifiers : CONTINUE'

# def p_reserved_non_modifiers_GOTO(p):
#     'reserved_non_modifiers : GOTO'

# def p_reserved_non_modifiers_FUNCTION(p):
#     'reserved_non_modifiers : FUNCTION'

# def p_reserved_non_modifiers_CONST(p):
#     'reserved_non_modifiers : CONST'

# def p_reserved_non_modifiers_RETURN(p):
#     'reserved_non_modifiers : RETURN'

# def p_reserved_non_modifiers_PRINT(p):
#     'reserved_non_modifiers : PRINT'

# def p_reserved_non_modifiers_YIELD(p):
#     'reserved_non_modifiers : YIELD'

# def p_reserved_non_modifiers_LIST(p):
#     'reserved_non_modifiers : LIST'

# def p_reserved_non_modifiers_SWITCH(p):
#     'reserved_non_modifiers : SWITCH'

# def p_reserved_non_modifiers_ENDSWITCH(p):
#     'reserved_non_modifiers : ENDSWITCH'

# def p_reserved_non_modifiers_CASE(p):
#     'reserved_non_modifiers : CASE'

# def p_reserved_non_modifiers_DEFAULT(p):
#     'reserved_non_modifiers : DEFAULT'

# def p_reserved_non_modifiers_BREAK(p):
#     'reserved_non_modifiers : BREAK'

# def p_reserved_non_modifiers_ARRAY(p):
#     'reserved_non_modifiers : ARRAY'

# def p_reserved_non_modifiers_CALLABLE(p):
#     'reserved_non_modifiers : CALLABLE'

# def p_reserved_non_modifiers_EXTENDS(p):
#     'reserved_non_modifiers : EXTENDS'

# def p_reserved_non_modifiers_IMPLEMENTS(p):
#     'reserved_non_modifiers : IMPLEMENTS'

# def p_reserved_non_modifiers_NAMESPACE(p):
#     'reserved_non_modifiers : NAMESPACE'

# def p_reserved_non_modifiers_TRAIT(p):
#     'reserved_non_modifiers : TRAIT'

# def p_reserved_non_modifiers_INTERFACE(p):
#     'reserved_non_modifiers : INTERFACE'

# def p_reserved_non_modifiers_CLASS(p):
#     'reserved_non_modifiers : CLASS'

# def p_reserved_non_modifiers_CLASS_C(p):
#     'reserved_non_modifiers : CLASS_C'

# def p_reserved_non_modifiers_TRAIC(p):
#     'reserved_non_modifiers : TRAIC'

# def p_reserved_non_modifiers_FUNC_C(p):
#     'reserved_non_modifiers : FUNC_C'

# def p_reserved_non_modifiers_METHOD_C(p):
#     'reserved_non_modifiers : METHOD_C'

# def p_reserved_non_modifiers_LINE(p):
#     'reserved_non_modifiers : LINE'

# def p_reserved_non_modifiers_FILE(p):
#     'reserved_non_modifiers : FILE'

# def p_reserved_non_modifiers_DIR(p):
#     'reserved_non_modifiers : DIR'

# def p_reserved_non_modifiers_NS_C(p):
#     'reserved_non_modifiers : NS_C'

# def p_reserved_non_modifiers_FN(p):
#     'reserved_non_modifiers : FN'

# def p_reserved_non_modifiers_MATCH(p):
#     'reserved_non_modifiers : MATCH'

# def p_reserved_non_modifiers_ENUM(p):
#     'reserved_non_modifiers : ENUM'

# def p_reserved_non_modifiers_ECHO(p):
#     'reserved_non_modifiers : ECHO'

# def p_semi_reserved_reserved_non_modifiers(p):
#     'p_semi_reserved: reserved_non_modifiers'

# def p_semi_reserved_STATIC(p):
#     'p_semi_reserved: STATIC'

# def p_semi_reserved_ABSTRACT(p):
#     'p_semi_reserved: ABSTRACT'

# def p_semi_reserved_FINAL(p):
#     'p_semi_reserved: FINAL'

# def p_semi_reserved_PRIVATE(p):
#     'p_semi_reserved: PRIVATE'

# def p_semi_reserved_PROTECTED(p):
#     'p_semi_reserved: PROTECTED'

# def p_semi_reserved_PUBLIC(p):
#     'p_semi_reserved: PUBLIC'

# def p_semi_reserved_READONLY(p):
#     'p_semi_reserved: READONLY'

# def p_identifier_maybe_reserved_STRING(p):
#     'identifier_maybe_reserved: STRING'

# def p_identifier_maybe_reserved_semi_reserved(p):
#     'identifier_maybe_reserved: semi_reserved'

# def p_identifier_not_reserved_STRING(p):
#     'identifier_maybe_reserved: STRING'

# def p_reserved_non_modifiers_identifier_reserved_non_modifiers(p):
#     'reserved_non_modifiers_identifier: reserved_non_modifiers'

# def p_namespace_declaration_name_STRING(p):
#     'namespace_declaration_name : STRING'

# def p_namespace_declaration_name_semi_reserved(p):
#     'namespace_declaration_name : semi_reserved'

# def p_namespace_declaration_STRING(p):
#     'namespace_declaration_name : STRING'

#187