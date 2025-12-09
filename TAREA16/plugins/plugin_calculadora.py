"""
Plugin de Calculadora: Realiza operaciones matemáticas básicas
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interfaz_plugin import InterfazPlugin


class PluginCalculadora(InterfazPlugin):
    """
    Plugin que evalúa expresiones matemáticas simples.
    """
    
    def obtener_nombre(self) -> str:
        return "Plugin Calculadora"
    
    def obtener_descripcion(self) -> str:
        return "Evalúa expresiones matemáticas básicas (suma, resta, multiplicación, división)"
    
    def ejecutar(self, dato: str) -> str:
        """
        Evalúa una expresión matemática.
        
        Args:
            dato (str): Expresión matemática (ej: "5 + 3", "10 * 2")
            
        Returns:
            str: Resultado de la operación
        """
        try:
            # Validar que solo contenga números y operadores permitidos
            caracteres_permitidos = "0123456789+-*/(). "
            if not all(c in caracteres_permitidos for c in dato):
                return "Error: Solo se permiten números y operadores (+, -, *, /, paréntesis)"
            
            resultado = eval(dato)
            return f"Resultado de '{dato}' = {resultado}"
        except ZeroDivisionError:
            return "Error: División por cero no permitida"
        except Exception as e:
            return f"Error al evaluar la expresión: {str(e)}"


# Instancia del plugin
plugin = PluginCalculadora()
