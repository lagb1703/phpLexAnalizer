# Construcción de la gramática
def p_break_statement(p):
    '''break_statement : BREAK breakout_levelopt SEMICOLON'''

def p_breakout_levelopt(p):
    '''breakout_levelopt : breakout_level
                         |'''

def p_breakout_level(p):
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
                       | catch_name_list | qualified_name'''

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

def p_visibility_modifieropt(p): #opcionales
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

def p_visibility_modifieropt(p): #opcionales
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

def p_namespace_aliasing_clauseopt(p): #opcionales
    '''namespace_aliasing_clauseopt : namespace_aliasing_clause
                                    |'''

