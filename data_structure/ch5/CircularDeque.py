# 코드 5.8: 원형 덱: 큐를 상속한 클래스 정의
if __package__:
    from .CircularQueue import CircularQueue
else:
    from CircularQueue import CircularQueue

class CircularDeque(CircularQueue) :
    def __init__( self, capacity=10 ) :
        super().__init__(capacity)

    # 코드 2.4b: 원형 덱: 동작이 동일한 연산들
    def addRear( self, item ):
       self.enqueue(item )

    def deleteFront( self ):
       return self.dequeue()

    def getFront( self ):
       return self.peek()


#================================================================
# Circular Deque에서 새로 구현이 필요한 다음 연산들을 완성한 뒤 실행해보세요
#================================================================

    def addFront( self, item ):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1) % self.capacity

    def deleteRear( self ):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.array[self.rear] = None
            self.rear = (self.rear - 1) % self.capacity
            return item

    def getRear( self ):
        if not self.isEmpty():
            return self.array[self.rear]

    def __str__(self):
        return str([
            self.array[(self.front + 1 + i) % self.capacity]
            for i in range(self.size())
        ])


# 코드 5.9: 원형 덱: 테스트 프로그램
if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i%2==0 : dq.addRear(i)
        else : dq.addFront(i)
    print("홀수->전단, 짝수->후단:", dq)

    for i in range(2): dq.deleteFront()
    for i in range(3): dq.deleteRear()
    print(" 전단삭제x2 후단삭제x3:", dq)

    for i in range(9,14): dq.addFront(i)
    print("   전단삽입 9,10,...13:", dq)
