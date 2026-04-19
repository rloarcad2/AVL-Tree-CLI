# Proyecto: Árbol AVL interactivo en Python

## Descripción
Este proyecto implementa un **programa interactivo en Python** para crear, manipular y visualizar un **Árbol AVL**, extendiendo la funcionalidad de un **Árbol Binario de Búsqueda (ABB)**.

El programa permite:
- Insertar elementos manteniendo el balance del árbol.
- Buscar elementos.
- Eliminar elementos con reequilibrio automático.
- Cargar datos desde archivos CSV.
- Generar una representación visual en **Graphviz**.

---

## Integrantes
> Complete esta sección antes de entregar.

- Nombre: ____________________  
  Carnet: ____________________  
  Participación: _______%

- Nombre: ____________________  
  Carnet: ____________________  
  Participación: _______%

> Si el trabajo es individual, deje solo un integrante con 100%.

---

## Requisitos
- Python 3.10 o superior
- Graphviz instalado en el sistema
- Librería de Python `graphviz` (opcional para futuras mejoras, aunque esta implementación usa el ejecutable `dot`)

### Instalar Graphviz
- **Windows:** descargar e instalar Graphviz y agregarlo al PATH.
- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt install graphviz
  ```
- **macOS (Homebrew):**
  ```bash
  brew install graphviz
  ```

---

## Estructura del proyecto
```text
avl_cli_project/
├── abb.py
├── avl.py
├── csv_loader.py
├── graphviz_export.py
├── main.py
├── README.md
├── requirements.txt
└── examples/
    ├── ejemplo1.csv
    ├── ejemplo2.csv
    └── ejemplo3.csv
```

---

## Cómo ejecutar
1. Clone el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd avl_cli_project
   ```

2. Ejecute el programa:
   ```bash
   python main.py
   ```

---

## Menú del programa
El sistema muestra un menú con las siguientes opciones:
1. Insertar número en el árbol.
2. Buscar número en el árbol.
3. Eliminar número del árbol.
4. Cargar árbol desde un archivo CSV.
5. Visualizar árbol mediante Graphviz.
6. Mostrar recorrido inorden.
7. Salir.

---

## Cómo probar la carga CSV
Puede usar cualquiera de los archivos de ejemplo de la carpeta `examples/`.

Ejemplo:
```text
examples/ejemplo1.csv
```

Contenido:
```csv
30,20,40,10,25,35,50
```

---

## Salida Graphviz
Al seleccionar la opción de visualización:
- se genera un archivo `avl_tree.dot`
- se genera una imagen `avl_tree.png` si Graphviz está instalado correctamente

El nodo muestra:
- valor del nodo
- altura (`H`) del nodo

---

## Uso de herencia
Este proyecto cumple con el requisito de herencia:
- `ABB` es la clase base.
- `AVL` hereda de `ABB` y sobrescribe los métodos necesarios para mantener el balance.

---

## Recomendaciones para la entrega
- Subir este proyecto a GitHub.
- Agregar como colaborador al usuario **`ingVillatoroUMG`**.
- Completar la sección de integrantes en este `README.md`.
- Verificar que Graphviz funcione correctamente antes de la demostración.

---

## Ejemplo de uso
```text
Seleccione una opción: 1
Ingrese el número a insertar: 30
Número 30 insertado correctamente.

Seleccione una opción: 1
Ingrese el número a insertar: 20
Número 20 insertado correctamente.

Seleccione una opción: 5
Se generó el archivo DOT: avl_tree.dot
Se generó la imagen: avl_tree.png
```

---

## Licencia
Uso académico.
