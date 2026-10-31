from Node import Node

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, elem):
        self.top = Node(elem, self.top)

    def pop(self):
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.link
        return data


def isPalindrome(text):
    # 구두점과 공백을 제거하고 대소문자를 통일
    text = "".join(ch for ch in text.casefold() if ch.isalnum())

    stack = LinkedStack()

    for ch in text:
        stack.push(ch)

    for ch in text:
        if ch != stack.pop():
            return False

    return True


text = input("문자열 입력: ")
print("회문입니다." if isPalindrome(text) else "회문이 아닙니다.")