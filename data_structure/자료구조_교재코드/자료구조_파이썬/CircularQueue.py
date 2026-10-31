# -*- coding: utf-8 -*-
# 출처: 6주차 PDF 27쪽
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
class CircularQueue:  # 관련 데이터와 연산을 하나의 클래스로 묶음
    def __init__(self, capacity=8):  # 메서드 정의; self는 현재 객체를 가리킴
        """생성: O(capacity). 실제 최대 항목 수는 capacity-1."""
        self.capacity = capacity  # 현재 객체의 저장 값 또는 연결 정보를 갱신
        self.array = [None] * capacity  # 저장 공간을 초기화하거나 사용하지 않는 칸을 비움
        self.front = 0  # 현재 객체의 저장 값 또는 연결 정보를 갱신
        self.rear = 0  # 현재 객체의 저장 값 또는 연결 정보를 갱신

    def isEmpty(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """공백 검사: O(1)."""
        return self.front == self.rear  # 계산하거나 조회한 결과를 반환

    def isFull(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """포화 검사: O(1)."""
        return self.front == (self.rear + 1) % self.capacity  # 계산하거나 조회한 결과를 반환

    def enqueue(self, item):  # 메서드 정의; self는 현재 객체를 가리킴
        """후단 삽입: O(1)."""
        if not self.isFull():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.rear = (self.rear + 1) % self.capacity  # 후단을 한 칸 전진; 배열 끝에서는 0번으로 회전
            self.array[self.rear] = item  # 전진한 후단 위치에 새 항목 저장

    def dequeue(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단 삭제: O(1)."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.front = (self.front + 1) % self.capacity  # 전단을 한 칸 전진시켜 첫 항목 위치로 이동
            return self.array[self.front]  # 계산하거나 조회한 결과를 반환

    def peek(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단 조회: O(1)."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            return self.array[(self.front + 1) % self.capacity]  # 계산하거나 조회한 결과를 반환

    def size(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """항목 수 계산: O(1)."""
        return (self.rear - self.front + self.capacity) % self.capacity  # 계산하거나 조회한 결과를 반환

    def __str__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """전단부터 문자열 변환: O(n)."""
        if self.front < self.rear:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            return str(self.array[self.front + 1:self.rear + 1])  # 계산하거나 조회한 결과를 반환
        else:  # 위 조건을 만족하지 않는 경우를 처리
            return str(self.array[self.front + 1:self.capacity] + self.array[0:self.rear + 1])  # 계산하거나 조회한 결과를 반환


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    q = CircularQueue(4)  # 해당 값을 준비하거나 연산을 실행
    for value in [10, 20, 30]:  # 지정 범위의 항목 또는 위치를 차례로 방문
        q.enqueue(value)  # 해당 값을 준비하거나 연산을 실행
    print("가득 참:", q.isFull())  # 실행 결과를 화면에서 확인
    print("삭제:", q.dequeue())  # 실행 결과를 화면에서 확인
    q.enqueue(40)  # 해당 값을 준비하거나 연산을 실행
    print("원형 회전 후:", q)  # 실행 결과를 화면에서 확인
    print("전단:", q.peek())  # 실행 결과를 화면에서 확인
