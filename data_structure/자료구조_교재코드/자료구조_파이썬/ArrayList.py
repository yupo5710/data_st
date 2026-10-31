# -*- coding: utf-8 -*-
# 출처: 3주차 PDF 32~35쪽
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
class ArrayList:  # 관련 데이터와 연산을 하나의 클래스로 묶음
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

    def getEntry(self, pos):  # 메서드 정의; self는 현재 객체를 가리킴
        """위치 조회: O(1)."""
        if 0 <= pos < self.size:  # 교재 원문: 0 <= ps < self.size (ps 오타)
            return self.array[pos]  # 계산하거나 조회한 결과를 반환
        else: return None  # 조건이 맞지 않을 때 지정된 값을 반환

    def insert(self, pos, e):  # 메서드 정의; self는 현재 객체를 가리킴
        """삽입: 최악 O(n), 맨 뒤 O(1)."""
        if not self.isFull() and 0 <= pos <= self.size:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            for i in range(self.size, pos, -1):  # 지정 범위의 항목 또는 위치를 차례로 방문
                self.array[i] = self.array[i - 1]  # 뒤에서부터 한 칸씩 오른쪽으로 밀어 삽입 공간 확보
            self.array[pos] = e  # 이동으로 확보한 pos 위치에 새 항목 저장
            self.size += 1  # 실제 항목 수를 하나 증가
        else: pass  # 조건을 만족하지 않으면 아무 작업 없이 종료

    def delete(self, pos):  # 메서드 정의; self는 현재 객체를 가리킴
        """삭제: 최악 O(n), 맨 뒤 O(1)."""
        if not self.isEmpty() and 0 <= pos < self.size:  # 현재 상태를 검사하여 필요한 경우에만 아래 연산 실행
            e = self.array[pos]  # 해당 값을 준비하거나 연산을 실행
            for i in range(pos, self.size - 1):  # 지정 범위의 항목 또는 위치를 차례로 방문
                self.array[i] = self.array[i + 1]  # 이후 항목을 한 칸씩 왼쪽으로 당겨 삭제 공간 제거
            self.size -= 1  # 실제 항목 수를 하나 감소; 배열 칸을 지우지는 않음
            return e  # 계산하거나 조회한 결과를 반환
        else: pass  # 조건을 만족하지 않으면 아무 작업 없이 종료

    def __str__(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """문자열 변환: O(n)."""
        return str(self.array[0:self.size])  # 계산하거나 조회한 결과를 반환


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    s = ArrayList()  # 해당 값을 준비하거나 연산을 실행
    s.insert(0, 10)  # 해당 값을 준비하거나 연산을 실행
    s.insert(0, 20)  # 해당 값을 준비하거나 연산을 실행
    s.insert(1, 30)  # 해당 값을 준비하거나 연산을 실행
    print("삽입 결과:", s)  # 실행 결과를 화면에서 확인
    print("1번 위치:", s.getEntry(1))  # 실행 결과를 화면에서 확인
    print("삭제한 값:", s.delete(1))  # 실행 결과를 화면에서 확인
    print("삭제 후:", s)  # 실행 결과를 화면에서 확인
    print("개수 속성:", s.size)  # 실행 결과를 화면에서 확인
