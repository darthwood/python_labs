from collections import deque
from typing import Any, Optional


class Stack:

    
    def __init__(self) -> None:
        
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None: #Добавить что-то наверх стека
        
        self._data.append(item)
    
    def pop(self) -> Any: #Затираем верхний элемент стека и показываем его
        
        if self.is_empty():
            raise IndexError("Стек пустой, тут ничего нет")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]: #Просто покажем верхний элемент, или скажем что там пусто
        
        return self._data[-1] if not self.is_empty() else None
    
    def is_empty(self) -> bool: #Проверяем пустой ли стек
        
        return len(self._data) == 0
    
    def __len__(self) -> int: #Считаем сколько там всего
        
        return len(self._data)
    

    def remove_at(self, index: int) -> Any: # Трем элемент по индексу
        
        if index < 0:
            # Преобразуем отрицательный индекс в положительный
            index = len(self._data) + index
            
        if 0 <= index < len(self._data):
            # Удаляем элемент по индексу
            return self._data.pop(index)
        else:
            raise IndexError(f"{index} слишком большое число для нашего стека (Он ващет: {len(self._data)})")
    
    def replace_at(self, index: int, new_item: Any) -> None: #Заменяем по индексу
        
        if index < 0:
            # Преобразуем отрицательный индекс в положительный
            index = len(self._data) + index
            
        if 0 <= index < len(self._data):
            # Заменяем элемент по индексу
            self._data[index] = new_item
        else:
            raise IndexError(f"{index} слишком велик для этого стека (Величина его: {len(self._data)})")
    
    def insert_at(self, index: int, item: Any) -> None: #Засовываем элемент по индексу
        
        if index < 0:
            # Преобразуем отрицательный индекс в положительный
            index = len(self._data) + index
            
        if 0 <= index <= len(self._data):
            # Вставляем элемент по индексу
            self._data.insert(index, item)
        else:
            raise IndexError(f"{index} нарушает все допустимые пределы (0-{len(self._data)})")
    
    def get_at(self, index: int) -> Any: # Получим элемент по индексу
        
        if index < 0:
            # Преобразуем отрицательный индекс в положительный
            index = len(self._data) + index
            
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexError(f"{index} слишком велик для этого стека (Величина его: {len(self._data)})")
    
    def clear(self) -> None: # Затираем все к такой-то
        
        self._data.clear()
    
    def reverse(self) -> None: # Разворачиваем выворот нашиворот
        
        self._data.reverse()
    
    def __str__(self) -> str: # Представляем в строковом виде
       
        return f"Stack({self._data})" 


class Queue:
    
    
    def __init__(self) -> None: #Инит пустой очереди
        
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None: #Добавляем элемент в конец очереди
        
        self._data.append(item)
    
    def dequeue(self) -> Any: #Трем элемент из начала очереди и показываем его
        
        if self.is_empty():
            raise IndexError("Очередь пуста, тут ничего нет")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]: #Показываем первый элемент в очереди
        
        return self._data[0] if not self.is_empty() else None
    
    def is_empty(self) -> bool: # Чек на вшивость
        
        return len(self._data) == 0
    
    def __len__(self) -> int: #Считаем сколько там всего
        
        return len(self._data)
    
    
    def remove_at(self, index: int) -> Any: # Затираем по индексу
        
        if index < 0:
            # Преобразуем отрицательный индекс в положительный
            index = len(self._data) + index
            
        if 0 <= index < len(self._data):
            # Создаем временный список, удаляем элемент и обновляем очередь
            temp_list = list(self._data)
            removed_item = temp_list.pop(index)
            self._data = deque(temp_list)
            return removed_item
        else:
            raise IndexError(f"{index} больше чем всего элементов в очереди (Стоит: {len(self._data)})")
    
    def replace_at(self, index: int, new_item: Any) -> None: # Заменяем по индексу
        
        if index < 0:
            # Преобразуем отрицательный индекс в положительный
            index = len(self._data) + index
            
        if 0 <= index < len(self._data):
            # deque не поддерживает замену по индексу напрямую, используем временный список
            temp_list = list(self._data)
            temp_list[index] = new_item
            self._data = deque(temp_list)
        else:
            raise IndexError(f"{index} больше чем всего элементов в очереди (Стоит: {len(self._data)})")
    
    def insert_at(self, index: int, item: Any) -> None: # Плаг ин нью девайс по индексу
        
        if index < 0:
            # Преобразуем отрицательный индекс в положительный
            index = len(self._data) + index
            
        if 0 <= index <= len(self._data):
            # deque имеет метод insert, но он менее эффективен для больших индексов
            # Вместо этого используем временный список
            temp_list = list(self._data)
            temp_list.insert(index, item)
            self._data = deque(temp_list)
        else:
            raise IndexError(f"Индекс {index} выходит за допустимые пределы (0-{len(self._data)})")
    
    def get_at(self, index: int) -> Any: # Показываем элемент по индексу
        
        if index < 0:
            # Преобразуем отрицательный индекс в положительный
            index = len(self._data) + index
            
        if 0 <= index < len(self._data):
            # deque поддерживает индексацию как список
            return self._data[index]
        else:
            raise IndexError(f"{index} больше чем всего элементов в очереди (Стоит: {len(self._data)})")
    
    def clear(self) -> None: # Всех почикаем
        
        self._data.clear()
    
    def rotate(self, n: int = 1) -> None: # Перетаскиваем из конца в начало (если n отрицательное) и наоборот
        
        self._data.rotate(-n)  # deque.rotate работает наоборот: положительное - вправо
    
    def reverse(self) -> None: #Разворачиваем очередь наизнанку
        # Преобразуем deque в список, разворачиваем и создаем новый deque
        self._data = deque(reversed(self._data))
    
    def __str__(self) -> str: # Показываем очередь в
        
        return f"Queue({list(self._data)})"


# Пример использования
if __name__ == "__main__":
    print("~~~~Тестируем Stack~~~~")
    stack = Stack()
    
    print(f"Стек пуст? {stack.is_empty()}")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Стек: {stack}")
    print(f"Размер стека: {len(stack)}")
    
    print(f"Верхний элемент: {stack.peek()}")
    print(f"Трем элемент: {stack.pop()}")
    print(f"Стек после затирки: {stack}")
    print(f"Стек пуст? {stack.is_empty()}")
    
    print("\n~~~~Тестируем дополнительные методы Stack~~~~")
    # Тестируем get_at
    print(f"Элемент по индексу 0 (дно стека): {stack.get_at(0)}")
    print(f"Элемент по индексу -1 (вершина): {stack.get_at(-1)}")
    
    # Тестируем remove_at
    stack.push(33)
    stack.push(44)
    print(f"\nДобавили 33 и 44 в стек: {stack}")
    print(f"Удаляем элемент по индексу 1: {stack.remove_at(1)}")
    print(f"Стек после удаления: {stack}")
    
    # Тестируем replace_at
    print(f"\nЗаменяем элемент по индексу 0 на 999")
    stack.replace_at(0, 999)
    print(f"Стек после замены: {stack}")
    
    # Тестируем insert_at
    print(f"\nВставляем 777 по индексу 1")
    stack.insert_at(1, 777)
    print(f"Стек после вставки: {stack}")
    
    # Тестируем reverse
    print(f"\nРазворачиваем стек")
    stack.reverse()
    print(f"Стек после разворота: {stack}")
    
    # Тестируем clear
    print(f"\nОчищаем стек")
    stack.clear()
    print(f"Стек после очистки: {stack}")
    print(f"Стек пуст? {stack.is_empty()}")
    
    print("\n~~~~Тестируем КУ Е КУ Е~~~~")
    queue = Queue()
    
    print(f"Очередь пуста? {queue.is_empty()}")
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    print(f"Очередь: {queue}")
    print(f"Размер очереди: {len(queue)}")
    
    print(f"Первый элемент: {queue.peek()}")
    print(f"Трем элемент: {queue.dequeue()}")
    print(f"Очередь после затирки: {queue}")
    print(f"Очередь пуста? {queue.is_empty()}")
    
    print("\n~~~~Тестируем дополнительные методы Queue~~~~")
    # Добавляем еще элементов
    queue.enqueue("d")
    queue.enqueue("e")
    queue.enqueue("f")
    print(f"Добавили d, e, f: {queue}")
    
    # Тестируем get_at
    print(f"\nЭлемент по индексу 0 (начало): {queue.get_at(0)}")
    print(f"Элемент по индексу -1 (конец): {queue.get_at(-1)}")
    
    # Тестируем remove_at
    print(f"\nУдаляем элемент по индексу 2: {queue.remove_at(2)}")
    print(f"Очередь после удаления: {queue}")
    
    # Тестируем replace_at
    print(f"\nЗаменяем элемент по индексу 1 на 'XXX'")
    queue.replace_at(1, 'XXX')
    print(f"Очередь после замены: {queue}")
    
    # Тестируем insert_at
    print(f"\nВставляем 'YYY' по индексу 1")
    queue.insert_at(1, 'YYY')
    print(f"Очередь после вставки: {queue}")
    
    # Тестируем rotate
    print(f"\nПеремещаем 2 элемента из начала в конец")
    queue.rotate(2)
    print(f"Очередь после rotate: {queue}")
    
    # Тестируем reverse
    print(f"\nРазворачиваем очередь")
    queue.reverse()
    print(f"Очередь после разворота: {queue}")
    
    # Тестируем clear
    print(f"\nОчищаем очередь")
    queue.clear()
    print(f"Очередь после очистки: {queue}")
    print(f"Очередь пуста? {queue.is_empty()}")
    
    print("\n~~~~Тестируем исключения~~~~")
    empty_stack = Stack()
    empty_queue = Queue()
    
    try:
        empty_stack.pop()
    except IndexError as e:
        print(f"Ошибка стека при pop(): {e}")
    
    try:
        empty_stack.get_at(0)
    except IndexError as e:
        print(f"Ошибка стека при get_at(): {e}")
    
    try:
        empty_queue.dequeue()
    except IndexError as e:
        print(f"Ошибка очереди при dequeue(): {e}")
    
    try:
        empty_queue.get_at(5)
    except IndexError as e:
        print(f"Ошибка очереди при get_at(): {e}")
    
    print("\n~~~~Тестируем с разными типами данных~~~~")
    mixed_stack = Stack()
    mixed_stack.push("строка")
    mixed_stack.push(123)
    mixed_stack.push(3.14)
    mixed_stack.push([1, 2, 3])
    mixed_stack.push({"ключ": "значение"})
    print(f"Стек с разными типами: {mixed_stack}")
    print(f"Извлекаем: {mixed_stack.pop()}")
    print(f"Теперь стек: {mixed_stack}")
    
    mixed_queue = Queue()
    mixed_queue.enqueue(True)
    mixed_queue.enqueue(None)
    mixed_queue.enqueue((1, 2, 3))
    print(f"\nОчередь с разными типами: {mixed_queue}")
    print(f"Извлекаем: {mixed_queue.dequeue()}")
    print(f"Теперь очередь: {mixed_queue}")   