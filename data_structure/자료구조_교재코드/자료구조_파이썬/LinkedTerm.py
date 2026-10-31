from LinkedList import LinkedList
from Node import Node


class Term:
    def __init__(self, expo, coef):
        self.expo = expo
        self.coef = coef


class SparsePoly(LinkedList):
    def read(self):
        count = int(input("입력할 항의 개수: "))
        terms = {}

        for _ in range(count):
            # 입력 순서는 계수, 지수
            coef, expo = map(
                int, input("계수 지수 입력: ").split()
            )

            if expo < 0:
                raise ValueError("지수는 0 이상이어야 합니다.")

            # 같은 지수의 항은 계수를 합침
            terms[expo] = terms.get(expo, 0) + coef

        self.head = None
        tail = None

        for expo in sorted(terms, reverse=True):
            coef = terms[expo]

            if coef == 0:
                continue

            node = Node(Term(expo, coef), None)

            if self.head is None:
                self.head = node
            else:
                tail.link = node

            tail = node

    def display(self):
        node = self.head
        parts = []

        while node is not None:
            term = node.data
            coef = term.coef
            expo = term.expo
            magnitude = abs(coef)

            if expo == 0:
                body = str(magnitude)
            else:
                # 계수가 1이면 1x 대신 x로 표시
                body = "" if magnitude == 1 else str(magnitude)
                body += "x" if expo == 1 else f"x^{expo}"

            if not parts:
                parts.append(("-" if coef < 0 else "") + body)
            else:
                parts.append((" - " if coef < 0 else " + ") + body)

            node = node.link

        print("".join(parts) if parts else "0")

    def add(self, polyB):
        result = SparsePoly()

        # 결과 리스트를 만들기 위한 임시 시작 노드
        dummy = Node(None, None)
        tail = dummy

        a = self.head
        b = polyB.head

        while a is not None or b is not None:
            if b is None or (
                a is not None and a.data.expo > b.data.expo
            ):
                expo = a.data.expo
                coef = a.data.coef
                a = a.link

            elif a is None or b.data.expo > a.data.expo:
                expo = b.data.expo
                coef = b.data.coef
                b = b.link

            else:
                # 지수가 같으면 계수를 더함
                expo = a.data.expo
                coef = a.data.coef + b.data.coef
                a = a.link
                b = b.link

            # 합이 0인 항은 저장하지 않음
            if coef != 0:
                tail.link = Node(Term(expo, coef), None)
                tail = tail.link

        result.head = dummy.link
        return result


if __name__ == "__main__":
    A = SparsePoly()
    B = SparsePoly()

    print("첫 번째 다항식")
    A.read()

    print("두 번째 다항식")
    B.read()

    C = A.add(B)

    print("A = ", end="")
    A.display()

    print("B = ", end="")
    B.display()

    print("A + B = ", end="")
    C.display()