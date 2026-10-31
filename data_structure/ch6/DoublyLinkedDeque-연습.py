

# 코드 6.9: 이중연결구조의 노드 클래스
class DNode:
    def __init__ (self, elem, prev, next):
        self.data = elem 
        self.prev = prev
        self.next = next


# 코드 6.10: 이중연결구조로 구현한 덱
class DoublyLinkedDeque:
    def __init__( self ):
        self.front = None
        self.rear = None

    def isEmpty( self ): return self.front == None
    def isFull( self ): return False


#== addFront(), addRear(), deleteFront(), deleteRear() 구현하세요

#    def addFront( self, item ):

#    def addRear( self, item ):

#    def deleteFront( self ):

#    def deleteRear( self ):

    def __str__( self ) :
        arr = []
        node = self.front
        while not node == None :
            arr.append(node.data)
            node = node.next
        return str(arr)

#======================================================================
if __name__ == "__main__":
    dq = DoublyLinkedDeque()

    for i in range(9):
        if i%2==0 : dq.addRear(i)
        else : dq.addFront(i)
    print("홀수->전단, 짝수->후단:", dq)

    for i in range(2): dq.deleteFront()
    for i in range(3): dq.deleteRear()
    print(" 전단삭제x2 후단삭제x3:", dq)

    for i in range(9,14): dq.addFront(i)
    print("   전단삽입 9,10,...13:", dq)

