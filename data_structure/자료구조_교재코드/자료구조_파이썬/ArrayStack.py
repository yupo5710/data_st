# -*- coding: utf-8 -*-
# 출처: 5주차 PDF 19~22쪽 및 53쪽 출력 설명
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
class ArrayStack:  # 관련 데이터와 연산을 하나의 클래스로 묶음
    def __init__(self, capacity):  # 메서드 정의; self는 현재 객체를 가리킴
        """생성: 시간 O(capacity), 공간 O(capacity)."""
        self.capacity = capacity  # 현재 객체의 저장 값 또는 연결 정보를 갱신
        self.array = [None] * self.capacity  # 저장 공간을 초기화하거나 사용하지 않는 칸을 비움
        self.top = -1  # 항목이 없는 초기 상단 위치를 -1로 지정

    def isEmpty(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """공백 검사: O(1)."""
        return self.top == -1  # 계산하거나 조회한 결과를 반환

    def isFull(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """포화 검사: O(1)."""
        return self.top == self.capacity - 1  # 계산하거나 조회한 결과를 반환

    def push(self, e):  # 메서드 정의; self는 현재 객체를 가리킴
        """상단 삽입: O(1). LIFO: 나중에 넣은 항목이 먼저 나옴."""
        if not self.isFull():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.top += 1  # 상단 인덱스를 한 칸 올려 새 항목의 자리를 확보
            self.array[self.top] = e  # 확보한 상단 위치에 새 항목 e를 저장
        else: pass  # 조건을 만족하지 않으면 아무 작업 없이 종료

    def pop(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """상단 삭제: O(1). top을 먼저 내리고 이전 상단의 값을 반환."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.top -= 1  # 상단 인덱스를 내려 기존 상단을 논리적으로 제거
            return self.array[self.top + 1]  # 인덱스를 내리기 전의 상단 값을 반환; 배열 칸은 그대로 둠
        else: pass  # 조건을 만족하지 않으면 아무 작업 없이 종료

    def peek(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """상단 조회: O(1)."""
        if not self.isEmpty():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            return self.array[self.top]  # 계산하거나 조회한 결과를 반환
        else: pass  # 조건을 만족하지 않으면 아무 작업 없이 종료

    def __str__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """문자열 변환: O(n). 미로 출력 설명대로 상단부터 슬라이싱하여 표시."""
        return str(self.array[0:self.top + 1][::-1])  # 계산하거나 조회한 결과를 반환


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    s = ArrayStack(3)  # 해당 값을 준비하거나 연산을 실행
    s.push(10)  # 해당 값을 준비하거나 연산을 실행
    s.push(20)  # 해당 값을 준비하거나 연산을 실행
    print("상단부터:", s)  # 실행 결과를 화면에서 확인
    print("상단 조회:", s.peek())  # 실행 결과를 화면에서 확인
    print("삭제:", s.pop())  # 실행 결과를 화면에서 확인
    print("삭제 후:", s)  # 실행 결과를 화면에서 확인
