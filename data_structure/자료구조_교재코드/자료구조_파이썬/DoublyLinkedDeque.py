# -*- coding: utf-8 -*-
# 출처: 6장 PDF 49~52쪽
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
from DNode import DNode  # 같은 폴더의 클래스를 가져옴


class DoublyLinkedDeque:  # 관련 데이터와 연산을 하나의 클래스로 묶음
    def __init__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """생성: O(1)."""
        self.front = None  # 빈 상태를 나타내도록 노드 참조를 None으로 지정
        self.rear = None  # 빈 상태를 나타내도록 노드 참조를 None으로 지정

    def isEmpty(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """공백 검사: O(1)."""
        return self.front == None  # 계산하거나 조회한 결과를 반환

    def addFront(self, item):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단 삽입: O(1)."""
        node = DNode(item, None, self.front)  # 데이터와 연결 정보를 담은 새 노드 생성
        if self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.front = self.rear = node  # 첫 노드이므로 전단과 후단이 모두 같은 노드를 가리킴
        else:  # 위 조건을 만족하지 않는 경우를 처리
            self.front.prev = node  # 기존 머리의 이전 링크를 새 노드로 연결
            self.front = node  # 새 노드를 전단으로 지정

    def addRear(self, item):  # 메서드 정의; self는 현재 객체를 가리킴
        """후단 삽입: O(1). 51쪽 '전단 삽입과 비슷함' 설명으로 구성."""
        node = DNode(item, self.rear, None)  # 데이터와 연결 정보를 담은 새 노드 생성
        if self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.front = self.rear = node  # 첫 노드이므로 전단과 후단이 모두 같은 노드를 가리킴
        else:  # 위 조건을 만족하지 않는 경우를 처리
            self.rear.next = node  # 기존 꼬리의 다음 링크를 새 노드로 연결
            self.rear = node  # 새 노드를 후단으로 지정

    def deleteFront(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단 삭제: O(1)."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            data = self.front.data  # 해당 값을 준비하거나 연산을 실행
            self.front = self.front.next  # 머리를 다음 노드로 옮겨 기존 머리를 제외
            if self.front == None:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
                self.rear = None  # 빈 상태를 나타내도록 노드 참조를 None으로 지정
            else:  # 위 조건을 만족하지 않는 경우를 처리
                self.front.prev = None  # 새 머리 앞의 연결을 끊음
            return data  # 계산하거나 조회한 결과를 반환

    def deleteRear(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """후단 삭제: O(1). 52쪽 전단 삭제와 후단 삭제 설명을 결합."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            data = self.rear.data  # 해당 값을 준비하거나 연산을 실행
            self.rear = self.rear.prev  # 꼬리를 이전 노드로 옮겨 기존 꼬리를 제외
            if self.rear == None:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
                self.front = None  # 빈 상태를 나타내도록 노드 참조를 None으로 지정
            else:  # 위 조건을 만족하지 않는 경우를 처리
                self.rear.next = None  # 새 꼬리 뒤의 연결을 끊음
            return data  # 계산하거나 조회한 결과를 반환

    def getFront(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단 조회: O(1). 50쪽 설명에 따라 데이터 반환."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            return self.front.data  # 계산하거나 조회한 결과를 반환

    def getRear(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """후단 조회: O(1). 50쪽 설명에 따라 데이터 반환."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            return self.rear.data  # 계산하거나 조회한 결과를 반환

    def size(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """노드 수 계산: O(n). 50쪽 설명대로 연결 스택의 순회 사용."""
        node = self.front  # 순회를 시작할 노드를 참조
        count = 0  # 해당 값을 준비하거나 연산을 실행
        while not node == None:  # 조건을 만족하는 동안 연결된 항목을 계속 확인
            node = node.next  # 이중 연결 링크를 따라 다음 노드로 이동
            count += 1  # 방문한 노드 수를 하나 증가
        return count  # 순회하며 센 노드 수를 반환

    def __str__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단부터 문자열 변환: O(n). 50쪽 설명대로 연결 스택의 순회 사용."""
        arr = []  # 출력할 데이터를 모을 임시 리스트 생성
        node = self.front  # 순회를 시작할 노드를 참조
        while not node == None:  # 조건을 만족하는 동안 연결된 항목을 계속 확인
            arr.append(node.data)  # 현재 노드의 데이터를 임시 리스트 끝에 추가
            node = node.next  # 이중 연결 링크를 따라 다음 노드로 이동
        return str(arr)  # 계산하거나 조회한 결과를 반환


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    d = DoublyLinkedDeque()  # 해당 값을 준비하거나 연산을 실행
    d.addRear(20)  # 해당 값을 준비하거나 연산을 실행
    d.addFront(10)  # 해당 값을 준비하거나 연산을 실행
    d.addRear(30)  # 해당 값을 준비하거나 연산을 실행
    print("덱:", d)  # 실행 결과를 화면에서 확인
    print("앞/뒤 조회:", d.getFront(), d.getRear())  # 실행 결과를 화면에서 확인
    print("앞 삭제:", d.deleteFront())  # 실행 결과를 화면에서 확인
    print("뒤 삭제:", d.deleteRear())  # 실행 결과를 화면에서 확인
    print("남은 덱:", d)  # 실행 결과를 화면에서 확인
