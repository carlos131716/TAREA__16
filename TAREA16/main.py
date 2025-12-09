"""
NÚCLEO (CORE) - Sistema de Carga Dinámica de Plugins
Implementación del patrón Microkernel/Plug-in
"""
import os
import sys
import importlib.util
from typing import List, Dict
from interfaz_plugin import InterfazPlugin


class NucleoPlugins:
    """
    Clase principal que gestiona la carga dinámica de plugins.
    Escanea la carpeta /plugins y carga módulos en tiempo de ejecución.
    """
    
    def __init__(self, directorio_plugins: str = "plugins"):
        """
        Inicializa el núcleo con el directorio de plugins.
        
        Args:
            directorio_plugins (str): Nombre del directorio donde están los plugins
        """
        self.directorio_plugins = directorio_plugins
        self.plugins_cargados: Dict[str, InterfazPlugin] = {}
        
    def escanear_plugins(self) -> List[str]:
        """
        Escanea el directorio de plugins y retorna los archivos .py encontrados.
        
        Returns:
            List[str]: Lista de rutas completas de archivos de plugins
        """
        ruta_plugins = os.path.join(os.path.dirname(__file__), self.directorio_plugins)
        
        if not os.path.exists(ruta_plugins):
            print(f"⚠️  Advertencia: El directorio '{self.directorio_plugins}' no existe.")
            return []
        
        archivos_plugins = []
        
        # Escanear todos los archivos .py en el directorio
        for archivo in os.listdir(ruta_plugins):
            if archivo.endswith('.py') and not archivo.startswith('__'):
                ruta_completa = os.path.join(ruta_plugins, archivo)
                archivos_plugins.append(ruta_completa)
                
        return archivos_plugins
    
    def cargar_plugin(self, ruta_archivo: str) -> bool:
        """
        Carga dinámicamente un plugin desde un archivo usando importlib.
        
        Args:
            ruta_archivo (str): Ruta completa al archivo del plugin
            
        Returns:
            bool: True si se cargó exitosamente, False en caso contrario
        """
        try:
            # Obtener el nombre del módulo desde el nombre del archivo
            nombre_modulo = os.path.splitext(os.path.basename(ruta_archivo))[0]
            
            # Crear una especificación del módulo
            spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
            
            if spec is None or spec.loader is None:
                print(f"❌ Error: No se pudo crear la especificación para {nombre_modulo}")
                return False
            
            # Crear el módulo desde la especificación
            modulo = importlib.util.module_from_spec(spec)
            
            # Ejecutar el módulo
            spec.loader.exec_module(modulo)
            
            # Verificar que el módulo tenga una instancia 'plugin'
            if not hasattr(modulo, 'plugin'):
                print(f"⚠️  {nombre_modulo}: No contiene una instancia 'plugin'")
                return False
            
            plugin_instancia = modulo.plugin
            
            # Verificar que implemente la interfaz correcta
            if not isinstance(plugin_instancia, InterfazPlugin):
                print(f"⚠️  {nombre_modulo}: No implementa InterfazPlugin")
                return False
            
            # Guardar el plugin cargado
            self.plugins_cargados[nombre_modulo] = plugin_instancia
            print(f"✅ Plugin cargado: {plugin_instancia.obtener_nombre()}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error al cargar {ruta_archivo}: {str(e)}")
            return False
    
    def cargar_todos_los_plugins(self) -> int:
        """
        Carga todos los plugins encontrados en el directorio.
        
        Returns:
            int: Número de plugins cargados exitosamente
        """
        print("🔍 Escaneando directorio de plugins...")
        archivos = self.escanear_plugins()
        
        if not archivos:
            print("⚠️  No se encontraron plugins para cargar.")
            return 0
        
        print(f"📁 Encontrados {len(archivos)} archivo(s) de plugins\n")
        
        plugins_exitosos = 0
        for archivo in archivos:
            if self.cargar_plugin(archivo):
                plugins_exitosos += 1
        
        print(f"\n✨ Total de plugins cargados: {plugins_exitosos}/{len(archivos)}\n")
        return plugins_exitosos
    
    def listar_plugins(self):
        """
        Muestra una lista de todos los plugins cargados con sus descripciones.
        """
        if not self.plugins_cargados:
            print("No hay plugins cargados.")
            return
        
        print("\n" + "="*60)
        print("PLUGINS DISPONIBLES")
        print("="*60)
        
        for idx, (nombre_modulo, plugin) in enumerate(self.plugins_cargados.items(), 1):
            print(f"\n[{idx}] {plugin.obtener_nombre()}")
            print(f"    📝 {plugin.obtener_descripcion()}")
            print(f"    📦 Módulo: {nombre_modulo}")
        
        print("\n" + "="*60 + "\n")
    
    def ejecutar_plugin(self, numero_plugin: int, dato: str) -> str:
        """
        Ejecuta un plugin específico con los datos proporcionados.
        
        Args:
            numero_plugin (int): Número del plugin (1-indexed)
            dato (str): Dato de entrada para el plugin
            
        Returns:
            str: Resultado de la ejecución del plugin
        """
        if numero_plugin < 1 or numero_plugin > len(self.plugins_cargados):
            return "❌ Número de plugin inválido"
        
        # Obtener el plugin por índice
        plugin = list(self.plugins_cargados.values())[numero_plugin - 1]
        
        try:
            resultado = plugin.ejecutar(dato)
            return resultado
        except Exception as e:
            return f"❌ Error al ejecutar el plugin: {str(e)}"


def menu_interactivo(nucleo: NucleoPlugins):
    """
    Menú interactivo para la aplicación de consola.
    
    Args:
        nucleo (NucleoPlugins): Instancia del núcleo de plugins
    """
    while True:
        print("\n" + "="*60)
        print("SISTEMA DE PLUGINS - MENÚ PRINCIPAL")
        print("="*60)
        print("1. Listar plugins disponibles")
        print("2. Ejecutar un plugin")
        print("3. Recargar plugins")
        print("4. Salir")
        print("="*60)
        
        opcion = input("\n👉 Selecciona una opción: ").strip()
        
        if opcion == '1':
            nucleo.listar_plugins()
            
        elif opcion == '2':
            if not nucleo.plugins_cargados:
                print("\n⚠️  No hay plugins cargados. Recarga los plugins primero.")
                continue
            
            nucleo.listar_plugins()
            
            try:
                num_plugin = int(input("Selecciona el número del plugin: ").strip())
                dato_entrada = input("Ingresa el dato de entrada: ").strip()
                
                print("\n" + "-"*60)
                print("RESULTADO:")
                print("-"*60)
                resultado = nucleo.ejecutar_plugin(num_plugin, dato_entrada)
                print(resultado)
                print("-"*60)
                
            except ValueError:
                print("❌ Por favor ingresa un número válido")
            except Exception as e:
                print(f"❌ Error: {str(e)}")
                
        elif opcion == '3':
            nucleo.plugins_cargados.clear()
            print("\n🔄 Recargando plugins...\n")
            nucleo.cargar_todos_los_plugins()
            
        elif opcion == '4':
            print("\n👋 ¡Hasta luego! Saliendo del sistema de plugins...")
            break
            
        else:
            print("\n❌ Opción no válida. Por favor selecciona 1, 2, 3 o 4.")


def main():
    """
    Función principal que inicia la aplicación.
    """
    print("\n" + "="*60)
    print("🚀 SISTEMA DE PLUGINS - PATRÓN MICROKERNEL")
    print("="*60)
    print("Implementación de carga dinámica de módulos en Python")
    print("="*60 + "\n")
    
    # Crear instancia del núcleo
    nucleo = NucleoPlugins(directorio_plugins="plugins")
    
    # Cargar todos los plugins automáticamente al inicio
    nucleo.cargar_todos_los_plugins()
    
    # Iniciar menú interactivo
    menu_interactivo(nucleo)


if __name__ == "__main__":
    main()
