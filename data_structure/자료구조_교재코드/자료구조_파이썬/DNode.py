# -*- coding: utf-8 -*-
# 출처: 6장 PDF 49쪽
# n=현재 항목 수; 원소 비교·대입·원소별 문자열 변환은 O(1)로 가정.
class DNode:  # 관련 데이터와 연산을 하나의 클래스로 묶음
    def __init__(self, elem, prev=None, next=None):  # 메서드 정의; self는 현재 객체를 가리킴
        """이중 연결 노드 생성: 시간·공간 O(1)."""
        self.data = elem  # 노드가 보관할 데이터 저장
        self.prev = prev  # 이전 노드를 가리키는 링크 저장
        self.next = next  # 다음 노드를 가리키는 링크 저장


if __name__ == "__main__":  # 직접 실행할 때만 학습 예제 실행
    first = DNode(10)  # 해당 값을 준비하거나 연산을 실행
    second = DNode(20, first)  # 해당 값을 준비하거나 연산을 실행
    first.next = second  # 해당 값을 준비하거나 연산을 실행
    print("다음 노드:", first.next.data)  # 실행 결과를 화면에서 확인
    print("이전 노드:", second.prev.data)  # 실행 결과를 화면에서 확인
