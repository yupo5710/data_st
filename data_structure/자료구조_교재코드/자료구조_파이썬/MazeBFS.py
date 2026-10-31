# -*- coding: utf-8 -*-
# 교재의 전역 map, MAZE_SIZE, 방문 표시 '.', 상→하→좌→우 순서를 유지.
# 주의: map은 파이썬 내장 함수 이름과 같지만 교재 이름을 유지함.
from CircularQueue import CircularQueue  # 교재의 원형 큐 사용

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


def BFS():  # 교재 6주차 32쪽의 너비우선탐색 함수
    """출력 제외 시간 O(V+E), 공간 O(V). V=칸 수, E=이웃 관계 수.
    동일 이동 비용에서 BFS는 최단 거리 순서로 탐색함. 경로 복원 코드는 교재에 없음.
    교재의 기본 큐 용량 8(실제 7칸)을 유지. 큰 미로에서는 후보가 누락될 수 있음.
    """
    que = CircularQueue()  # 교재처럼 기본 용량 원형 큐 생성
    que.enqueue((0, 1))  # 입구를 첫 후보로 저장
    print('BFS: ')  # 탐색 이름 출력
    while not que.isEmpty():  # 큐에 후보가 남아 있는 동안 반복
        here = que.dequeue()  # 가장 먼저 넣은 좌표를 꺼냄
        print(here, end='->')  # 현재 방문 좌표 출력
        x, y = here  # 튜플에서 좌표 분리
        if map[y][x] == 'x': return True  # 출구를 찾으면 성공 반환
        else:  # 출구가 아니면 이웃 검사
            map[y][x] = '.'  # 교재처럼 큐에서 꺼낸 뒤 방문 처리
            if isValidPos(x, y - 1): que.enqueue((x, y - 1))  # 위쪽 후보 저장
            if isValidPos(x, y + 1): que.enqueue((x, y + 1))  # 아래쪽 후보 저장
            if isValidPos(x - 1, y): que.enqueue((x - 1, y))  # 왼쪽 후보 저장
            if isValidPos(x + 1, y): que.enqueue((x + 1, y))  # 오른쪽 후보 저장
    return False  # 후보가 없으면 실패


if __name__ == "__main__":  # 직접 실행 시 아래 학습 예제 동작
    result = BFS()  # 교재 미로를 탐색; 전역 map의 통로가 방문 표시로 바뀜
    print("\n탐색 성공:", result)  # 성공 True 또는 실패 False 확인
