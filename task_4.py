import uuid
import networkx as nx
import matplotlib.pyplot as plt


class HeapNode:
    def __init__(self, key, color="lightgreen"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap_array):
    nodes = [HeapNode(val) for val in heap_array]
    n = len(nodes)

    for i in range(n):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < n:
            nodes[i].left = nodes[left_idx]
        else:
            nodes[i].left = None
        if right_idx < n:
            nodes[i].right = nodes[right_idx]
        else:
            nodes[i].right = None

    return nodes[0] if nodes else None


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
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


def draw_heap(heap_array):
    root = build_heap_tree(heap_array)
    if not root:
        print("Heap is empty")
        return

    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [data['color'] for _, data in tree.nodes(data=True)]
    labels = {n: data['label'] for n, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors)
    plt.show()


# Приклад використання:
heap_array = [10, 7, 9, 5, 6, 8]
draw_heap(heap_array)
