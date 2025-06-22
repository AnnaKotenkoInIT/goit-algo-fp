import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.id = str(uuid.uuid4())
        self.color = "#CE6CF1"  # Стартовий колір вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, label=node.val, color=node.color)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            lx = x - 1 / 2 ** layer
            pos[node.left.id] = (lx, y - 1)
            add_edges(graph, node.left, pos, lx, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            rx = x + 1 / 2 ** layer
            pos[node.right.id] = (rx, y - 1)
            add_edges(graph, node.right, pos, rx, y - 1, layer + 1)


def draw_tree_step(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)
    colors = [data['color'] for _, data in tree.nodes(data=True)]
    labels = {n: data['label'] for n, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors)
    plt.show()


def generate_color_gradient(n):
    # Від темного синього до світлого блакитного
    colors = []
    for i in range(n):
        intensity = int(50 + (205 * i / (n - 1)))
        hex_color = f"#{intensity:02x}{intensity:02x}F0"
        colors.append(hex_color)
    return colors


def dfs_visual(root):
    if not root:
        return
    stack = [root]
    visited = []
    colors = generate_color_gradient(100)  # запас кольорів

    step = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            node.color = colors[step]
            step += 1
            draw_tree_step(root)
            visited.append(node)
            # Спочатку правий, бо стек — LIFO
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def bfs_visual(root):
    if not root:
        return
    queue = deque([root])
    visited = []
    colors = generate_color_gradient(100)

    step = 0
    while queue:
        node = queue.popleft()
        if node not in visited:
            node.color = colors[step]
            step += 1
            draw_tree_step(root)
            visited.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходів
print("DFS обхід:")
dfs_visual(root)

# Скидання кольорів перед BFS
for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left]:
    node.color = "#D1EC1F"

print("BFS обхід:")
bfs_visual(root)
