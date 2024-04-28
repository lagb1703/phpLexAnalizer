import ply.yacc as yacc
from AnalixadorLex import tokens
import AnalixadorLex
import sys

VERBOSE = 1

def p_start(p):
    'start: top_statement_list'

def top_statement_list_ex(p):
    'top_statement_list_ex: top_statement_list_ex top_statement'

def p_top_statement_list(p):
    'top_statement_list: top_statement_list_ex'

def p_ampersand(p):
    'ampersand: AMPERSAND'

def p_ampersand_variable(p):
    'ampersand: ampersand VARIABLE'

def p_reserved_non_modifiers_INCLUDE(p):
    'reserved_non_modifiers: INCLUDE'

def p_reserved_non_modifiers_INCLUDE_ONCE(p):
    'reserved_non_modifiers: INCLUDE_ONCE'

def p_reserved_non_modifiers_EVAL(p):
    'reserved_non_modifiers: EVAL'

def p_reserved_non_modifiers_REQUIRE(p):
    'reserved_non_modifiers: REQUIRE'

def p_reserved_non_modifiers_REQUIRE_ONCE(p):
    'reserved_non_modifiers: REQUIRE_ONCE'

def p_reserved_non_modifiers_LOGICAL_OR(p):
    'reserved_non_modifiers: LOGICAL_OR'

def p_reserved_non_modifiers_LOGICAL_XOR(p):
    'reserved_non_modifiers: LOGICAL_XOR'

def p_reserved_non_modifiers_LOGICAL_AND(p):
    'reserved_non_modifiers: LOGICAL_AND'

def p_reserved_non_modifiers_INSTANCEOF(p):
    'reserved_non_modifiers: INSTANCEOF'

def p_reserved_non_modifiers_NEW(p):
    'reserved_non_modifiers: NEW'

def p_reserved_non_modifiers_CLONE(p):
    'reserved_non_modifiers: CLONE'

def p_reserved_non_modifiers_EXIT(p):
    'reserved_non_modifiers: EXIT'

def p_reserved_non_modifiers_IF(p):
    'reserved_non_modifiers: IF'

def p_reserved_non_modifiers_ELSEIF(p):
    'reserved_non_modifiers: ELSEIF'

def p_reserved_non_modifiers_ELSE(p):
    'reserved_non_modifiers: ELSE'

def p_reserved_non_modifiers_ENDIF(p):
    'reserved_non_modifiers: ENDIF'

def p_reserved_non_modifiers_DO(p):
    'reserved_non_modifiers: DO'

def p_reserved_non_modifiers_WHILE(p):
    'reserved_non_modifiers: WHILE'

def p_reserved_non_modifiers_ENDWHILE(p):
    'reserved_non_modifiers: ENDWHILE'

def p_reserved_non_modifiers_FOR(p):
    'reserved_non_modifiers: FOR'

def p_reserved_non_modifiers_ENDFOR(p):
    'reserved_non_modifiers: ENDFOR'

def p_reserved_non_modifiers_FOREACH(p):
    'reserved_non_modifiers: FOREACH'

def p_reserved_non_modifiers_ENDFOREACH(p):
    'reserved_non_modifiers: ENDFOREACH'

def p_reserved_non_modifiers_DECLARE(p):
    'reserved_non_modifiers: DECLARE'

def p_reserved_non_modifiers_ENDDECLARE(p):
    'reserved_non_modifiers: ENDDECLARE'

def p_reserved_non_modifiers_AS(p):
    'reserved_non_modifiers: AS'

def p_reserved_non_modifiers_TRY(p):
    'reserved_non_modifiers: TRY'

def p_reserved_non_modifiers_CATCH(p):
    'reserved_non_modifiers: CATCH'

def p_reserved_non_modifiers_FINALLY(p):
    'reserved_non_modifiers: FINALLY'

def p_reserved_non_modifiers_THROW(p):
    'reserved_non_modifiers : THROW'

def p_reserved_non_modifiers_USE(p):
    'reserved_non_modifiers : USE'

def p_reserved_non_modifiers_INSTEADOF(p):
    'reserved_non_modifiers : INSTEADOF'

def p_reserved_non_modifiers_GLOBAL(p):
    'reserved_non_modifiers : GLOBAL'

def p_reserved_non_modifiers_VAR(p):
    'reserved_non_modifiers : VAR'

def p_reserved_non_modifiers_UNSET(p):
    'reserved_non_modifiers : UNSET'

def p_reserved_non_modifiers_ISSET(p):
    'reserved_non_modifiers : ISSET'

def p_reserved_non_modifiers_EMPTY(p):
    'reserved_non_modifiers : EMPTY'

def p_reserved_non_modifiers_CONTINUE(p):
    'reserved_non_modifiers : CONTINUE'

def p_reserved_non_modifiers_GOTO(p):
    'reserved_non_modifiers : GOTO'

def p_reserved_non_modifiers_FUNCTION(p):
    'reserved_non_modifiers : FUNCTION'

def p_reserved_non_modifiers_CONST(p):
    'reserved_non_modifiers : CONST'

def p_reserved_non_modifiers_RETURN(p):
    'reserved_non_modifiers : RETURN'

def p_reserved_non_modifiers_PRINT(p):
    'reserved_non_modifiers : PRINT'

def p_reserved_non_modifiers_YIELD(p):
    'reserved_non_modifiers : YIELD'

def p_reserved_non_modifiers_LIST(p):
    'reserved_non_modifiers : LIST'

def p_reserved_non_modifiers_SWITCH(p):
    'reserved_non_modifiers : SWITCH'

def p_reserved_non_modifiers_ENDSWITCH(p):
    'reserved_non_modifiers : ENDSWITCH'

def p_reserved_non_modifiers_CASE(p):
    'reserved_non_modifiers : CASE'

def p_reserved_non_modifiers_DEFAULT(p):
    'reserved_non_modifiers : DEFAULT'

def p_reserved_non_modifiers_BREAK(p):
    'reserved_non_modifiers : BREAK'

def p_reserved_non_modifiers_ARRAY(p):
    'reserved_non_modifiers : ARRAY'

def p_reserved_non_modifiers_CALLABLE(p):
    'reserved_non_modifiers : CALLABLE'

def p_reserved_non_modifiers_EXTENDS(p):
    'reserved_non_modifiers : EXTENDS'

def p_reserved_non_modifiers_IMPLEMENTS(p):
    'reserved_non_modifiers : IMPLEMENTS'

def p_reserved_non_modifiers_NAMESPACE(p):
    'reserved_non_modifiers : NAMESPACE'

def p_reserved_non_modifiers_TRAIT(p):
    'reserved_non_modifiers : TRAIT'

def p_reserved_non_modifiers_INTERFACE(p):
    'reserved_non_modifiers : INTERFACE'

def p_reserved_non_modifiers_CLASS(p):
    'reserved_non_modifiers : CLASS'

def p_reserved_non_modifiers_CLASS_C(p):
    'reserved_non_modifiers : CLASS_C'

def p_reserved_non_modifiers_TRAIC(p):
    'reserved_non_modifiers : TRAIC'

def p_reserved_non_modifiers_FUNC_C(p):
    'reserved_non_modifiers : FUNC_C'

def p_reserved_non_modifiers_METHOD_C(p):
    'reserved_non_modifiers : METHOD_C'

def p_reserved_non_modifiers_LINE(p):
    'reserved_non_modifiers : LINE'

def p_reserved_non_modifiers_FILE(p):
    'reserved_non_modifiers : FILE'

def p_reserved_non_modifiers_DIR(p):
    'reserved_non_modifiers : DIR'

def p_reserved_non_modifiers_NS_C(p):
    'reserved_non_modifiers : NS_C'

def p_reserved_non_modifiers_FN(p):
    'reserved_non_modifiers : FN'

def p_reserved_non_modifiers_MATCH(p):
    'reserved_non_modifiers : MATCH'

def p_reserved_non_modifiers_ENUM(p):
    'reserved_non_modifiers : ENUM'

def p_reserved_non_modifiers_ECHO(p):
    'reserved_non_modifiers : ECHO'

def p_semi_reserved_reserved_non_modifiers(p):
    'p_semi_reserved: reserved_non_modifiers'

def p_semi_reserved_STATIC(p):
    'p_semi_reserved: STATIC'

def p_semi_reserved_ABSTRACT(p):
    'p_semi_reserved: ABSTRACT'

def p_semi_reserved_FINAL(p):
    'p_semi_reserved: FINAL'

def p_semi_reserved_PRIVATE(p):
    'p_semi_reserved: PRIVATE'

def p_semi_reserved_PROTECTED(p):
    'p_semi_reserved: PROTECTED'

def p_semi_reserved_PUBLIC(p):
    'p_semi_reserved: PUBLIC'

def p_semi_reserved_READONLY(p):
    'p_semi_reserved: READONLY'

def p_identifier_maybe_reserved_STRING(p):
    'identifier_maybe_reserved: STRING'

def p_identifier_maybe_reserved_semi_reserved(p):
    'identifier_maybe_reserved: semi_reserved'

def p_identifier_not_reserved_STRING(p):
    'identifier_maybe_reserved: STRING'

def p_reserved_non_modifiers_identifier_reserved_non_modifiers(p):
    'reserved_non_modifiers_identifier: reserved_non_modifiers'

def p_namespace_declaration_name_STRING(p):
    'namespace_declaration_name : STRING'

def p_namespace_declaration_name_semi_reserved(p):
    'namespace_declaration_name : semi_reserved'

def p_namespace_declaration_STRING(p):
    'namespace_declaration_name : STRING'

#187