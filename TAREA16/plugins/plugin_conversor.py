"""
Plugin de Conversor: Invierte el orden de un texto
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interfaz_plugin import InterfazPlugin


class PluginConversor(InterfazPlugin):
    """
    Plugin que invierte el orden de caracteres de un texto.
    """
    
    def obtener_nombre(self) -> str:
        return "Plugin Conversor"
    
    def obtener_descripcion(self) -> str:
        return "Invierte el orden de los caracteres de un texto"
    
    def ejecutar(self, dato: str) -> str:
        """
        Invierte el orden del texto.
        
        Args:
            dato (str): Texto a invertir
            
        Returns:
            str: Texto invertido
        """
        if not dato:
            return "No hay texto para invertir"
        
        texto_invertido = dato[::-1]
        
        # Información adicional
        num_caracteres = len(dato)
        num_palabras = len(dato.split())
        
        return f"Texto invertido: '{texto_invertido}'\nCaracteres: {num_caracteres} | Palabras: {num_palabras}"


# Instancia del plugin
plugin = PluginConversor()
