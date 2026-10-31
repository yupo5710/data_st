# 5.22

from CircularDeque import CircularDeque


def is_palindrome(text):
    # 구두점과 공백을 제거하고 대소문자 통일
    text = ''.join(ch for ch in text.casefold() if ch.isalnum())

    D = CircularDeque(len(text) + 1)

    for ch in text:
        D.addRear(ch)

    # 양 끝의 문자를 꺼내 비교
    while D.size() > 1:
        if D.deleteFront() != D.deleteRear():
            return False

    return True


if __name__ == "__main__":
    text = input("문자열 입력: ")

    if is_palindrome(text):
        print("회문입니다.")
    else:
        print("회문이 아닙니다.")