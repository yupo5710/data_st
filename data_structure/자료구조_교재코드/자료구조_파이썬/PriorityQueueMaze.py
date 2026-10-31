# -*- coding: utf-8 -*-
# 출처: 6주차 PDF 56쪽 비교 방식
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
from PriorityQueue import PriorityQueue  # 같은 폴더의 클래스를 가져옴


class PriorityQueueMaze(PriorityQueue):  # 관련 데이터와 연산을 하나의 클래스로 묶음
    """교재 56쪽의 미로용 비교 버전. 중복 클래스명 구분을 위해 파일·클래스명만 구별."""
    def findMaxIndex(self):  # 메서드 정의; self는 현재 객체를 가리킴
        """튜플의 세 번째 값(-거리) 최대 위치: O(n)."""
        if self.isEmpty(): return -1  # 교재 원문: return None; 51쪽 dequeue의 -1 검사와 불일치
        else:  # 위 조건을 만족하지 않는 경우를 처리
            highest = 0  # 해당 값을 준비하거나 연산을 실행
            for i in range(1, self.size):  # 교재 원문: self.size(); 50쪽에서는 size가 정수 속성
                if self.array[i][2] > self.array[highest][2]:  # 교재 원문: self.items[i][2] > self.items[highest][2]
                    highest = i  # 더 높은 우선순위를 가진 항목의 위치로 갱신
            return highest  # 계산하거나 조회한 결과를 반환


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    q = PriorityQueueMaze()  # 해당 값을 준비하거나 연산을 실행
    q.enqueue((1, 1, -5.0))  # 해당 값을 준비하거나 연산을 실행
    q.enqueue((2, 1, -3.0))  # 해당 값을 준비하거나 연산을 실행
    q.enqueue((3, 1, -1.0))  # 해당 값을 준비하거나 연산을 실행
    while not q.isEmpty():  # 조건을 만족하는 동안 연결된 항목을 계속 확인
        print("출구와 가까운 항목부터:", q.dequeue())  # 실행 결과를 화면에서 확인
