# Extrra Functions for solicitudes applications
import random
import string

# Función que genera un código pseudoaleatorio que contiene letras y números en mayúsculas
def code_generator( size = 8, chars = string.ascii_uppercase + string.digits):
    return ''.join( random.choice(chars) for _ in range(size) )
