# PT---Flight-data

  Este proyecto está desarrollado en Python para el desarrollo de datos de vuelos almacenados en archivos JSON, CSV y LOG. Encontraremos funciones para cargar, analizar y combinar los datos pertinentes, así como pruebas unitarias para garantizar el correcto funcionamiento de las funciones implementadas.

-------->>Librerías:
-JSON: para trabajar con datos JSON
-CSV: para leer y escribir archivos CSV
-Logging: para registrar problemas en el .LOG
Estas librerías no hay que instalarlas ya que las proporciona directamente Python.
La única librería que tenemos que instalar es:
-Pytest: el framework para las pruebas unitarias.

-------->>Explicación de cada función:
-"load_data_json": Esta función carga los datos de los vuelos desde un archivo JSON y devuelve una lista de diccionarios y cada diccionario representa un vuelo.

-"load_data_csv": Misma acción que la carga del JSON pero con archivos CSV.

-"parse_log_data": Esta función analiza datos de los vuelos desde un archivo LOG, devolviendo también una lista diccionario donde cada diccionario representa un vuelo.

-"combine_data": Esta función combina los datos de los vuelos de los archivos JSON, CSV y LOG en un solo conjunto de datos. A través del ID del vuelo unifica la información que le pedimos de cada archivo para crear un diccionario para cada vuelo.

Lo que hacemos con el TRY y EXCEPT en cada función anterior es intentar abrir el archivo en modo lectura y si lo encuentra que lo devuelva. En el caso de no encontrar el archivo le pedimos que, a través del logging que hemos configurado, nos devuelva un mensaje dinámico de error al cargar el archivo.

-"calculate_revenue_per_passenger": Esta función calcula los ingresos por pasajeros para cada vuelo a través del "combine_data" y agrega un nuevo valor a cada diccionario de vuelo que representa los ingresos por pasajero.

En esta función de calcular los ingresos por pasajero le pedimos que intente coger los datos de los pasajeros, la duración de minutos y los ingresos y en el caso de venir vacío que lo cambie por un 0 para que no nos dé error. Si los pasajeros son diferentes a 0 que nos haga la división de ingreso / pasajeros y si no que sea 0. En este caso nos piden que no solo diga cuando hay un error si no que nos comunique cada error por lo que declaramos el logging.debug para que nos dé todo el rango de problemas que pueda dar en otro mensaje dinámico.

--------->>Ejecución del programa y de los test unitarios:
  Principalmente tenemos que instalar la librería Pytest
  pip install pytest
  que es la única que no viene con la instalación de Python. 
  El siguiente paso es ejecutar el script de flight_data_module.py en la terminal
  python flight_data_module.py
  para cargar los datos de los vuelos desde los archivos JSON, CSV y LOG, la combinación de ellos y el calculo de ingresos por pasajero.

Para empezar con las pruebas unitarias ponemos en terminal
```pytest```
y detectará automáticamente todas aquellas pruebas que empiecen por la palabra test. 
Hacemos la prueba unitaria de cada archivo para ver que hace una lectura correcta y, para cerciorarnos de su buen funcionamiento, también probamos diferentes escenarios como puede ser un archivo vacío o inválido. Hacemos la prueba para verificar la combinación de datos correctamente.
Por último, hacemos la prueba del cálculo de ingresos por pasajero para cada vuelo y hacemos otra para ver un vuelo concreto y verificar que lo está haciendo correctamente.

