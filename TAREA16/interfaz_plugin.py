"""
Interfaz base para el patrón Plug-in
Define el contrato que todos los plugins deben cumplir
"""
from abc import ABC, abstractmethod


class InterfazPlugin(ABC):
    """
    Clase abstracta que define la interfaz común para todos los plugins.
    Todos los plugins deben heredar de esta clase e implementar sus métodos.
    """
    
    @abstractmethod
    def obtener_nombre(self) -> str:
        """
        Retorna el nombre del plugin.
        
        Returns:
            str: Nombre descriptivo del plugin
        """
        pass
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción breve de lo que hace el plugin.
        
        Returns:
            str: Descripción del plugin
        """
        pass
    
    @abstractmethod
    def ejecutar(self, dato: str) -> str:
        """
        Método principal que ejecuta la funcionalidad del plugin.
        
        Args:
            dato (str): Dato de entrada para procesar
            
        Returns:
            str: Resultado del procesamiento
        """
        pass
