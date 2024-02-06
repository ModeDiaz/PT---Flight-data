# Proyecto de Datos de Vuelos

Este proyecto está desarrollado en Python para el análisis de datos de vuelos almacenados en archivos JSON, CSV y LOG. Se proporcionan funciones para cargar, analizar y combinar los datos pertinentes, así como pruebas unitarias para garantizar el correcto funcionamiento de las funciones implementadas.

## Librerías

Este proyecto utiliza las siguientes librerías:

- JSON: para trabajar con datos JSON
- CSV: para leer y escribir archivos CSV
- Logging: para registrar problemas en el archivo de registro (LOG)

Estas librerías no necesitan ser instaladas ya que vienen incluidas con la instalación estándar de Python. La única librería que debes instalar es:

- Pytest: el framework para las pruebas unitarias. Puedes instalarlo mediante pip:

```bash
pip install pytest
```

## Funciones

### `load_data_json`

Esta función carga los datos de los vuelos desde un archivo JSON y devuelve una lista de diccionarios, donde cada diccionario representa un vuelo.

### `load_data_csv`

Similar a `load_data_json`, pero para archivos CSV.

### `parse_log_data`

Esta función analiza datos de vuelos desde un archivo LOG y devuelve una lista de diccionarios, donde cada diccionario representa un vuelo.

### `combine_data`

Combina los datos de vuelos de los archivos JSON, CSV y LOG en un solo conjunto de datos. Utiliza el ID del vuelo para unificar la información de cada archivo y crea un diccionario para cada vuelo.

### `calculate_revenue_per_passenger`

Calcula los ingresos por pasajero para cada vuelo utilizando la función `combine_data`. Agrega un nuevo valor a cada diccionario de vuelo que representa los ingresos por pasajero.

## Ejecución del Programa y Pruebas Unitarias

Para ejecutar el programa, sigue estos pasos:

1. Instalar la librería pytest:

```bash
pip install pytest
```

2. Ejecuta el script `flight_data_module.py` en la terminal para cargar los datos de los vuelos desde los archivos JSON, CSV y LOG, combinarlos y calcular los ingresos por pasajero:

```bash
python flight_data_module.py
```

Para ejecutar las pruebas unitarias, simplemente ejecuta el comando `pytest` en la terminal. Este comando detectará automáticamente todas las pruebas que comiencen con la palabra `test`.

Probamos diferentes escenarios, como archivos vacíos o inválidos, para verificar el buen funcionamiento del programa y las funciones implementadas.

Para verificar que todo se ha hecho correctamente vamos a mirar la cobertura con la que contamos con los siguientes comandos en la terminal:

```bash
pytest flight_data_test.py
```

Después:

```bash
coverage run -m pytest flight_data_test.py
```

Y para ver el informe:

```bash
coverage report -m
```

```bash
pytest --cov=flight_data_module
```
