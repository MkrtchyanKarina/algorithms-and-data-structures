class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)  # Добавляем новый элемент в конец
        self.bubble_up(len(self.heap) - 1)  # Поднимаем элемент до правильной позиции

    def bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            # Обмен значений между дочерним и родительским узлом
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.bubble_up(parent_index)  # Продолжаем подъем для родительского узла

    def build_heap(self, elements):
        self.heap = elements[:]  # Копируем элементы в кучу
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Находим меньший из текущего, левого и правого дочерних узлов
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # Если самый маленький элемент не является родительским
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)  # Продолжаем обрабатывать

    def __str__(self):
        return str(self.heap)


# Пример использования
if __name__ == "__main__":
    elements = [5, 4, 3, 2, 1]

    # Создаем пирамиду
    heap = MinHeap()
    heap.build_heap(elements)
    print("Неубывающая пирамида:", heap)
