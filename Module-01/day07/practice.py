# Exercises from module1 day07
#1
numbers = [10, 20, 30, 40, 50]
print(numbers[3])

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

numbers = [1, 2, 3, 4]

for i in numbers:
    for j in numbers:
        print(i, j)

accounts = {
    "A001": 1000,
    "A002": 2000,
    "A003": 1500
}

print(accounts["A003"])

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

numbers = list(range(1, 101))
print(binary_search(numbers, 78))

print('\n')
#2
import time

accounts_list = [f"ACC{i}" for i in range(100000)]

accounts_dict = {f"ACC{i}": i for i in range(100000)}

target = "ACC99999"

start = time.perf_counter()

found = target in accounts_list

end = time.perf_counter()

print("List lookup:", end - start)

start = time.perf_counter()

found = target in accounts_dict

end = time.perf_counter()

print("Dict lookup:", end - start)

print('\n')
#3
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

names = ["Abebe", "Biruk", "Surafel", "Kirubel"]

stack = Stack()

for name in names:
    stack.push(name)

reversed_names = []

while stack.items:
    reversed_names.append(stack.pop())

print(reversed_names)

print('\n')
#5
from collections import deque

queue = deque()

queue.append("Nahon")
queue.append("Samson")
queue.append("Hiwot")
queue.append("Dani")
queue.append("Eleni")

while queue:
    customer = queue.popleft()
    print(f"Serving {customer}")

print('\n')
#5
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_all(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next


linked_list = LinkedList()

linked_list.push_front("Abel")
linked_list.push_front("Yeab")
linked_list.push_front("Eyasu")

linked_list.print_all()