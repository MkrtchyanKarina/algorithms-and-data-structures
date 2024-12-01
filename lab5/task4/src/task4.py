import typing as tp


class MinHeap:
    def __init__(self, array_len: int, array: tp.List[int]) -> None:
        self.heap = array
        self.high = array_len
        self.swaps = []

    def heap_sort(self) -> (int, tp.List[tp.Tuple[int]]):
        for i in range(self.high // 2 - 1, -1, -1):
            self.swap(i)
        return len(self.swaps), self.swaps

    def swap(self, index: int) -> None:
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.high and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < self.high and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swaps += [(index, smallest)]
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.swap(smallest)

    @staticmethod
    def limits(array_len: int, array: tp.List[int]) -> bool:
        if 1 <= array_len <= 10**5 and len(array) == array_len and all(0 <= a <= 10**9 for a in array):
            return True
        else:
            return False


if __name__ == "__main__":
    elements = [5, 4, 3, 2, 1]
    heap = MinHeap(5, elements).heap_sort()
    print(heap)