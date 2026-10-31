# -*- coding: utf-8 -*-
# 출처: 6장 PDF 15~20쪽 (기본 버전)
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
from Node import Node  # 같은 폴더의 클래스를 가져옴


class LinkedStack:  # 관련 데이터와 연산을 하나의 클래스로 묶음
    def __init__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """생성: O(1). 15~20쪽 기본 버전. count 추가 도전 코딩 버전은 아님."""
        self.top = None  # 빈 상태를 나타내도록 노드 참조를 None으로 지정

    def isEmpty(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """공백 검사: O(1)."""
        return self.top == None  # 계산하거나 조회한 결과를 반환

    def isFull(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """포화 검사: O(1)."""
        return False  # 조건을 만족하지 않았음을 반환

    def push(self, item):  # 메서드 정의; self는 현재 객체를 가리킴
        """상단 삽입: O(1)."""
        n = Node(item, self.top)  # 기존 상단을 다음 링크로 갖는 새 노드를 생성
        self.top = n  # 새 노드를 상단으로 지정

    def pop(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """상단 삭제: O(1)."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            n = self.top  # 삭제할 기존 상단 노드를 임시로 참조
            self.top = n.link  # 교재 17쪽 원문: self.top = self.n.link (self.n 오타)
            return n.data  # 계산하거나 조회한 결과를 반환

    def peek(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """상단 조회: O(1)."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            return self.top.data  # 계산하거나 조회한 결과를 반환

    def size(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """노드 수 순회 계산: O(n)."""
        node = self.top  # 순회를 시작할 노드를 참조
        count = 0  # 해당 값을 준비하거나 연산을 실행
        while not node == None:  # 조건을 만족하는 동안 연결된 항목을 계속 확인
            node = node.link  # 단순 연결 링크를 따라 다음 노드로 이동
            count += 1  # 방문한 노드 수를 하나 증가
        return count  # 순회하며 센 노드 수를 반환

    def __str__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """상단부터 문자열 변환: O(n)."""
        arr = []  # 출력할 데이터를 모을 임시 리스트 생성
        node = self.top  # 순회를 시작할 노드를 참조
        while not node == None:  # 조건을 만족하는 동안 연결된 항목을 계속 확인
            arr.append(node.data)  # 현재 노드의 데이터를 임시 리스트 끝에 추가
            node = node.link  # 단순 연결 링크를 따라 다음 노드로 이동
        return str(arr)  # 계산하거나 조회한 결과를 반환


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    s = LinkedStack()  # 해당 값을 준비하거나 연산을 실행
    s.push(10)  # 해당 값을 준비하거나 연산을 실행
    s.push(20)  # 해당 값을 준비하거나 연산을 실행
    print("상단부터:", s)  # 실행 결과를 화면에서 확인
    print("삭제:", s.pop())  # 실행 결과를 화면에서 확인
    print("남은 개수:", s.size())  # 실행 결과를 화면에서 확인
