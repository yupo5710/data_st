from Node import Node


class LinkedQueue:  # 관련 데이터와 연산을 하나의 클래스로 묶음
    def __init__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """원형 연결 큐 생성: O(1)."""
        self.tail = None  # 빈 상태를 나타내도록 노드 참조를 None으로 지정

    def isEmpty(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """공백 검사: O(1)."""
        return self.tail == None  # 계산하거나 조회한 결과를 반환

    def isFull(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """포화 검사: O(1)."""
        return False  # 조건을 만족하지 않았음을 반환

    def enqueue(self, item):  # 메서드 정의; self는 현재 객체를 가리킴
        """후단 삽입: O(1)."""
        node = Node(item, None)  # 데이터와 연결 정보를 담은 새 노드 생성
        if self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.tail = node  # 새 노드를 꼬리로 지정
            node.link = node  # 유일한 노드가 자기 자신을 가리키도록 원형 연결
        else:  # 위 조건을 만족하지 않는 경우를 처리
            node.link = self.tail.link  # 새 노드의 다음을 기존 머리 노드로 연결
            self.tail.link = node  # 기존 꼬리의 다음을 새 노드로 연결
            self.tail = node  # 새 노드를 꼬리로 지정

    def dequeue(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단 삭제: O(1)."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            data = self.tail.link.data  # 해당 값을 준비하거나 연산을 실행
            if self.tail.link == self.tail:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
                self.tail = None  # 빈 상태를 나타내도록 노드 참조를 None으로 지정
            else:  # 위 조건을 만족하지 않는 경우를 처리
                self.tail.link = self.tail.link.link  # 꼬리가 두 번째 노드를 가리키게 하여 전단 노드를 제외
            return data  # 계산하거나 조회한 결과를 반환

    def size(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """원형 순회로 개수 계산: O(n)."""
        if self.isEmpty(): return 0  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
        else:  # 위 조건을 만족하지 않는 경우를 처리
            count = 1  # 해당 값을 준비하거나 연산을 실행
            node = self.tail.link  # 꼬리 다음에 있는 머리 노드를 참조
            while not node == self.tail:  # 조건을 만족하는 동안 연결된 항목을 계속 확인
                node = node.link  # 단순 연결 링크를 따라 다음 노드로 이동
                count += 1  # 방문한 노드 수를 하나 증가
            return count  # 순회하며 센 노드 수를 반환

    def __str__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단부터 문자열 변환: O(n). 44쪽 왼쪽 버전."""
        arr = []  # 출력할 데이터를 모을 임시 리스트 생성
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            node = self.tail.link  # 꼬리 다음에 있는 머리 노드를 참조
            while not node == self.tail:  # 조건을 만족하는 동안 연결된 항목을 계속 확인
                arr.append(node.data)  # 현재 노드의 데이터를 임시 리스트 끝에 추가
                node = node.link  # 단순 연결 링크를 따라 다음 노드로 이동
            arr.append(node.data)  # 현재 노드의 데이터를 임시 리스트 끝에 추가
        return str(arr)  # 계산하거나 조회한 결과를 반환


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    q = LinkedQueue()  # 해당 값을 준비하거나 연산을 실행
    for value in [10, 20, 30]:  # 지정 범위의 항목 또는 위치를 차례로 방문
        q.enqueue(value)  # 해당 값을 준비하거나 연산을 실행
    print("전단부터:", q)  # 실행 결과를 화면에서 확인
    print("삭제:", q.dequeue())  # 실행 결과를 화면에서 확인
    print("삭제 후:", q)  # 실행 결과를 화면에서 확인
    print("개수:", q.size())  # 실행 결과를 화면에서 확인