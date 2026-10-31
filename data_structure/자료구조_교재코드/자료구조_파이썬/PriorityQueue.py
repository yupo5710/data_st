# -*- coding: utf-8 -*-
# 출처: 6주차 PDF 50~51쪽
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
class PriorityQueue:  # 관련 데이터와 연산을 하나의 클래스로 묶음
    def __init__(self, capacity=10):  # 메서드 정의; self는 현재 객체를 가리킴
        """생성: 시간 O(capacity), 공간 O(capacity)."""
        self.capacity = capacity  # 현재 객체의 저장 값 또는 연결 정보를 갱신
        self.array = [None] * capacity  # 저장 공간을 초기화하거나 사용하지 않는 칸을 비움
        self.size = 0  # 배열에 저장된 실제 항목 수를 0으로 초기화

    def isEmpty(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """공백 검사: O(1). 기본 상태 검사 식을 사용."""
        return self.size == 0  # 계산하거나 조회한 결과를 반환

    def isFull(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """포화 검사: O(1). 기본 상태 검사 식을 사용."""
        return self.size == self.capacity  # 계산하거나 조회한 결과를 반환

    def findMaxIndex(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """가장 큰 값의 위치 탐색: O(n). 빈 경우 -1."""
        if self.isEmpty(): return -1  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
        highest = 0  # 해당 값을 준비하거나 연산을 실행
        for i in range(1, self.size):  # 지정 범위의 항목 또는 위치를 차례로 방문
            if self.array[i] > self.array[highest]:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
                highest = i  # 더 높은 우선순위를 가진 항목의 위치로 갱신
        return highest  # 계산하거나 조회한 결과를 반환

    def enqueue(self, e):  # 메서드 정의; self는 현재 객체를 가리킴
        """정렬 없이 맨 뒤 삽입: O(1)."""
        if not self.isFull():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.array[self.size] = e  # 사용 중인 마지막 칸 바로 뒤에 새 항목 저장
            self.size += 1  # 실제 항목 수를 하나 증가

    def dequeue(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """최대 원소를 마지막 원소와 교환한 뒤 삭제: O(n)."""
        highest = self.findMaxIndex()  # 해당 값을 준비하거나 연산을 실행
        if highest != -1:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.size -= 1  # 실제 항목 수를 하나 감소; 배열 칸을 지우지는 않음
            self.array[highest], self.array[self.size] = self.array[self.size], self.array[highest]  # 최대 항목과 마지막 항목을 교환하여 최대 항목을 사용 범위 밖으로 이동
            return self.array[self.size]  # 계산하거나 조회한 결과를 반환

    def peek(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """최대 원소 조회: O(n)."""
        highest = self.findMaxIndex()  # 해당 값을 준비하거나 연산을 실행
        if highest != -1:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            return self.array[highest]  # 계산하거나 조회한 결과를 반환


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    q = PriorityQueue()  # 해당 값을 준비하거나 연산을 실행
    for value in [34, 18, 27, 45, 15]:  # 지정 범위의 항목 또는 위치를 차례로 방문
        q.enqueue(value)  # 해당 값을 준비하거나 연산을 실행
    print("최대값 조회:", q.peek())  # 실행 결과를 화면에서 확인
    while not q.isEmpty():  # 조건을 만족하는 동안 연결된 항목을 계속 확인
        print("높은 우선순위부터:", q.dequeue())  # 실행 결과를 화면에서 확인
