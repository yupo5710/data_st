# 5.20

class QueueTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def isEmpty(self):
        return not self.stack1 and not self.stack2

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        # 출력 스택이 비어 있으면 입력 스택의 요소를 모두 이동
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return None

        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return None

        return self.stack2[-1]

    def size(self):
        return len(self.stack1) + len(self.stack2)


if __name__ == "__main__":
    Q = QueueTwoStacks()

    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)

    print(Q.dequeue())  # 1
    print(Q.dequeue())  # 2

    Q.enqueue(4)
    Q.enqueue(5)

    while not Q.isEmpty():
        print(Q.dequeue())  # 3, 4, 5 순서로 출력