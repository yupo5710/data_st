# 5.21

from CircularQueue import CircularQueue


def fibonacci(n):
    if n < 0:
        raise ValueError("n은 0 이상이어야 합니다.")

    if n == 0:
        return 0

    # 원형 큐는 한 칸을 비워 두므로 용량을 3으로 설정
    Q = CircularQueue(3)
    Q.enqueue(0)  # F(0)
    Q.enqueue(1)  # F(1)

    for i in range(2, n + 1):
        previous = Q.dequeue()  # F(i-2)
        current = Q.peek()      # F(i-1)
        Q.enqueue(previous + current)  # F(i)

    Q.dequeue()  # F(n-1) 제거
    return Q.peek()  # F(n) 반환


if __name__ == "__main__":
    n = int(input("n 입력: "))
    print(f"F({n}) = {fibonacci(n)}")