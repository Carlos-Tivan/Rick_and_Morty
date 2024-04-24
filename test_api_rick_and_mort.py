import pytest
from main import filter_characters, count_episodes

# Prueba test en filter_characters
def test_filter_characters():

    # Lista de personajes a filtrar

    characters = [
        {'name': 'Rick Sanchez', 'status': 'Alive', 'gender': 'Male', 'species': 'Human'},
        {'name': 'Morty Smith', 'status': 'Alive', 'gender': 'Male', 'species': 'Human'},
        {'name': 'Summer Smith', 'status': 'Alive', 'gender': 'Female', 'species': 'Human'},
        {'name': 'Beth Smith', 'status': 'Dead', 'gender': 'Female', 'species': 'Human'},
        {'name': 'Alien', 'status': 'Dead', 'gender': 'Unknown', 'species': 'Alien'}
    ]

    # Caso de prueba: Filtrar por estado "Alive" y género "Male"
    filtered_alive_male = filter_characters(characters, status="Alive", gender="Male")
    assert len(filtered_alive_male) == 2  # Deberían haber 2 personajes (Rick y Morty)

    # Caso de prueba: Filtrar por estado "Dead" y género "Female"
    filtered_dead_female = filter_characters(characters, status="Dead", gender="Female")
    assert len(filtered_dead_female) == 1  # Debería haber 1 personaje (Beth)

    # Caso de prueba: Filtrar por especie "Human" y género "Female"
    filtered_human_female = filter_characters(characters, species="Human", gender="Female")
    assert len(filtered_human_female) == 2  # Deberían haber 2 personajes (Summer y Beth)

# Prueba para la función count_episodes
def test_count_episodes():
    # URL de ejemplo para un personaje con 3 episodios
    character_url_with_episodes = 'https://rickandmortyapi.com/api/character/1'
    # URL de ejemplo para un personaje sin episodios
    character_url_no_episodes = 'https://rickandmortyapi.com/api/character/2'

    # Caso de prueba: Contar episodios para el personaje con episodios
    num_episodes_with_episodes = count_episodes(character_url_with_episodes)
    assert num_episodes_with_episodes == 3  # Deberían ser 3 episodios para este personaje

    # Caso de prueba: Contar episodios para el personaje sin episodios
    num_episodes_no_episodes = count_episodes(character_url_no_episodes)
    assert num_episodes_no_episodes == 0  # Deberían ser 0 episodios para este personaje

# Ejecutar las pruebas con pytest
if __name__ == '__main__':
    pytest.main()
