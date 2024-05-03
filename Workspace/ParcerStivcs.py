import ply.yacc as yacc

# Definición de tokens (asumidos ya definidos por el lexer)
tokens = (
    'BREAK', 'RETURN', 'THROW', 'TRY', 'CATCH', 'FINALLY',
    'ID', 'SEMICOLON', 'LPAREN', 'RPAREN', 'COMMA', 'VERTICAL',
)

# Construcción de la gramática
def p_break_statement(p):
    '''break_statement : BREAK breakout_level_opt SEMICOLON'''

def p_return_statement(p):
    '''return_statement : RETURN expression_opt SEMICOLON'''

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
    '''catch_clause : CATCH LPAREN catch_name_list VARIABLE RPAREN compound_statement'''

def p_catch_name_list(p):
    '''catch_name_list : qualified_name
                       | catch_name_list VERTICAL qualified_name'''

def p_finally_clause(p):
    '''finally_clause : FINALLY compound_statement'''

# Reglas de expresiones opcionales
def p_breakout_level_opt(p):
    '''breakout_level_opt : 
                          | breakout_level'''

def p_expression_opt(p):
    '''expression_opt : 
                      | expression'''

# Definiciones adicionales de reglas
def p_compound_statement(p):
    '''compound_statement : 
                          | ID'''

def p_qualified_name(p):
    '''qualified_name : ID'''

def p_expression(p):
    '''expression : ID'''

# Manejo de errores de sintaxis
def p_error(p):
    if p:
        print("Error de sintaxis en '%s'" % p.value)
    else:
        print("Error de sintaxis al final de la entrada")

# Construcción del parser
parser = yacc.yacc()

# Ejemplo de uso
input_str = """
try compound-statement catch ( qualified-name variable-name ) compound-statement finally compound-statement
"""
result = parser.parse(input_str)
print(result)
