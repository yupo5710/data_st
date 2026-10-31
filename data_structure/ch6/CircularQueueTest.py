from CircularQueue import CircularQueue

q = CircularQueue(8)
 
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.enqueue('D')
q.enqueue('E')
q.enqueue('F')
print('A B C D E F 삽입: ', q)
print('삭제 -->', q.dequeue())
print('삭제 -->', q.dequeue())
print('삭제 -->', q.dequeue())
print('      3번의 삭제: ', q)
q.enqueue('G')
q.enqueue('H')
q.enqueue('I')
print('      G H I 삽입: ', q)