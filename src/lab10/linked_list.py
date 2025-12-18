from typing import Any, Optional, Iterator


class Node:
    # Создаем узел
    
    def __init__(self, value: Any) -> None:
        
        self.value: Any = value  # Значение, хранящееся в узле
        self.next: Optional['Node'] = None  # Ссылка на следующий узел, изначально None
    
    def __repr__(self) -> str: # Показываем свои стринги
        
        return f"Node({self.value})"


class SinglyLinkedList:
    # Создаем из узлов цепочку
    
    def __init__(self) -> None: # Пустой по умолчанию

        self.head: Optional[Node] = None  
        self.tail: Optional[Node] = None  
        self._size: int = 0  
    
    def append(self, value: Any) -> None: # Добавим в конец
        
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:  # Добавим в  начало
        
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None: # Засунем по индексу
       
        if idx < 0 or idx > self._size:
            raise IndexError(f"{idx} вне зоны доступа [0, {self._size}]")
        
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        new_node = Node(value)
        current = self.head
        
        for _ in range(idx - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        
        self._size += 1
    
    def remove_at(self, idx: int) -> None: # Затираем по индексу
        
        if self.head is None:
            raise IndexError("Список пустой, че тут удалять то")
        
        if idx < 0 or idx >= self._size:
            raise IndexError(f"{idx} вне зоны доступа [0, {self._size - 1}]")
        
        if idx == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        current = self.head
        
        for _ in range(idx - 1):         # Проходим до узла перед удаляемым
            current = current.next
        
        current.next = current.next.next # Пропускаем удаляемый узел
        
        if current.next is None:
            self.tail = current
        
        self._size -= 1
    
    def remove(self, value: Any) -> bool: # Трем первое вхождение указанного значения
        
        if self.head is None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        current = self.head # Поиск элемента в середине или конце списка
        
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
            
                if current.next is None:
                    self.tail = current
                
                self._size -= 1
                return True
            
            current = current.next
        
        return False
    
    def __iter__(self) -> Iterator[Any]: # Итератор по значениям в спиське
        
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int: # Показываем сколько всего 
        
        return self._size
    
    def __repr__(self) -> str: # Выдаем список стрингами
        
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def visual_repr(self) -> str: # Рисуем поезд как в ТЗ
        
        parts = []
        current = self.head
        
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        
        parts.append("None")
        
        return " -> ".join(parts)
    
    def get_at(self, idx: int) -> Any: # Смотрим по индексу что в узле за дата
        
        if idx < 0 or idx >= self._size:
            raise IndexError(f"{idx} вне зоны доступа [0, {self._size - 1}]")
        
        current = self.head
        
        for _ in range(idx):
            current = current.next
        
        return current.value
    
    def is_empty(self) -> bool: # Чек на пустоту
        
        return self._size == 0
    
    def clear(self) -> None: # Затираем все 
        
        self.head = None
        self.tail = None
        self._size = 0


# Тестируем
if __name__ == "__main__":
    print("~~~~Тестируем SinglyLinkedList~~~~")
    
    sll = SinglyLinkedList()
    print(f"Создали пустой список: {sll}")
    print(f"Визуальное представление: {sll.visual_repr()}")
    print(f"Длина списка: {len(sll)}")
    print(f"Список пуст? {sll.is_empty()}")
    
    print("\n~~~~Добавляем элементы в конец (append)~~~~")
    sll.append(10)
    sll.append(20)
    sll.append(30)
    print(f"Список после append: {sll}")
    print(f"Визуальное представление: {sll.visual_repr()}")
    print(f"Длина списка: {len(sll)}")
    
    print("\n~~~~Добавляем элементы в начало (prepend)~~~~")
    sll.prepend(5)
    sll.prepend(1)
    print(f"Список после prepend: {sll}")
    print(f"Визуальное представление: {sll.visual_repr()}")
    print(f"Длина списка: {len(sll)}")
    
    print("\n~~~~Вставляем элементы по индексу (insert)~~~~")
    sll.insert(2, 7)
    print(f"Вставили 7 на позицию 2: {sll}")
    print(f"Визуальное представление: {sll.visual_repr()}")
    
    sll.insert(0, 0)
    print(f"Вставили 0 на позицию 0: {sll}")
    print(f"Визуальное представление: {sll.visual_repr()}")
    
    sll.insert(len(sll), 40)
    print(f"Вставили 40 в конец: {sll}")
    print(f"Визуальное представление: {sll.visual_repr()}")
    
    print("\n~~~~Получаем элементы по индексу (get_at)~~~~")
    for i in range(len(sll)):
        print(f"Элемент на позиции {i}: {sll.get_at(i)}")
    
    print("\n~~~~Удаляем элементы по значению (remove)~~~~")
    print(f"Удаляем 7: {sll.remove(7)}")
    print(f"Список после удаления 7: {sll}")
    print(f"Визуальное представление: {sll.visual_repr()}")
    
    print(f"Удаляем 100 (не существует): {sll.remove(100)}")
    print(f"Список без изменений: {sll}")
    
    print("\n~~~~Удаляем элементы по индексу (remove_at)~~~~")
    sll.remove_at(0)
    print(f"Удалили элемент на позиции 0: {sll}")
    print(f"Визуальное представление: {sll.visual_repr()}")
    
    sll.remove_at(2)
    print(f"Удалили элемент на позиции 2: {sll}")
    print(f"Визуальное представление: {sll.visual_repr()}")
    
    print("\n~~~~Итерируемся по списку~~~~")
    print("Элементы списка:")
    for value in sll:
        print(f"  {value}")
    
    print("\n~~~~Тестируем с разными типами данных~~~~")
    mixed_list = SinglyLinkedList()
    mixed_list.append("строка")
    mixed_list.append(123)
    mixed_list.append(3.14)
    mixed_list.append([1, 2, 3])
    mixed_list.append({"key": "value"})
    print(f"Смешанный список: {mixed_list}")
    print(f"Визуальное представление: {mixed_list.visual_repr()}")
    
    print("\n~~~~Тестируем исключения~~~~")
    empty_list = SinglyLinkedList()
    
    try:
        empty_list.remove_at(0)
    except IndexError as e:
        print(f"Ошибка при удалении из пустого списка: {e}")
    
    try:
        empty_list.get_at(0)
    except IndexError as e:
        print(f"Ошибка при получении элемента из пустого списка: {e}")
    
    try:
        sll.insert(100, 999)
    except IndexError as e:
        print(f"Ошибка при вставке с неверным индексом: {e}")
    
    print("\n~~~~Очищаем список~~~~")
    sll.clear()
    print(f"Список после очистки: {sll}")
    print(f"Визуальное представление: {sll.visual_repr()}")
    print(f"Длина списка: {len(sll)}")
    print(f"Список пуст? {sll.is_empty()}")