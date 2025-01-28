import string  # Módulo para trabajar con cadenas de caracteres
import unicodedata  # Módulo para manejar caracteres Unicode

# Función para normalizar caracteres eliminando acentos
def eliminar_acentos(palabra):
    """
    Esta función toma una palabra y elimina los acentos.
    Utiliza la normalización Unicode para separar los caracteres base de los acentos diacríticos
    y filtra cualquier componente categorizado como 'Mn' (marca no espaciada).
    
    :param palabra: Cadena de texto que puede contener caracteres con acentos.
    :return: Cadena de texto sin acentos.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', palabra) if unicodedata.category(c) != 'Mn'
    )

# Función para organizar palabras de un archivo por la longitud especificada
def organizar_palabras_por_alfabeto(cantidadLetras):
    """
    Lee palabras desde un archivo de texto ('listado-general.txt') y las organiza
    en una lista, filtrándolas por longitud y eliminando duplicados y acentos.
    
    :param cantidadLetras: Longitud específica que deben tener las palabras seleccionadas.
    :return: Lista de palabras organizadas que cumplen con la longitud especificada.
    """
    # Crear una lista para almacenar las palabras filtradas
    palabras_agrupadas = []

    # Abrir el archivo de texto en modo lectura
    with open('listado-general.txt', 'r', encoding='utf-8') as file:
        # Iterar sobre cada línea del archivo
        for linea in file:
            # Eliminar espacios en blanco al inicio y al final y convertir a minúsculas
            palabra = linea.strip().lower()
            if palabra:  # Si la línea no está vacía
                # Eliminar acentos de la palabra
                palabra_sin_acentos = eliminar_acentos(palabra)
                # Verificar que la palabra tenga la longitud requerida y no esté duplicada
                if len(palabra_sin_acentos) == cantidadLetras and palabra not in palabras_agrupadas:
                    # Añadir la palabra a la lista
                    palabras_agrupadas.append(palabra_sin_acentos)

    # Retornar la lista de palabras agrupadas
    return palabras_agrupadas


