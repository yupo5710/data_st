# -*- coding: utf-8 -*-
# 출처: 3주차 PDF 48~53쪽
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
class ArraySet:  # 관련 데이터와 연산을 하나의 클래스로 묶음
    # 생성자·상태 검사·문자열 변환은 48쪽의 'ArrayList와 비슷한 배열 구조' 설명에 따라 구성.
    def __init__(self, capacity=100):  # 메서드 정의; self는 현재 객체를 가리킴
        """생성: 시간 O(capacity), 공간 O(capacity)."""
        self.capacity = capacity  # 현재 객체의 저장 값 또는 연결 정보를 갱신
        self.array = [None] * capacity  # 저장 공간을 초기화하거나 사용하지 않는 칸을 비움
        self.size = 0  # 배열에 저장된 실제 항목 수를 0으로 초기화

    def isEmpty(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """공백 검사: O(1)."""
        return self.size == 0  # 계산하거나 조회한 결과를 반환

    def isFull(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """포화 검사: O(1)."""
        return self.size == self.capacity  # 계산하거나 조회한 결과를 반환

    def contains(self, e):  # 메서드 정의; self는 현재 객체를 가리킴
        """순차 탐색: O(n)."""
        for i in range(self.size):  # 지정 범위의 항목 또는 위치를 차례로 방문
            if self.array[i] == e:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
                return True  # 조건을 만족했음을 반환
        return False  # 조건을 만족하지 않았음을 반환

    def insert(self, e):  # 메서드 정의; self는 현재 객체를 가리킴
        """중복 검사 후 삽입: O(n)."""
        if not self.contains(e) and not self.isFull():  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            self.array[self.size] = e  # 사용 중인 마지막 칸 바로 뒤에 새 항목 저장
            self.size += 1  # 실제 항목 수를 하나 증가

    def delete(self, e):  # 메서드 정의; self는 현재 객체를 가리킴
        """원소 검색 후 마지막 원소로 교체: O(n)."""
        for i in range(self.size):  # 지정 범위의 항목 또는 위치를 차례로 방문
            if self.array[i] == e:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
                self.array[i] = self.array[self.size - 1]  # 집합은 순서가 없으므로 마지막 원소로 삭제 위치를 채움
                self.size -= 1  # 실제 항목 수를 하나 감소; 배열 칸을 지우지는 않음
                return  # 해당 값을 준비하거나 연산을 실행

    def union(self, setB):  # 메서드 정의; self는 현재 객체를 가리킴
        """합집합: O((n+m)^2), 기본 결과 배열 생성 비용 별도 O(capacity)."""
        setC = ArraySet()  # 결과를 담을 기본 용량의 빈 집합 생성
        for i in range(self.size):  # 지정 범위의 항목 또는 위치를 차례로 방문
            setC.insert(self.array[i])  # 교재처럼 중복 검사 함수를 거쳐 결과 집합에 삽입
        for i in range(setB.size):  # 지정 범위의 항목 또는 위치를 차례로 방문
            if not setC.contains(setB.array[i]):  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
                setC.insert(setB.array[i])  # 교재처럼 중복 검사 함수를 거쳐 결과 집합에 삽입
        return setC  # 계산하거나 조회한 결과를 반환

    def intersect(self, setB):  # 메서드 정의; self는 현재 객체를 가리킴
        """교집합: O(n*m+n^2), n=m일 때 O(n^2). 결과 배열 생성 비용 별도."""
        setC = ArraySet()  # 결과를 담을 기본 용량의 빈 집합 생성
        for i in range(self.size):  # 지정 범위의 항목 또는 위치를 차례로 방문
            if setB.contains(self.array[i]):  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
                setC.insert(self.array[i])  # 교재처럼 중복 검사 함수를 거쳐 결과 집합에 삽입
        return setC  # 계산하거나 조회한 결과를 반환

    def difference(self, setB):  # 메서드 정의; self는 현재 객체를 가리킴
        """차집합: O(n*m+n^2), n=m일 때 O(n^2). 결과 배열 생성 비용 별도."""
        setC = ArraySet()  # 결과를 담을 기본 용량의 빈 집합 생성
        for i in range(self.size):  # 지정 범위의 항목 또는 위치를 차례로 방문
            if not setB.contains(self.array[i]):  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
                setC.insert(self.array[i])  # 교재처럼 중복 검사 함수를 거쳐 결과 집합에 삽입
        return setC  # 계산하거나 조회한 결과를 반환

    def __str__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """문자열 변환: O(n)."""
        return str(self.array[0:self.size])  # 계산하거나 조회한 결과를 반환


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    a = ArraySet(5)  # 해당 값을 준비하거나 연산을 실행
    b = ArraySet(5)  # 해당 값을 준비하거나 연산을 실행
    for value in [1, 2, 2, 3]:  # 지정 범위의 항목 또는 위치를 차례로 방문
        a.insert(value)  # 해당 값을 준비하거나 연산을 실행
    for value in [3, 4]:  # 지정 범위의 항목 또는 위치를 차례로 방문
        b.insert(value)  # 해당 값을 준비하거나 연산을 실행
    print("A:", a, "B:", b)  # 실행 결과를 화면에서 확인
    print("합집합:", a.union(b))  # 실행 결과를 화면에서 확인
    print("교집합:", a.intersect(b))  # 실행 결과를 화면에서 확인
    print("차집합:", a.difference(b))  # 실행 결과를 화면에서 확인
    a.delete(2)  # 해당 값을 준비하거나 연산을 실행
    print("2 삭제:", a)  # 실행 결과를 화면에서 확인
