class Deque:
    def __init__(self):
        # Inicializamos con una lista vacía o con algunos valores iniciales
        self.__deque = [14, 12, 3, 4]  

    def add_first(self, item):
        """Agregar un elemento a la parte inicial del deque (cola)."""
        self.__deque.insert(0, item)
        
    def remove_first(self):
        """Remover y retornar un elemento de la parte inicial del deque (cola)."""
        if self.__deque:
            return self.__deque.pop(0)
        else:
            return "Deque vacío, no se puede remover el primer elemento."
        
    def add_last(self, item):
        """Agregar un elemento a la parte final del deque (cola/pila)."""
        self.__deque.append(item)
        
    def remove_last(self):
        """Remover y retornar un elemento de la parte final del deque (pila)."""
        if self.__deque:
            return self.__deque.pop()
        else:
            return "Deque vacío, no se puede remover el último elemento."
    
    def __str__(self):
        """Imprimir el contenido actual del deque."""
        return str(self.__deque)

deque = Deque()
print("Deque inicial:", deque)

deque.add_first(10)
print("Después de agregar 10 al principio:", deque)

deque.add_last(20)
print("Después de agregar 20 al final:", deque)

deque.remove_first()
print("Después de remover el primer elemento:", deque)

deque.remove_last()
print("Después de remover el último elemento:", deque)
