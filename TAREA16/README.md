# 🚀 Sistema de Plugins - Patrón Microkernel

## 📋 Descripción

Implementación práctica del **patrón Plug-in (Microkernel)** en Python puro, demostrando la carga dinámica de módulos externos sin usar frameworks ni librerías externas.

Este proyecto es una aplicación de consola que ilustra:
- ✅ Separación clara entre **Núcleo** y **Plugins**
- ✅ Carga dinámica de módulos usando `importlib`
- ✅ Uso de interfaces abstractas (ABC)
- ✅ Solo librería estándar de Python

---

## 📁 Estructura del Proyecto

```
TAREA16/
│
├── main.py                    # 🎯 NÚCLEO: Carga dinámica de plugins
├── interfaz_plugin.py         # 📜 CONTRATO: Interfaz abstracta
│
└── plugins/                   # 📦 DIRECTORIO DE PLUGINS
    ├── plugin_saludo.py       # Plugin 1: Convierte a mayúsculas
    ├── plugin_calculadora.py  # Plugin 2: Evalúa expresiones matemáticas
    └── plugin_conversor.py    # Plugin 3: Invierte texto
```

---

## 🔧 Componentes del Sistema

### 1️⃣ **Interfaz (Contrato)** - `interfaz_plugin.py`

Define la **clase abstracta** que todos los plugins deben implementar:

```python
class InterfazPlugin(ABC):
    @abstractmethod
    def obtener_nombre(self) -> str:
        pass
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass
    
    @abstractmethod
    def ejecutar(self, dato: str) -> str:
        pass
```

**Responsabilidad**: Establecer el contrato que garantiza que todos los plugins tengan los mismos métodos.

---

### 2️⃣ **Plugins (Implementaciones)**

Cada plugin implementa `InterfazPlugin` y debe tener una instancia global llamada `plugin`:

#### 📌 `plugin_saludo.py`
- Convierte texto a mayúsculas
- Agrega un saludo personalizado

#### 📌 `plugin_calculadora.py`
- Evalúa expresiones matemáticas básicas
- Soporta +, -, *, /, paréntesis

#### 📌 `plugin_conversor.py`
- Invierte el orden de caracteres
- Muestra estadísticas del texto

---

### 3️⃣ **Núcleo (Core)** - `main.py`

El componente más importante del sistema. Realiza:

1. **Escaneo automático** del directorio `/plugins`
2. **Carga dinámica** usando `importlib.util`:
   ```python
   spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
   modulo = importlib.util.module_from_spec(spec)
   spec.loader.exec_module(modulo)
   ```
3. **Validación** de que cada plugin implementa `InterfazPlugin`
4. **Ejecución interactiva** mediante menú de consola

**Características clave**:
- ❌ NO usa `import plugin_saludo` al inicio
- ✅ Detecta archivos `.py` automáticamente
- ✅ Carga plugins en tiempo de ejecución
- ✅ Manejo robusto de errores

---

## 🚀 Cómo Ejecutar

### Paso 1: Verificar la estructura
Asegúrate de tener esta estructura de carpetas:
```
TAREA16/
├── main.py
├── interfaz_plugin.py
└── plugins/
    ├── plugin_saludo.py
    ├── plugin_calculadora.py
    └── plugin_conversor.py
```

### Paso 2: Ejecutar el programa
Desde la carpeta `TAREA16`, ejecuta:

```bash
python main.py
```

### Paso 3: Usar el sistema
El menú interactivo te permite:
1. **Listar plugins**: Ver todos los plugins cargados
2. **Ejecutar plugin**: Seleccionar un plugin e ingresar datos
3. **Recargar plugins**: Volver a escanear el directorio
4. **Salir**: Cerrar la aplicación

---

## 💡 Ejemplo de Uso

```
🚀 SISTEMA DE PLUGINS - PATRÓN MICROKERNEL
============================================================

🔍 Escaneando directorio de plugins...
📁 Encontrados 3 archivo(s) de plugins

✅ Plugin cargado: Plugin Saludo
✅ Plugin cargado: Plugin Calculadora
✅ Plugin cargado: Plugin Conversor

✨ Total de plugins cargados: 3/3

============================================================
SISTEMA DE PLUGINS - MENÚ PRINCIPAL
============================================================
1. Listar plugins disponibles
2. Ejecutar un plugin
3. Recargar plugins
4. Salir
============================================================

👉 Selecciona una opción: 2

[1] Plugin Saludo
    📝 Convierte el texto a MAYÚSCULAS y agrega un saludo personalizado

[2] Plugin Calculadora
    📝 Evalúa expresiones matemáticas básicas

[3] Plugin Conversor
    📝 Invierte el orden de los caracteres de un texto

Selecciona el número del plugin: 1
Ingresa el dato de entrada: hola mundo

------------------------------------------------------------
RESULTADO:
------------------------------------------------------------
¡HOLA! Tu mensaje en mayúsculas es: HOLA MUNDO
------------------------------------------------------------
```

---

## 🎓 Conceptos Educativos Demostrados

### ✅ Patrón Microkernel/Plug-in
- **Núcleo mínimo** que no conoce las implementaciones específicas
- **Plugins intercambiables** sin modificar el núcleo
- **Extensibilidad**: Agregar nuevos plugins sin cambiar código existente

### ✅ Carga Dinámica de Módulos
```python
# Sin carga dinámica (estática):
import plugin_saludo  # ❌ No flexible

# Con carga dinámica (runtime):
spec = importlib.util.spec_from_file_location(...)  # ✅ Flexible
```

### ✅ Programación por Contrato (Design by Contract)
- `InterfazPlugin` define el contrato
- Todos los plugins deben cumplir el contrato
- El núcleo trabaja con la abstracción, no con implementaciones concretas

### ✅ Principios SOLID
- **Open/Closed**: Abierto a extensión (nuevos plugins), cerrado a modificación (núcleo)
- **Dependency Inversion**: El núcleo depende de la abstracción, no de implementaciones

---

## 🔨 Cómo Crear tu Propio Plugin

1. **Crea un archivo** en `/plugins/`, por ejemplo `plugin_contador.py`

2. **Importa la interfaz**:
```python
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from interfaz_plugin import InterfazPlugin
```

3. **Implementa la clase**:
```python
class PluginContador(InterfazPlugin):
    def obtener_nombre(self) -> str:
        return "Plugin Contador"
    
    def obtener_descripcion(self) -> str:
        return "Cuenta las palabras de un texto"
    
    def ejecutar(self, dato: str) -> str:
        num_palabras = len(dato.split())
        return f"El texto tiene {num_palabras} palabras"
```

4. **Crea la instancia**:
```python
plugin = PluginContador()
```

5. **Ejecuta el programa** y tu plugin se cargará automáticamente

---

## 📚 Tecnologías Utilizadas

- **Python 3.x** (solo librería estándar)
- `abc` - Abstract Base Classes
- `importlib` - Carga dinámica de módulos
- `os` - Manejo de rutas y archivos
- `sys` - Configuración de paths

---

## ✨ Características Destacadas

- 🔄 **Carga automática**: Detecta plugins sin configuración manual
- 🛡️ **Validación robusta**: Verifica que los plugins cumplan el contrato
- 🎨 **Interfaz amigable**: Menú interactivo con emojis
- 📦 **Extensible**: Agrega plugins solo creando archivos nuevos
- ⚡ **Sin dependencias externas**: 100% librería estándar

---

## 🎯 Aplicaciones del Patrón

Este patrón se usa en:
- **Navegadores web**: Extensions/Add-ons (Chrome, Firefox)
- **IDEs**: Plugins de VS Code, IntelliJ
- **CMS**: Plugins de WordPress, Drupal
- **Sistemas operativos**: Drivers de dispositivos
- **Frameworks**: Middleware en Express.js, Django

---

## 👨‍🎓 Para la Presentación

### Puntos clave para explicar:
1. **Separación de responsabilidades**: Núcleo vs Plugins
2. **Carga dinámica**: `importlib` permite cargar código en runtime
3. **Contrato mediante ABC**: Garantiza consistencia
4. **Extensibilidad**: Solo agregar archivos, sin modificar el núcleo

### Demo sugerida:
1. Ejecutar el programa y mostrar los 3 plugins
2. Crear un nuevo plugin simple (ej: contador de palabras)
3. Recargar plugins y mostrar que el nuevo aparece automáticamente
4. Explicar cómo el núcleo no fue modificado

---

## 📞 Autores

Proyecto desarrollado para **TAREA16** - Curso de Arquitectura de Software

---

## 📝 Licencia

Proyecto educativo - Libre uso para fines académicos
