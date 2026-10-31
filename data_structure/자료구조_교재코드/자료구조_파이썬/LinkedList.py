    # -*- coding: utf-8 -*-
# 출처: 6장 PDF 28~32쪽
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
from Node import Node  # 같은 폴더의 클래스를 가져옴


class LinkedList:  # 관련 데이터와 연산을 하나의 클래스로 묶음
    def __init__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """생성: O(1)."""
        self.head = None  # 빈 상태를 나타내도록 노드 참조를 None으로 지정

    def isEmpty(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """공백 검사: O(1)."""
        return self.head == None  # 계산하거나 조회한 결과를 반환

    def isFull(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """포화 검사: O(1)."""
        return False  # 조건을 만족하지 않았음을 반환

    def getNode(self, pos):  # 메서드 정의; self는 현재 객체를 가리킴
        """위치 노드 탐색: 최악 O(n)."""
        if pos < 0: return None  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
        node = self.head  # 순회를 시작할 노드를 참조
        while pos > 0 and node != None:  # 조건을 만족하는 동안 연결된 항목을 계속 확인
            node = node.link  # 단순 연결 링크를 따라 다음 노드로 이동
            pos -= 1  # 해당 값을 준비하거나 연산을 실행
        return node  # 계산하거나 조회한 결과를 반환

    def getEntry(self, pos):  # 메서드 정의; self는 현재 객체를 가리킴
        """위치 값 조회: 최악 O(n)."""
        node = self.getNode(pos)  # 순회를 시작할 노드를 참조
        if node == None: return None  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
        else: return node.data  # 조건이 맞지 않을 때 지정된 값을 반환

    def insert(self, pos, elem):  # 메서드 정의; self는 현재 객체를 가리킴
        """위치 삽입: 최악 O(n), 머리 삽입 O(1). 연결 자체는 O(1)."""
        before = self.getNode(pos - 1)  # 대상 위치 바로 앞 노드를 찾음; 없으면 None
        if before == None:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.head = Node(elem, self.head)  # 현재 객체의 저장 값 또는 연결 정보를 갱신
        else:  # 위 조건을 만족하지 않는 경우를 처리
            node = Node(elem, before.link)  # 기존 다음 노드로 연결되는 새 노드를 생성
            before.link = node  # 이전 노드가 새 노드를 가리키도록 연결

    def delete(self, pos):  # 메서드 정의; self는 현재 객체를 가리킴
        """위치 삭제: 최악 O(n), 머리 삭제 O(1). 교재처럼 값 반환은 없음."""
        before = self.getNode(pos - 1)  # 대상 위치 바로 앞 노드를 찾음; 없으면 None
        if before == None:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            if self.head is not None:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
                self.head = self.head.link  # 머리를 다음 노드로 옮겨 첫 노드를 제외
        elif before.link != None:  # 해당 값을 준비하거나 연산을 실행
            before.link = before.link.link  # 해당 값을 준비하거나 연산을 실행

    def size(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """노드 수 계산: O(n)."""
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


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    s = LinkedList()  # 해당 값을 준비하거나 연산을 실행
    s.insert(0, 10)  # 해당 값을 준비하거나 연산을 실행
    s.insert(1, 30)  # 해당 값을 준비하거나 연산을 실행
    s.insert(1, 20)  # 해당 값을 준비하거나 연산을 실행
    print("삽입 결과:", s)  # 실행 결과를 화면에서 확인
    print("1번 위치:", s.getEntry(1))  # 실행 결과를 화면에서 확인
    s.delete(1)  # 해당 값을 준비하거나 연산을 실행
    print("삭제 후:", s)  # 실행 결과를 화면에서 확인
    print("개수:", s.size())  # 실행 결과를 화면에서 확인
