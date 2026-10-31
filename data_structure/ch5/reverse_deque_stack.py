# 5.16 덱의 뒤집기 (스택을 사용하여)

from CircularDeque import CircularDeque

D = CircularDeque(10)
S = []

for i in range(1, 9):
    D.addRear(i)

print("뒤집기 전:", D)

# 덱의 뒤에서 꺼내 스택에 삽입
while not D.isEmpty():
    S.append(D.deleteRear())

# 스택에서 꺼내 덱의 앞에 삽입
while S:
    D.addFront(S.pop())

print("뒤집기 후:", D)