from Node import Node


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def isFull(self):
        return False

    def enqueue(self, item):
        node = Node(item, None)

        if self.isEmpty():
            self.front = node
        else:
            self.rear.link = node

        self.rear = node

    def dequeue(self):
        if self.isEmpty():
            return None

        data = self.front.data
        self.front = self.front.link

        # 마지막 원소를 삭제했다면 rear도 비움
        if self.front is None:
            self.rear = None

        return data

    def peek(self):
        if not self.isEmpty():
            return self.front.data

    def size(self):
        node = self.front
        count = 0

        while node is not None:
            count += 1
            node = node.link

        return count

    def __str__(self):
        arr = []
        node = self.front

        while node is not None:
            arr.append(node.data)
            node = node.link

        return str(arr)