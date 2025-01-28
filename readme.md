# Generador de Palabras Filtradas

Este proyecto es una aplicación en Python que permite trabajar con un conjunto de palabras, filtrándolas según su longitud y proporcionando herramientas para jugar y analizar palabras basadas en pistas dadas.

## Características

- **Filtrado por longitud**: Lee palabras desde un archivo (`listado-general.txt`) y filtra las palabras por su cantidad de letras.
- **Eliminación de acentos**: Normaliza palabras eliminando caracteres acentuados para un análisis uniforme.
- **Expresiones regulares dinámicas**: Genera patrones basados en pistas dadas por el usuario para filtrar palabras posibles.
- **Interfaz interactiva**: Permite al usuario ingresar pistas y ajusta las palabras posibles en consecuencia.

## Requisitos

- **Python 3.8+**
- Archivo de texto llamado `listado-general.txt` que contenga una lista de palabras, una por línea.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/nombre-del-repo.git
   ```
2. Ve al directorio del proyecto:
   ```bash
   cd nombre-del-repo
   ```
3. Instala los requisitos necesarios (si los hubiera):
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Ejecución del programa principal**: Ejecuta el archivo principal:

   ```bash
   python main.py
   ```

   - Ingresa la cantidad de letras que tendrán las palabras.
   - Ingresa la cantidad de intentos permitidos.

2. **Archivo de palabras**: Asegúrate de que el archivo `listado-general.txt` contenga palabras válidas. Por ejemplo:

   ```
   árbol
   casa
   niño
   juego
   ```

3. **Juego interactivo**:

   - El programa te sugerirá palabras.
   - Debes ingresar pistas para cada intento:
     - `B`: Letra en la posición correcta.
     - `Y`: Letra está en la palabra pero en una posición incorrecta.
     - `M`: Letra no está en la palabra.

## Archivos principales

- ``: Contiene la lógica principal del programa, incluyendo el manejo de intentos y generación de expresiones regulares.
- ``: Contiene funciones para leer el archivo de texto y procesar palabras (eliminación de acentos, filtrado por longitud).

## Ejemplo de uso

Ejemplo de ejecución:

```
Ingrese la cantidad de letras de las palabras: 5
Ingrese la cantidad de intentos permitidos: 6
Intente con la palabra: arbol
Ingrese pista (B/Y/M) o escriba 'skip' para saltar: MMMMM
Palabras posibles: ['casa', 'juego']
```

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request si deseas mejorar este proyecto.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

