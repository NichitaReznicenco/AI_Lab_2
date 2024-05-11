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

def bfs(graph, start, goal):
    visited = [False] * len(graph)
    queue = deque([(start, [start])])
    visited[start] = True
    
    while queue:
        current_node, path = queue.popleft()
        
        if current_node == goal:
            return path
        
        for neighbor, distance in enumerate(graph[current_node]):
            if distance > 0 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, path + [neighbor]))
    
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
    
    path = bfs(graph, start, goal)
    if path:
        print("Путь из", start, "в", goal, ":", path)
    else:
        print("Путь не найден.")

"""
Особенности алгоритма поиска в ширину (BFS):
- Исследует вершины графа по уровням, начиная с исходной вершины и постепенно расширяя поиск на все ближайшие вершины, затем на их соседей и так далее. Эта стратегия гарантирует нахождение кратчайшего пути от начальной вершины ко всем остальным вершинам в неориентированном графе без весов на ребрах.
- Использует очередь для хранения вершин, которые еще не были исследованы, обрабатывая вершины в порядке их добавления и обеспечивая поиск в ширину.
- Помогает определить, существует ли путь между двумя вершинами, и если путь существует, то находит кратчайший путь.
- Обеспечивает линейное время выполнения при поиске в графах без циклов, что делает его эффективным для нахождения кратчайших путей.
"""

"""
Начать с исходного узла и поместить его в очередь (или список).
Пометить исходный узел как посещенный.
Извлечь узел из очереди и проверить его соседей.
Для каждого соседа, который еще не был посещен и не находится в очереди:
Пометить его как посещенный.
Добавить его в очередь.
Повторять шаги 3-4, пока очередь не станет пустой.

"""