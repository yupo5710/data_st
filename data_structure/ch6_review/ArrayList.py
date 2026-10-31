class ArrayList:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity
        
        
    def isEmpty(self): #공백검사
        return self.size == 0
    
    def isFull(self): # 포화 검사
        return self.size == self.capacity
    
    def getEntry(self,pos): # 위치 조회
        if 0 <= pos <= self.size:
            return self.array[pos]
        else:
            return None
        
    def insert(self,pos,e): # 삽입 연산
        if not self.isEmpty() and 0 <= pos <= self.size:
            for i in range(self.size,pos,-1): # size 에서 pos 까지 뒤에서 한칸씩
                self.array[i] = self.array[i - 1] # 한칸씩 뒤로 이동
            self.array[pos] = e
            size += 1
        else:
            pass     
    def delete(self,pos): # 삭제 연산
        if not self.isFull() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos,self.size-1):
                self.array[i] = self.array[i + 1]
            size -= 1
            return e
        else:
            pass
    def __str__(self):
            return str(self.array[0:self.size])