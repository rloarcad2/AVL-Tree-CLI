"""Funciones para buscar y cargar datos desde archivos CSV."""

from __future__ import annotations
import csv
from pathlib import Path
from typing import List


PROJECT_ROOT = Path(__file__).resolve().parent


def load_numbers_from_csv(file_path: str) -> List[int]:
    """Carga enteros desde un CSV.

    Acepta formatos como:
    - una columna por fila: 10
    - múltiples columnas: 10,20,30
    """
    numbers: List[int] = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                value = value.strip()
                if value:
                    numbers.append(int(value))
    return numbers



def find_csv_files(search_root: str | None = None) -> List[Path]:
    """Busca archivos CSV de forma recursiva.

    Si no se indica una ruta, busca dentro del proyecto actual.
    """
    root = Path(search_root).expanduser().resolve() if search_root else PROJECT_ROOT
    if not root.exists():
        raise FileNotFoundError(f'La carpeta de búsqueda no existe: {root}')
    if root.is_file():
        return [root] if root.suffix.lower() == '.csv' else []

    csv_files = sorted(
        [path for path in root.rglob('*.csv') if path.is_file()],
        key=lambda p: (str(p.parent).lower(), p.name.lower())
    )
    return csv_files



def choose_csv_file() -> str | None:
    """Permite al usuario seleccionar un CSV encontrado en el proyecto o ingresar una ruta manual."""
    print('\nBúsqueda de archivos CSV')
    print('1. Buscar CSV en la carpeta del proyecto')
    print('2. Buscar CSV en otra carpeta')
    print('3. Escribir la ruta manualmente')
    print('4. Cancelar')

    option = input('Seleccione una opción: ').strip()

    if option == '1':
        files = find_csv_files()
    elif option == '2':
        folder = input('Ingrese la ruta de la carpeta donde desea buscar: ').strip()
        files = find_csv_files(folder)
    elif option == '3':
        manual_path = input('Ingrese la ruta completa del archivo CSV: ').strip()
        return manual_path or None
    elif option == '4':
        return None
    else:
        print('Opción no válida.')
        return None

    if not files:
        print('No se encontraron archivos CSV disponibles.')
        return None

    print('\nArchivos CSV encontrados:')
    for index, file in enumerate(files, start=1):
        try:
            display_path = file.relative_to(PROJECT_ROOT)
        except ValueError:
            display_path = file
        print(f'{index}. {display_path}')

    while True:
        selection = input('Seleccione el número del archivo que desea cargar (o 0 para cancelar): ').strip()
        if selection == '0':
            return None
        if selection.isdigit():
            selected_index = int(selection)
            if 1 <= selected_index <= len(files):
                return str(files[selected_index - 1])
        print('Selección inválida. Intente nuevamente.')
