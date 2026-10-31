from DNode import DNode


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def isFull(self):
        return False

    def getNode(self, pos):
        if pos < 0:
            return None

        node = self.head
        while pos > 0 and node is not None:
            node = node.next
            pos -= 1
        return node

    def insert(self, pos, elem):
        # 삽입 위치: 0부터 size()까지
        if pos < 0:
            raise IndexError("잘못된 삽입 위치입니다.")

        if pos == 0:
            node = DNode(elem, None, self.head)

            if self.head is not None:
                self.head.prev = node

            self.head = node

        else:
            before = self.getNode(pos - 1)
            if before is None:
                raise IndexError("잘못된 삽입 위치입니다.")

            after = before.next
            node = DNode(elem, before, after)

            before.next = node
            if after is not None:
                after.prev = node

    def delete(self, pos):
        node = self.getNode(pos)
        if node is None:
            raise IndexError("잘못된 삭제 위치입니다.")

        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        return node.data

    def size(self):
        node = self.head
        count = 0

        while node is not None:
            count += 1
            node = node.next

        return count

    def __str__(self):
        arr = []
        node = self.head

        while node is not None:
            arr.append(node.data)
            node = node.next

        return str(arr)