import re
from obtenerPalabras import organizar_palabras_por_alfabeto
import random

# Solicita al usuario la cantidad de letras para las palabras y la cantidad de intentos disponibles.
cantidad_letras = int(input("Ingrese la cantidad de letras de las palabras: "))
cantidad_intentos = int(input("Ingrese la cantidad de intentos permitidos: "))

# Filtra las palabras disponibles con base en la cantidad de letras especificada por el usuario.
palabras_posibles = [
    palabra for palabra in organizar_palabras_por_alfabeto(cantidad_letras)
]

# Si no hay palabras con la longitud requerida, se detiene el programa.
if not palabras_posibles:
    print("No hay palabras disponibles con la longitud especificada. Intenta nuevamente.")
    exit()

# Genera una expresión regular a partir de la palabra y las pistas proporcionadas.
def generar_regex(palabra, pista):
    # Inicializa la expresión regular permitiendo cualquier letra en cada posición.
    regex = ['[a-z]'] * len(palabra)

    # Identifica las letras que no deben estar en la palabra.
    letras_excluidas = set(letra for letra, res in zip(palabra, pista) if res == 'M')

    # Ajusta la expresión regular según las pistas recibidas.
    for i, (letra, resultado) in enumerate(zip(palabra, pista)):
        if resultado == 'B':  # La letra está en la posición correcta.
            regex[i] = letra
        elif resultado == 'M':  # La letra no está en la palabra.
            regex[i] = f'[^{letra}]'
        elif resultado == 'Y':  # La letra está en la palabra pero en otra posición.
            regex[i] = f'[^{letra}]'

    # Añade condiciones para asegurar que las letras marcadas como 'Y' aparezcan en otras posiciones.
    letras_condicionales = ''.join(
        f'(?=.*{letra})' for letra, res in zip(palabra, pista) if res == 'Y'
    )

    # Combina las condiciones y la estructura de la expresión regular.
    return f'^{letras_condicionales}{"".join(regex)}$'

# Filtra las palabras posibles utilizando la expresión regular generada.
def filtrar_palabras(palabra, pista, lista_palabras):
    regex = generar_regex(palabra, pista)
    print(f'Expresión regular generada: {regex}')
    # Devuelve las palabras que cumplen con la expresión regular.
    palabras_filtradas = [p for p in lista_palabras if re.match(regex, p)]
    return palabras_filtradas

# Comienza el juego, permitiendo al usuario realizar varios intentos.
for intento in range(cantidad_intentos):
    # Si no quedan palabras posibles, termina el juego.
    if not palabras_posibles:
        print("¡No hay más palabras posibles!")
        break
    
    # Selecciona una palabra aleatoria de las posibles.
    palabra_ingresada = palabras_posibles[random.randint(0, len(palabras_posibles)-1)]
    print(f'Intente con la palabra: {palabra_ingresada}')
    
    while True:
        # Solicita al usuario que proporcione la pista para la palabra.
        pista = input("Ingrese pista (B/Y/M) o escriba 'skip' para saltar: ").upper()
        
        if pista == 'SKIP':
            # Si el usuario decide saltar esta palabra, se elimina de la lista de posibles.
            palabras_posibles.remove(palabra_ingresada)
            print(f"Palabra '{palabra_ingresada}' eliminada. Buscando otra palabra...")
            break  # Sale del bucle interno y selecciona una nueva palabra.
        elif not pista.isalpha() or not all(letra in 'BYM' for letra in pista):
            print("La pista solo puede contener las letras 'B', 'Y' o 'M'.")
        elif len(pista) != len(palabra_ingresada):
            print(f"La pista debe tener exactamente {len(palabra_ingresada)} caracteres.")
        elif pista == 'B' * cantidad_letras:
            # Si todas las letras están correctas, el usuario gana.
            print(f"¡Ganaste! La palabra correcta era: {palabra_ingresada}")
            exit()
        else:
            # Filtra las palabras posibles según la pista ingresada.
            palabras_posibles = filtrar_palabras(palabra_ingresada, pista, palabras_posibles)
            # Muestra las palabras posibles restantes.
            print(f'Palabras posibles: {palabras_posibles}')
            
            # Si queda una sola palabra posible, el juego termina con éxito.
            if len(palabras_posibles) == 1:
                print(f"¡La palabra correcta es: {palabras_posibles[0]}!")
                exit()
            break

# Mensaje final si el usuario agota todos los intentos sin ganar.
print("¡Se acabaron los intentos! Mejor suerte la próxima vez.")