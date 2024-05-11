import csv
from collections import deque

def read_graph_from_csv(csv_file):
    graph = []
    cities = {}  # Словарь для соответствия имен городов и их индексов в матрице смежности
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        cities_list = next(reader)  # Получаем список имен городов из первой строки
        for index, city in enumerate(cities_list):
            cities[city] = index
        for row in reader:
            graph.append([int(cell) for cell in row])
    return graph, cities

def bidirectional_search(graph, start, goal):
    # Функция для поиска пути от start к goal
    def bfs(start, goal, visited, queue):
        while queue:
            current_node, path = queue.popleft()
            if current_node == goal:
                return path
            for neighbor, distance in enumerate(graph[current_node]):
                if distance > 0 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, path + [neighbor]))
        return None
    
    forward_visited = [False] * len(graph)  # Массив посещенных вершин в прямом направлении
    backward_visited = [False] * len(graph)  # Массив посещенных вершин в обратном направлении
    forward_queue = deque([(start, [start])])  # Очередь для прямого поиска
    backward_queue = deque([(goal, [goal])])  # Очередь для обратного поиска
    forward_visited[start] = True
    backward_visited[goal] = True
    
    while forward_queue and backward_queue:
        # Поиск в прямом направлении
        forward_path = bfs(start, goal, forward_visited, forward_queue)
        if forward_path:
            return forward_path
        # Поиск в обратном направлении
        backward_path = bfs(goal, start, backward_visited, backward_queue)
        if backward_path:
            return backward_path[::-1]  # Возвращаем путь в обратном порядке
    
    return None

# Функция для выбора города
def choose_city(cities):
    print("Доступные города:")
    for city in cities:
        print(city)
    start = input("Введите начальный город: ")
    goal = input("Введите конечный город: ")
    return cities[start], cities[goal]

if __name__ == "__main__":
    csv_file = "D:\Present\AI\Lab_2\map.csv"
    graph, cities = read_graph_from_csv(csv_file)
    
    start, goal = choose_city(cities)
    
    path = bidirectional_search(graph, start, goal)
    if path:
        print("Путь из", start, "в", goal, ":", path)
    else:
        print("Путь не найден.")

"""
Особенности алгоритма Bidirectional BFS (Двунаправленный поиск в ширину):
- Исследует вершины графа сразу из двух направлений: от начальной вершины к цели и от цели к начальной вершине.
- Позволяет уменьшить время поиска пути путем встречи двух поисковых волн, одна из которых начинается от начальной вершины, а другая - от конечной. Это может значительно сократить количество вершин, которые необходимо исследовать.
- Применяет поиск в ширину как в прямом, так и в обратном направлениях, пока не будет найден путь или не исчерпаны все возможные пути.
- Позволяет находить кратчайший путь от начальной вершины к цели, учитывая стоимости ребер между вершинами и эвристическую оценку стоимости оставшегося пути.
- Эффективен в поиске кратчайших путей в графах с большим количеством вершин и ребер.
"""