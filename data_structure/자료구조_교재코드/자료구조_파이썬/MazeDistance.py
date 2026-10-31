# -*- coding: utf-8 -*-
# 교재의 전역 map, MAZE_SIZE, 방문 표시 '.', 상→하→좌→우 순서를 유지.
# 주의: map은 파이썬 내장 함수 이름과 같지만 교재 이름을 유지함.
from PriorityQueueMaze import PriorityQueueMaze as PriorityQueue  # 56쪽 거리 비교 버전을 사용
import math  # 교재처럼 제곱근 계산에 사용

MAZE_SIZE = 6  # 교재 예제의 한 변 길이
map = [  # 1=벽, 0=통로, 'e'=입구, 'x'=출구
    [1, 1, 1, 1, 1, 1],  # 첫 번째 행
    ['e', 0, 1, 0, 0, 1],  # 입구는 (0, 1)
    [1, 0, 0, 0, 1, 1],  # 세 번째 행
    [1, 0, 1, 0, 1, 1],  # 네 번째 행
    [1, 0, 1, 0, 0, 'x'],  # 출구는 (5, 4); PDF 설명의 (5, 3)은 배열과 불일치
    [1, 1, 1, 1, 1, 1],  # 마지막 행
]


def isValidPos(x, y):  # 갈 수 있는 칸인지 검사하는 공통 함수
    """시간 O(1). 좌표는 (x,y), 배열은 map[y][x]로 접근."""
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:  # 범위 안인지 검사
        if map[y][x] == 0 or map[y][x] == 'x':  # 교재 원문: '0'; 미로 배열의 정수 0에 맞춘 오타 수정
            return True  # 아직 방문하지 않은 통로 또는 출구이면 허용
    return False  # 범위 밖, 벽, 방문한 칸은 제외


(ox, oy) = (5, 4)  # 교재 55쪽의 출구 좌표


def dist(x, y):  # 현재 위치에서 출구까지의 직선거리 계산
    """시간 O(1). 유클리드 거리; 누적 이동거리는 아님."""
    (dx, dy) = (ox - x, oy - y)  # 출구와 현재 위치의 좌표 차이
    return math.sqrt(dx * dx + dy * dy)  # 피타고라스 정리로 거리 계산


def MySmartSearch():  # 교재 57쪽의 전략적 미로 탐색 함수
    """시간 최악 O(V^2+E), 공간 O(V). V=칸 수, E=이웃 관계 수.
    정렬하지 않은 배열에서 최고 우선순위 탐색 O(n)을 반복. 최단 경로 보장 없음.
    교재의 기본 우선순위 큐 용량 10 유지. 큰 미로에는 용량 제한이 있음.
    """
    q = PriorityQueue()  # 교재의 우선순위 큐 생성
    q.enqueue((0, 1, -dist(0, 1)))  # 시작 좌표와 음수 거리 저장
    print('PQueue: ')  # 탐색 이름 출력
    while not q.isEmpty():  # 후보가 있는 동안 반복
        here = q.dequeue()  # -거리가 가장 큰, 즉 출구와 가장 가까운 후보 선택
        print(here[0:2], end='->')  # 좌표만 출력하고 우선순위 값은 생략
        x, y, _ = here  # 좌표를 분리하고 우선순위 값은 사용하지 않음
        if map[y][x] == 'x': return True  # 출구에 도달하면 성공
        else:  # 출구가 아니면 이웃을 확인
            map[y][x] = '.'  # 교재처럼 꺼낸 뒤 방문 처리
            if isValidPos(x, y - 1): q.enqueue((x, y - 1, -dist(x, y - 1)))  # 위쪽 후보와 우선순위
            if isValidPos(x, y + 1): q.enqueue((x, y + 1, -dist(x, y + 1)))  # 아래쪽 후보와 우선순위
            if isValidPos(x - 1, y): q.enqueue((x - 1, y, -dist(x - 1, y)))  # 왼쪽 후보와 우선순위
            if isValidPos(x + 1, y): q.enqueue((x + 1, y, -dist(x + 1, y)))  # 오른쪽 후보와 우선순위
            print('우선순위큐: ', q.array)  # 교재 원문: q.items; 50쪽 저장 속성은 array
    return False  # 출구를 찾지 못한 경우 실패


if __name__ == "__main__":  # 직접 실행 시 아래 학습 예제 동작
    result = MySmartSearch()  # 교재 미로를 탐색; 전역 map의 통로가 방문 표시로 바뀜
    print("\n탐색 성공:", result)  # 성공 True 또는 실패 False 확인
