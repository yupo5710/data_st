# 5.19 미로탐색 (스택과 큐를 사용하여)

from queue import LifoQueue, Queue


def isValidPos(maze, x, y, visited):
    return (
        0 <= y < len(maze)
        and 0 <= x < len(maze[y])
        and maze[y][x] in ('0', 'e', 'x')
        and (x, y) not in visited
    )


# 깊이우선탐색: 스택 사용
def DFS(maze, start):
    S = LifoQueue()
    S.put(start)
    visited = {start}

    while not S.empty():
        x, y = S.get()
        print((x, y), end=' ')

        if maze[y][x] == 'x':
            return True

        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy

            if isValidPos(maze, nx, ny, visited):
                visited.add((nx, ny))
                S.put((nx, ny))

    return False


# 너비우선탐색: 큐 사용
def BFS(maze, start):
    Q = Queue()
    Q.put(start)
    visited = {start}

    while not Q.empty():
        x, y = Q.get()
        print((x, y), end=' ')

        if maze[y][x] == 'x':
            return True

        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy

            if isValidPos(maze, nx, ny, visited):
                visited.add((nx, ny))
                Q.put((nx, ny))

    return False


if __name__ == "__main__":
    maze = [
        ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '1'],
        ['1', '1', '1', '0', '0', 'x'],
        ['1', '1', '1', '0', '1', '1'],
        ['1', '1', '1', '1', '1', '1']
    ]

    start = (0, 1)  # (x, y)

    print("DFS 탐색 순서:")
    print("\n탐색 결과:", DFS(maze, start))

    print("\nBFS 탐색 순서:")
    print("\n탐색 결과:", BFS(maze, start))