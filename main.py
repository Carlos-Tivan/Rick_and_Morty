import requests
import csv
import os

# By: Carlos Tivan
def fetch_characters(url):
    """
    Realiza una solicitud GET a una URL especificada y devuelve los datos en formato JSON.
    Args:
        url (str): La URL a la que se realizará la solicitud.
    Returns:
        dict or None: Los datos obtenidos de la respuesta HTTP en formato JSON, o None si hay un error.
    """
    try:
        response = requests.get(url)  # Realiza la solicitud HTTP GET
        response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        return response.json()  # Devuelve los datos de la respuesta en formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None


def filter_characters(characters, status=None, gender=None, species=None):
    """
    Filtra una lista de personajes según el estado, género y especie especificados.
    Args:
        characters (list): Lista de personajes (diccionarios) a ser filtrados.
        status (str): Estado por el cual filtrar los personajes ('Alive' o 'Dead'). Por defecto None (sin filtrar por estado).
        gender (str): Género por el cual filtrar los personajes ('Male' o 'Female'). Por defecto None (sin filtrar por género).
        species (str): Especie por la cual filtrar los personajes. Por defecto None (sin filtrar por especie).
    Returns:
        list: Lista de personajes filtrados que cumplen con los criterios especificados.
    """
    filtered_characters = []
    for character in characters:
        if (status is None or character['status'].lower() == status.lower()) and \
           (gender is None or character['gender'].lower() == gender.lower()) and \
           (species is None or character['species'].lower() == species.lower()):
            filtered_characters.append(character)
    return filtered_characters


def count_episodes(character_url):
    """
    Cuenta la cantidad de episodios en los que aparece un personaje.

    Args:
        character_url (str): URL del personaje del cual se contarán los episodios.

    Returns:
        int: Cantidad de episodios en los que aparece el personaje, o 0 si hay un error.
    """
    try:
        response = requests.get(character_url)  # Realiza la solicitud HTTP GET
        response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        character_data = response.json()  # Obtiene los datos del personaje en formato JSON
        print("Response JSON:", character_data)  # Imprimir la respuesta JSON para depurar
        return len(character_data['episode'])  # Devuelve la cantidad de episodios
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error al obtener la cantidad de episodios: {e}")
        return 0


def save_to_csv(characters, filename, fields):
    """
    Guarda los datos de los personajes en un archivo CSV.

    Args:
        characters (list): Lista de personajes (diccionarios) a ser guardados en el archivo CSV.
        filename (str): Nombre del archivo CSV donde se guardarán los datos.
        fields (list): Lista de nombres de campo (encabezados) para el archivo CSV.

    Returns:
        None
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)  # Crea un escritor CSV
        writer.writeheader()  # Escribe la fila de encabezado en el archivo CSV
        for character in characters:
            episode_count = count_episodes(character['url'])  # Obtiene el número de episodios
            row = {
                'ID': character['id'],
                'Name': character['name'],
                'Status': character['status'],
                'Gender': character['gender'],
                'Species': character['species'],
                'Location': character['location']['name'],
                'Image': character['image'],
                'Episode Count': episode_count
            }
            writer.writerow(row)  # Escribe una fila en el archivo CSV


def main():
    """
    Función principal que realiza la consulta, filtrado y guarda los resultados en archivos CSV.
    """
    base_url = "https://rickandmortyapi.com/api/character"

    # Consultar todos los personajes desde la API
    all_characters = fetch_characters(base_url)
    if not all_characters:
        print("No se obtuvieron los datos de los personajes.")
        return

    # Filtrar personajes vivos por estado "Alive", género "Male" y especie "Human"
    alive_characters = filter_characters(all_characters['results'], status="Alive", gender="Male", species="Human")
    # Filtrar personajes muertos por estado "Dead", género "Female" y especie "Human"
    dead_characters = filter_characters(all_characters['results'], status="Alive", gender="Female", species="Alien")

    # Definir los campos para guardar en CSV mediante una lista
    csv_fields = ['ID', 'Name', 'Status', 'Gender', 'Species', 'Location', 'Image', 'Episode Count']

    # Guardar personajes vivos en un archivo CSV
    alive_filename = "male_characters.csv"
    save_to_csv(alive_characters, alive_filename, csv_fields)
    print(f"Personajes (género masculino) guardados en: {os.path.abspath(alive_filename)}")

    # Guardar personajes muertos en un archivo CSV
    dead_filename = "female_characters.csv"
    save_to_csv(dead_characters, dead_filename, csv_fields)
    print(f"Personajes (género femenino) guardados en: {os.path.abspath(dead_filename)}")

if __name__ == "__main__":
    main()  # Llama a la función principal
