# Desarrollo de Actividades

# Clase Deque
La clase `Deque` en Python, permite manipular elementos en una doble cola (deque) utilizando operaciones para agregar y remover elementos tanto al inicio como al final.

## Implementación
La clase `Deque` contiene los siguientes métodos:

- `__init__(self)`: Inicializa el deque con una lista de valores predeterminados.
- `add_first(self, item)`: Agrega un elemento al inicio del deque.
- `remove_first(self)`: Remueve y retorna el primer elemento del deque.
- `add_last(self, item)`: Agrega un elemento al final del deque.
- `remove_last(self)`: Remueve y retorna el último elemento del deque.
- `__str__(self)`: Devuelve una representación en cadena del deque actual.

# Cambio Limitado de Monedas

**Objetivo**: Desarrollar una función para distribuir una cantidad específica de dinero utilizando un conjunto limitado de monedas disponibles, priorizando las de mayor denominación.

**Función Principal**: `cambio_moneda2`, que recibe monedas disponibles y la cantidad a cambiar, devolviendo cómo se debe distribuir el cambio utilizando la menor cantidad de monedas posibles.

**Pasos**:
1. Inicializar las monedas.
2. Calcular el cambio priorizando las monedas de mayor denominación.
3. Verificar la disponibilidad de las monedas.
4. Devolver la distribución de monedas o indicar imposibilidad de cambio.

**Uso**: Este algoritmo se utilizó para proporcionar cambio de manera eficiente con un conjunto limitado de monedas, ayudando a optimizar las transacciones y la distribución de dinero en situaciones prácticas.

**Recursos de Python Aplicados**:
1. **Listas**: Para almacenar y manejar las monedas disponibles y la cantidad a cambiar.
2. **Bucles For**: Para iterar sobre las monedas disponibles y calcular la distribución del cambio.
3. **Funciones**: Para encapsular la lógica de distribución de cambio y hacerla reutilizable.
4. **Condicionales**: Para verificar la disponibilidad de las monedas y manejar situaciones en las que no se puede dar el cambio exacto.


# Algoritmo de Kadane

**Objetivo**: Implementar el Algoritmo de Kadane para encontrar la suma máxima de un subarreglo contiguo dentro de una matriz unidimensional de enteros.

**Función Principal**: `maximum_subarray`, que recibe una lista de enteros y devuelve la suma máxima de un subarreglo contiguo.

**Pasos**:
1. Inicializar `max_current` y `max_global` con el primer elemento de la lista.
2. Iterar sobre los elementos restantes de la lista.
3. Actualizar `max_current` al máximo entre el elemento actual y la suma de `max_current` con el elemento actual.
4. Si `max_current` es mayor que `max_global`, actualizar `max_global`.
5. Devolver `max_global` como la suma máxima del subarreglo contiguo.

**Uso**: Este algoritmo se utilizó para encontrar la suma máxima de subarreglos contiguos en una lista de enteros, ayudando a identificar la subsecuencia de mayor suma posible en problemas de optimización y análisis de datos.

**Recursos de Python Aplicados**:
1. **Listas**: Para almacenar y manejar los números en la matriz unidimensional.
2. **Bucles For**: Para iterar sobre los elementos de la lista y actualizar las variables `max_current` y `max_global`.
3. **Funciones**: Para encapsular la lógica del Algoritmo de Kadane y hacerla reutilizable.
4. **Comparaciones**: Para actualizar los valores de `max_current` y `max_global` utilizando la función `max`.

# Solución del Laberinto con Backtracking

**Objetivo**: Implementar una solución para encontrar un camino en un laberinto desde la posición inicial (0, 0) hasta la meta (N-1, N-1) utilizando la técnica de backtracking.

**Función Principal**: `solve_maze`, que recibe una matriz binaria representando el laberinto y devuelve la ruta desde la entrada hasta la salida si existe.

**Pasos**:
1. **Inicializar la matriz**: Representar el laberinto como una matriz binaria.
2. **Definir funciones auxiliares**:
   - `is_safe(x, y)`: Verifica si la posición (x, y) es segura para moverse.
   - `dfs(x, y)`: Implementa la búsqueda en profundidad (DFS) con backtracking para encontrar el camino.
3. **Marcar celdas visitadas**: Para evitar ciclos durante la búsqueda.
4. **Backtrack**: Retrocede si no encuentra un camino, desmarcando las celdas visitadas.
5. **Devolver la ruta**: Si se encuentra un camino, devolver la ruta; si no, indicar que no hay camino disponible.

**Uso**: Este algoritmo se utilizó para resolver el problema del laberinto, encontrando una ruta desde la entrada hasta la salida, lo cual es útil en problemas de navegación y búsqueda de caminos.

**Recursos de Python Aplicados**:
1. **Listas**: Para representar el laberinto y almacenar la ruta.
2. **Funciones**: Para definir la lógica del algoritmo de backtracking y las funciones auxiliares.
3. **Recursión**: Para implementar la búsqueda en profundidad (DFS) con backtracking.
4. **Condicionales**: Para verificar las condiciones de movimiento seguro y determinar cuándo retroceder en el backtracking.
