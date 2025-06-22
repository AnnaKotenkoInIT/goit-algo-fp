class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        elems = []
        while current:
            elems.append(str(current.data))
            current = current.next
        print(" -> ".join(elems) + " -> None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


    def sorted_insert(self, new_node):
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()
        current_self = self.head
        current_other = other_list.head
        while current_self or current_other:
            if not current_self:
                merged_list.sorted_insert(Node(current_other.data))
                current_other = current_other.next
            elif not current_other:
                merged_list.sorted_insert(Node(current_self.data))
                current_self = current_self.next
            elif current_self.data <= current_other.data:
                merged_list.sorted_insert(Node(current_self.data))
                current_self = current_self.next
            else:
                merged_list.sorted_insert(Node(current_other.data))
                current_other = current_other.next
        return merged_list   


# Testing
llist = LinkedList()

print("Кейс 1: Додавання на початок")
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.print_list()

print("\nКейс 2: Додавання в кінець")
llist.insert_at_end(20)
llist.insert_at_end(25)
llist.print_list()

print("\nКейс 3: Видалення вузла (10)")
llist.delete_node(10)
llist.print_list()

print("\nКейс 4: Пошук елемента (15)")
node = llist.search_element(15)
if node:
    print(f"Знайдено: {node.data}")
else:
    print("Не знайдено")

print("\nКейс 5: Реверс списку")
llist.reverse()
llist.print_list()

print("\nКейс 6: Вставка після 20")
target = llist.search_element(20)
llist.insert_after(target, 18)
llist.print_list()