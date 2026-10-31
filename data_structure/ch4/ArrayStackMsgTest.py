from ArrayStack import ArrayStack
s=ArrayStack(100)

msg = input("문자열입력: ")
for c in msg:
        s.push(c)

print("문자열출력: ", end='')
while not s.isEmpty():
    print(s.pop(), end='')
print()

# 입력한 문자열 거꾸로 출력