from lab4.src.utils import File


class Node:
    def __init__(self, val: int, next=None) -> None:
        """Node: Это класс для узла связного списка (длиной одного элемента).
            val: Значение, которое будет храниться в узле (целое число).
            next: Указатель на следующий узел в списке.
                По умолчанию устанавливается в None, что означает,
                что этот узел не указывает на следующий узел (он последний в списке)."""
        self.val = val
        self.next = next



class LinkedList:
    def __init__(self, root) -> None:
        """self.root: Сохраняет корень (первый узел) в списке."""
        self.root = root

    def append(self, val: int) -> None:
        """ Добавление элемента в конец связного списка
        Создаем временную переменную tmp, указывающую на self.root (первый узел).
        С помощью цикла while проходим по всему списку, пока tmp.next не станет None, что означает, что мы достигли конца списка.
        Создаем новый узел с val и присоединяем его к tmp.next, тем самым добавляя его в конец списка."""
        tmp = self.root
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val=val)

    def output(self):
        tmp = self.root
        while tmp:
            print(tmp.val, end = " ")
            tmp = tmp.next



    def is_empty(self) -> bool:
        tmp = self.root
        if tmp is None:
            return True
        else:
            return False

    def pop_end(self):
        tmp = self.root
        while tmp.next.next:
            tmp = tmp.next
        tmp.next = None


ll = LinkedList(root=None)
print(ll.is_empty())
root = Node(10)
ll = LinkedList(root=root)
ll.append(13)
ll.append(12)
ll.output()
print()
ll.pop_end()
ll.output()