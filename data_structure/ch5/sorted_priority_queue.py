#  5.23

class SortedPriorityQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

    def size(self):
        return self.count

    def enqueue(self, item):
        if self.isFull():
            return

        # 삽입할 값보다 큰 요소들을 오른쪽으로 이동
        i = self.count - 1

        while i >= 0 and self.array[i] > item:
            self.array[i + 1] = self.array[i]
            i -= 1

        self.array[i + 1] = item
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return None

        # 최댓값은 항상 마지막 위치에 있음
        self.count -= 1
        item = self.array[self.count]
        self.array[self.count] = None
        return item

    def peek(self):
        if self.isEmpty():
            return None

        return self.array[self.count - 1]

    def __str__(self):
        return str(self.array[:self.count])


if __name__ == "__main__":
    Q = SortedPriorityQueue()

    for item in [34, 18, 27, 45, 15]:
        Q.enqueue(item)

    print("정렬된 배열:", Q)

    while not Q.isEmpty():
        print("최고 우선순위:", Q.dequeue())