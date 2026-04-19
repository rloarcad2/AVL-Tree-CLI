"""Programa principal con interfaz de línea de comandos para Árbol AVL."""

from __future__ import annotations
import os
import subprocess
from avl import AVL
from csv_loader import load_numbers_from_csv, choose_csv_file
from graphviz_export import export_to_dot


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def pause() -> None:
    input('\nPresione Enter para continuar...')


def show_menu() -> None:
    print('=' * 50)
    print('        GESTOR INTERACTIVO DE ÁRBOL AVL')
    print('=' * 50)
    print('1. Insertar número')
    print('2. Buscar número')
    print('3. Eliminar número')
    print('4. Cargar árbol desde archivo CSV')
    print('5. Visualizar árbol con Graphviz')
    print('6. Mostrar recorrido inorden')
    print('7. Salir')
    print('=' * 50)


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Entrada inválida. Debe ingresar un número entero.')


def visualize_tree(tree: AVL) -> None:
    dot_file = 'avl_tree.dot'
    png_file = 'avl_tree.png'
    export_to_dot(tree.root, dot_file)
    print(f'Se generó el archivo DOT: {dot_file}')

    try:
        subprocess.run(['dot', '-Tpng', dot_file, '-o', png_file], check=True)
        print(f'Se generó la imagen: {png_file}')

        if os.name == 'nt':
            os.startfile(png_file)  # type: ignore[attr-defined]
        elif os.name == 'posix':
            try:
                subprocess.run(['xdg-open', png_file], check=False)
            except FileNotFoundError:
                print('No fue posible abrir automáticamente la imagen.')
    except FileNotFoundError:
        print('Graphviz no está instalado o el comando "dot" no está en el PATH.')
        print('Puede abrir manualmente el archivo .dot con Graphviz.')
    except subprocess.CalledProcessError:
        print('Ocurrió un error al generar la imagen con Graphviz.')


def load_csv_into_tree(tree: AVL) -> None:
    path = choose_csv_file()
    if not path:
        print('Carga cancelada.')
        return

    try:
        values = load_numbers_from_csv(path)
        for value in values:
            tree.insert(value)
        print('\nDatos cargados correctamente desde CSV.')
        print(f'Archivo utilizado: {path}')
        print('Valores insertados:', values)
        print('Recorrido inorden actual:', tree.inorder())
    except FileNotFoundError:
        print('No se encontró el archivo especificado.')
    except ValueError:
        print('El CSV contiene datos no válidos. Solo se permiten enteros.')
    except Exception as error:
        print(f'Ocurrió un error al cargar el CSV: {error}')


def main() -> None:
    tree = AVL()

    while True:
        clear_screen()
        show_menu()
        option = input('Seleccione una opción: ').strip()

        if option == '1':
            number = read_int('Ingrese el número a insertar: ')
            tree.insert(number)
            print(f'Número {number} insertado correctamente.')
            print('Recorrido inorden actual:', tree.inorder())
            pause()

        elif option == '2':
            number = read_int('Ingrese el número a buscar: ')
            found = tree.search(number)
            if found:
                print(f'El número {number} SÍ existe en el árbol.')
            else:
                print(f'El número {number} NO existe en el árbol.')
            pause()

        elif option == '3':
            number = read_int('Ingrese el número a eliminar: ')
            if tree.search(number):
                tree.delete(number)
                print(f'Número {number} eliminado correctamente.')
            else:
                print(f'El número {number} no existe en el árbol.')
            print('Recorrido inorden actual:', tree.inorder())
            pause()

        elif option == '4':
            load_csv_into_tree(tree)
            pause()

        elif option == '5':
            visualize_tree(tree)
            pause()

        elif option == '6':
            print('Recorrido inorden del árbol:', tree.inorder())
            pause()

        elif option == '7':
            print('Saliendo del programa...')
            break

        else:
            print('Opción no válida. Intente nuevamente.')
            pause()


if __name__ == '__main__':
    main()
