class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, root: Node) -> None:
        self.root = root

    def prepend(self, val: any) -> None:
        new_node = Node(val)
        tmp = self.root
        new_node.next = tmp  # Сделаем новый узел первым
        self.root = new_node  # Обновляем корень списка

    def popleft(self) -> None:
        tmp = self.root
        tmp = tmp.next
        self.root = tmp

    def output(self) -> None:
        tmp = self.root
        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.next

    def search(self, key: any) -> bool:
        tmp = self.root
        while tmp:
            if tmp.val == key:
                return True
            tmp = tmp.next
        return False

    def insert_after(self, key: any, value: any) -> None:
        tmp = self.root
        while tmp:
            if tmp.val == key:
                new_node = Node(value)
                new_node.next = tmp.next
                tmp.next = new_node
                break
            tmp = tmp.next

    def delete_after(self, key):
        tmp = self.root
        while tmp:
            if tmp.val == key:
                if tmp.next:
                    tmp.next = tmp.next.next
                else:
                    break
            tmp = tmp.next






root = Node(1)
ll = LinkedList(root=root)
ll.prepend(19)
ll.prepend(12)
ll.prepend('hello')
ll.output()
print(ll.search('hello'))
print()
ll.popleft()
ll.popleft()
ll.output()
print(ll.search('hello'))
ll.insert_after(1, 2)
ll.insert_after(19, 8)
ll.output()
print()
ll.delete_after(19)
ll.output()