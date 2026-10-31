from LinkedList import LinkedList

L = LinkedList()
    
print("최초   ", L)
L.insert(0, 10)
L.insert(0, 20)
L.insert(1, 30)
L.insert(2, 50)
print("삽입x5 ", L)
L.delete(2)
print("삭제(2)", L)
print("삭제(E)", L)
L.delete(0)
print("삭제(0)", L)
