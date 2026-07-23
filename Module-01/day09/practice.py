#Exerciese from module day09
#1
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)

    elif value > root.value:
        root.right = insert(root.right, value)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

balances = [5000, 2500, 7000, 1000, 4000, 6000, 9000]
root = None

for balance in balances:
    root = insert(root, balance)

print("Balances in sorted order:")
inorder(root)

Print('\n')
#2
def height(node):
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return max(left_height, right_height) + 1

print("Tree Height:", height(root))

Print('\n')
#3
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                queue.append(neighbor)

    return visited

reachable = bfs(graph, "A")
print("Reachable vertices:", reachable)

Print('\n')
#4
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

print("DFS Visit Order:")
visited = dfs(graph, "A")

from collections import deque

def bfs_order(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            print(vertex)
            visited.add(vertex)

            for neighbor in graph[vertex]:
                queue.append(neighbor)

print("BFS Visit Order:")
bfs_order(graph, "A")

Print('\n')
#5
import heapq

tasks = []

heapq.heappush(tasks, (3, "Write report"))
heapq.heappush(tasks, (1, "Reply to email"))
heapq.heappush(tasks, (5, "Go shopping"))
heapq.heappush(tasks, (2, "Attend meeting"))
heapq.heappush(tasks, (4, "Read book"))

print("Tasks in priority order:")

while tasks:
    priority, task = heapq.heappop(tasks)
    print(priority, "-", task)