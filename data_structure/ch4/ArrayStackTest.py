from ArrayStack import ArrayStack 

s = ArrayStack(10)

for i in range(1, 6):
    s.push(i)
print("push 5회: ", s)

s.pop()
print('pop 1회:', s)

print('peek :', s.peek())
# 이 코드는 1~5를 스택에 넣고, 한 번 꺼낸 뒤 맨 위 값을 확인합니다.