from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False
    
    def getNode(self,pos):
        
        if pos < 0:return None
        node = self.head
        
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
        
    def insert(self,pos,elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem,self.head)
            
        else:
            node = Node(elem,before.link)
            before.link = node
            
    def delete(self,pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link
            
    def size(self):
        node = self.head  # 순회를 시작할 노드를 참조
        count = 0  # 해당 값을 준비하거나 연산을 실행
        while node is not None:  # 조건을 만족하는 동안 연결된 항목을 계속 확인
            node = node.link  # 단순 연결 링크를 따라 다음 노드로 이동
            count += 1  # 방문한 노드 수를 하나 증가
        return count  # 순회하며 센 노드 수를 반환


    def __str__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """머리부터 문자열 변환: O(n)."""
        arr = []  # 출력할 데이터를 모을 임시 리스트 생성
        node = self.head  # 순회를 시작할 노드를 참조
        while node is not None:  # 조건을 만족하는 동안 연결된 항목을 계속 확인
            arr.append(node.data)  # 현재 노드의 데이터를 임시 리스트 끝에 추가
            node = node.link  # 단순 연결 링크를 따라 다음 노드로 이동
        return str(arr)  # 계산하거나 조회한 결과를 반환
    # 6.12: 앞에서부터 출력
    def printForward(self):
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.link
        print()

    # 6.13: 재귀를 이용해 역순 출력
    def printReverse(self):
        self._printReverse(self.head)
        print()

    def _printReverse(self, node):
        if node is None:
            return
        self._printReverse(node.link)
        print(node.data, end=" ")

    # 6.14: 맨 끝에 추가
    def append(self, elem):
        node = Node(elem, None)

        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.link is not None:
                last = last.link
            last.link = node

    # 6.15: A의 맨 뒤에 B를 연결하고 B를 비움
    def merge(self, B):
        if B is self:
            raise ValueError("자기 자신과 병합할 수 없습니다.")

        if self.head is None:
            self.head = B.head
        else:
            last = self.head
            while last.link is not None:
                last = last.link
            last.link = B.head

        B.head = None