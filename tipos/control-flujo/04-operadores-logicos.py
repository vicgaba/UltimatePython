# and, or, not
""" and -> Devuelve True si ambos operandos son True
    or -> Devuelve True si al menos uno de los operandos es True (el otro puede ser incluso desconocido), y False si ambos son False
    not -> Devuelve True si el operando es False
"""
gas = False
encendido = True
edad = 18

if not gas and encendido and edad >= 18:
    print("El motor está en marcha")

# operaciones de cortocircuito
# En una operación and, si el primer operando es False, no se evalúa el segundo operando
# En una operación or, si el primer operando es True, no se evalúa el segundo operando
# Esto es útil cuando el segundo operando es una operación costosa o tiene efectos secundarios  indeseados
# Siempre se evalúal de izquierda a derecha
