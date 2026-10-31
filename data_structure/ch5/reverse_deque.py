# 5.15 덱의 뒤집기


from CircularDeque import CircularDeque
from CircularQueue import CircularQueue


if __name__ == "__main__":
    D = CircularDeque(10)
    Q = CircularQueue(10)

    # 덱의 뒤에 1부터 8까지 삽입
    for i in range(1, 9):
        D.addRear(i)

    print("뒤집기 전:", D)

    # 1. 덱의 뒤에서 꺼내 큐에 삽입
    while not D.isEmpty():
        Q.enqueue(D.deleteRear())

    # 2. 큐에서 꺼내 덱의 뒤에 삽입
    while not Q.isEmpty():
        D.addRear(Q.dequeue())

    print("뒤집기 후:", D)
 