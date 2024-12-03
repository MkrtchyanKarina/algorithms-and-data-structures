from lab4.src.utils import File


class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next



class LinkedList:
    def __init__(self, root) -> None:
        self.root = root

    def append(self, val: int) -> None:
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