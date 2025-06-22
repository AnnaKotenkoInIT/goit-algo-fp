import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    heap = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()

    while heap:
        
        current_distance, current_vertex = heapq.heappop(heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

def create_graph():
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }
    return graph

def main():
    graph = create_graph()
    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)

    for vertex in distances:
        print(f'Відстань від {start_vertex} до {vertex} дорівнює {distances[vertex]}')


if __name__ == "__main__":
    main()
