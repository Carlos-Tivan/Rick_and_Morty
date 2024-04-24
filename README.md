# Obtención y Análisis de Datos de Personajes de Rick and Morty

Este script en Python interactúa con la API de Rick and Morty para obtener datos de personajes, realizar filtrados basados en criterios específicos y guardar los resultados en archivos CSV para análisis.

## Características

- **Obtención de Datos:** Utiliza la API de Rick and Morty para recuperar información de personajes.
- **Filtrado de Personajes:** Filtra personajes según criterios como estado, género y especie.
- **Conteo de Episodios:** Determina la cantidad de episodios en los que aparece cada personaje.
- **Generación de Archivos CSV:** Guarda datos de personajes filtrados en archivos CSV con campos específicos.

## Descripción del Script

El script consta de las siguientes funciones clave:

- **`fetch_characters(url)`**:
  - Realiza una solicitud GET a la URL especificada y devuelve los datos de respuesta en formato JSON.
  
- **`filter_characters(characters, status=None, gender=None, species=None)`**:
  - Filtra una lista de personajes según el estado, género y especie especificados.
  
- **`count_episodes(character_url)`**:
  - Cuenta la cantidad de episodios en los que aparece un personaje basado en su URL de API.
  
- **`save_to_csv(characters, filename, fields)`**:
  - Guarda datos de personajes en un archivo CSV con campos específicos.

## Uso

1. **Clonar el Repositorio:**
   Clona el repositorio que contiene este script en tu máquina local.
   
2. **Instalar Dependencias:**
   Asegúrate de tener instalados los paquetes de Python necesarios (`requests`, `csv`).

3. **Actualizar Parámetros de la Función Principal:**
   Modifica la función principal (`main()`) para personalizar los criterios de filtrado y los nombres de archivos según sea necesario.

4. **Ejecutar el Script:**
   Ejecuta el script para obtener, filtrar y guardar datos de personajes en archivos CSV.

## Dependencias

- Python 3.x
- Biblioteca `requests` para solicitudes HTTP
- Módulo `csv` para manejo de archivos CSV

## Ejemplo de Uso

```bash
python main.py
