# 코드 6.1: 단순연결노드 클래스
class Node:
    def __init__ (self, elem, link=None):
        self.data = elem 
        self.link = link

# 코드 6.2: 연결된 스택 클래스
class LinkedStack :
    def __init__( self ):
        self.top = None

# isEmpty(), push(), pop(), peek()l, size(), 다음을 구현하세요 

    def isEmpty( self ):
        return self.top == None
    def push( self, item ):
        n = Node(item,self.top)
        self.top = n
    def peek( self ):
        if not self.isEmpty():
            return self.top.data
    def pop( self ):
        if not self.isEmpty():
            n = self.top
            self.top = self.n.link
            return n.data
    def size( self ):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count


    def __str__(self):
        arr = []
        node = self.top
        while not node == None :
            arr.append(node.data)
            node = node.link
        return str(arr)



#======================================================================
if __name__ == "__main__":
    s = LinkedStack()             # 스택 객체를 생성

    print("스택: ", s)
    msg = input("문자열 입력: ")    # 문자열을 입력받음
    for c in msg :                  # 문자열의 각 문자 c에 대해
        s.push(c)                   # c를 스택에 삽입

    print("스택: ", s)

    print("문자열 출력: ", end='')
    while not s.isEmpty():          # 스택이 공백상태가 아니라면
        print(s.pop(), end='')      # 하나의 요소를 꺼내서 출력
    print()
    print("스택: ", s)

