# Linked List.
class Node:
    def __init__ (self, elem, next=None):
        self.data = elem 
        self.link = next

# 코드 6.5: 연결리스트 클래스
class LinkedList:
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    def __init__( self ):
        self.head = None

    # 리스트의 연산: 클래스의 메소드
    def isEmpty( self ): return self.head == None
    def isFull( self ): return False

# getNode(), getEntry(), 

    def getNode(self, pos) :
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
            return node

    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None : return None
        else:return node.data
    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
    def delete(self, pos) :

    def size( self ) :

    def __str__( self ) :
        arr = []
        node = self.head
        while node is not None :
            arr.append(node.data)
            node = node.link
        return str(arr)
    

    def replace(self, pos, elem) :

    def find(self, val) :


#======================================================================
if __name__ == "__main__":
    L = LinkedList()
    
    print("최초   ", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(3, 40)
    L.insert(2, 50)
    print("삽입x5 ", L)
    L.delete(2)
    print("삭제(2)", L)
    L.delete(3)
    print("삭제(3)", L)
    L.delete(0)
    print("삭제(0)", L)

