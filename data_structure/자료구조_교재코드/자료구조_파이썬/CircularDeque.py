# -*- coding: utf-8 -*-
# 출처: 6주차 PDF 43~44쪽
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
from CircularQueue import CircularQueue  # 같은 폴더의 클래스를 가져옴


class CircularDeque(CircularQueue):  # 관련 데이터와 연산을 하나의 클래스로 묶음
    """부모의 isEmpty/isFull/size는 O(1), __str__은 O(n)."""
    def __init__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """부모 생성자 호출: O(capacity), 기본 capacity=8."""
        super().__init__()  # 부모 클래스의 초기화 기능을 실행

    def addRear(self, item):  # 메서드 정의; self는 현재 객체를 가리킴
        """후단 삽입: O(1)."""
        self.enqueue(item)  # 부모 큐의 후단 삽입 연산을 재사용

    def deleteFront(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단 삭제: O(1)."""
        return self.dequeue()  # 계산하거나 조회한 결과를 반환

    def getFront(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단 조회: O(1)."""
        return self.peek()  # 계산하거나 조회한 결과를 반환

    def addFront(self, item):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단 삽입: O(1)."""
        if not self.isFull():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.array[self.front] = item  # 첫 항목 직전의 빈 칸에 새 전단 항목 저장
            self.front = (self.front - 1 + self.capacity) % self.capacity  # 전단 경계를 한 칸 뒤로 이동; 0 이전은 배열 끝으로 회전
        else: pass  # 조건을 만족하지 않으면 아무 작업 없이 종료

    def deleteRear(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """후단 삭제: O(1)."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            item = self.array[self.rear]  # 삭제 또는 반환 전에 항목 값을 따로 보관
            self.rear = (self.rear - 1 + self.capacity) % self.capacity  # 후단을 한 칸 뒤로 이동; 0 이전은 배열 끝으로 회전
            return item  # 보관해 둔 항목을 호출한 곳으로 반환
        else: pass  # 조건을 만족하지 않으면 아무 작업 없이 종료

    def getRear(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """후단 조회: O(1)."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            return self.array[self.rear]  # 계산하거나 조회한 결과를 반환
        else: pass  # 조건을 만족하지 않으면 아무 작업 없이 종료


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    d = CircularDeque()  # 해당 값을 준비하거나 연산을 실행
    d.addRear(20)  # 해당 값을 준비하거나 연산을 실행
    d.addFront(10)  # 해당 값을 준비하거나 연산을 실행
    d.addRear(30)  # 해당 값을 준비하거나 연산을 실행
    print("덱:", d)  # 실행 결과를 화면에서 확인
    print("앞/뒤 조회:", d.getFront(), d.getRear())  # 실행 결과를 화면에서 확인
    print("앞 삭제:", d.deleteFront())  # 실행 결과를 화면에서 확인
    print("뒤 삭제:", d.deleteRear())  # 실행 결과를 화면에서 확인
    print("남은 덱:", d)  # 실행 결과를 화면에서 확인
