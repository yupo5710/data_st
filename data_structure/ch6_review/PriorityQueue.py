class PriorityQueue:
    def __init__(self, capacity=10):  # 메서드 정의; self는 현재 객체를 가리킴
        """생성: 시간 O(capacity), 공간 O(capacity)."""
        self.capacity = capacity  # 현재 객체의 저장 값 또는 연결 정보를 갱신
        self.array = [None] * capacity  # 저장 공간을 초기화하거나 사용하지 않는 칸을 비움
        self.size = 0  # 배열에 저장된 실제 항목 수를 0으로 초기화
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def findMaxIndex(self):
        if self.isEmpty(): return -1
        highest = 0
        for i in range(1,self.size):
            if self.array[i] > self.array[highest]:
                highest = i
        return highest
    
    def enqueue(self,e):
        if not self.isFull():
            self.array[self.size] = e
            size += 1
            
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest != -1:
            self.size -= 1
            self.array[highest],self.array[self.size] = self.array[self.size],self.array[highest]
            return self.array[self.size]
    
    def peek(self):
        highest = self.findMaxIndex()
        if highest != -1:
            return self.array[highest]
        