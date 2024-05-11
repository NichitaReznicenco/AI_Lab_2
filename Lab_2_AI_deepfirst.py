import csv

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

def depth_first_search(graph, start, goal):
    visited = [False] * len(graph)
    path = []
    
    def dfs(current_node):
        visited[current_node] = True
        path.append(current_node)
        if current_node == goal:
            return True
        for neighbor, distance in enumerate(graph[current_node]):
            if distance > 0 and not visited[neighbor]:
                if dfs(neighbor):
                    return True
        path.pop()
        return False
    
    dfs(start)
    if path[-1] != goal:
        return None
    return path

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
    
    path = depth_first_search(graph, start, goal)
    if path:
        print("Путь из", start, "в", goal, ":", path)
    else:
        print("Путь не найден.")

"""
Особенности алгоритма поиска в глубину (DFS):
- Поиск в глубину использует стек для хранения вершин, что позволяет ему исследовать пути настолько глубоко, насколько это возможно, прежде чем вернуться и исследовать другие пути.
- Он начинает с выбранной начальной вершины и исследует все ее соседние вершины по одной, до тех пор, пока не достигнет вершины, у которой больше нет непосещенных соседей, после чего возвращается к предыдущей вершине и продолжает поиск.
- DFS не гарантирует нахождение кратчайшего пути, так как он может зациклиться на одной ветви исследования, если она содержит большое количество вершин.
- В отличие от BFS, DFS может работать с графами с циклами и даже с бесконечными графами, так как он не требует запоминания посещенных вершин, пока не найдет путь до целевой вершины.
"""
