"""
Plugin de Saludo: Convierte texto a mayúsculas
Ejemplo básico de plugin que implementa la interfaz
"""
import sys
import os

# Agregar el directorio padre al path para importar la interfaz
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interfaz_plugin import InterfazPlugin


class PluginSaludo(InterfazPlugin):
    """
    Plugin que convierte texto a mayúsculas y agrega un saludo.
    """
    
    def obtener_nombre(self) -> str:
        return "Plugin Saludo"
    
    def obtener_descripcion(self) -> str:
        return "Convierte el texto a MAYÚSCULAS y agrega un saludo personalizado"
    
    def ejecutar(self, dato: str) -> str:
        """
        Convierte el texto a mayúsculas y agrega un saludo.
        
        Args:
            dato (str): Texto a transformar
            
        Returns:
            str: Texto transformado con saludo
        """
        if not dato:
            return "¡Hola! No proporcionaste ningún texto."
        
        texto_mayusculas = dato.upper()
        return f"¡HOLA! Tu mensaje en mayúsculas es: {texto_mayusculas}"


# Instancia del plugin que será cargada dinámicamente
plugin = PluginSaludo()
