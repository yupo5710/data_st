class ArraySet:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    # 원소가 집합에 있는지 확인
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False

    # 중복되지 않는 원소만 삽입
    def insert(self, e):
        if not self.isFull() and not self.contains(e):
            self.array[self.size] = e
            self.size += 1
            return True
        return False

    # 값이 e인 원소 삭제
    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.size -= 1
                self.array[self.size] = None
                return True
        return False

    # 합집합
    def union(self, other):
        result = ArraySet(self.size + other.size)
        for i in range(self.size):
            result.insert(self.array[i])
        for i in range(other.size):
            result.insert(other.array[i])
        return result

    # 교집합
    def intersection(self, other):
        result = ArraySet(self.size)
        for i in range(self.size):
            if other.contains(self.array[i]):
                result.insert(self.array[i])
        return result

    # 차집합: 자신에게만 있는 원소
    def difference(self, other):
        result = ArraySet(self.size)
        for i in range(self.size):
            if not other.contains(self.array[i]):
                result.insert(self.array[i])
        return result

    def __str__(self):
        if self.isEmpty():
            return "{}"
        return "{" + ", ".join(
            str(self.array[i]) for i in range(self.size)
        ) + "}"
        
        

maze = [
    [1, 1, 1, 1, 1, 1],
    ['e', 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 'x'],
    [1, 1, 1, 1, 1, 1]
]

stack = [(0, 1)]
visited = set()

while stack:
    x, y = stack.pop()

    if (x, y) in visited:
        continue

    if maze[y][x] == 'x':
        print("출구 발견!")
        break

    visited.add((x, y))

    for dx, dy in [(0,-1), (0,1), (-1,0), (1,0)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 6 and 0 <= ny < 6:
            if maze[ny][nx] != 1:
                if (nx, ny) not in visited:
                    stack.append((nx, ny))
else:
    print("출구를 찾지 못했습니다.")
