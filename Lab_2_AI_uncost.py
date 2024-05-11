import csv
import heapq

def read_graph_from_csv(csv_file):
    graph = {}
    cities = {}
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        cities_list = next(reader)
        for index, city in enumerate(cities_list):
            cities[city] = index
            graph[index] = {}
        for index, row in enumerate(reader):
            for j, cell in enumerate(row):
                if int(cell) > 0:
                    graph[index][j] = int(cell)
    return graph, cities

def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = [(0, start, [start])]
    
    while queue:
        cost, current_node, path = heapq.heappop(queue)
        
        if current_node == goal:
            return path
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor, distance in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + distance, neighbor, path + [neighbor]))
    
    return None

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
    
    path = uniform_cost_search(graph, start, goal)
    if path:
        print("Путь из", start, "в", goal, ":", path)
    else:
        print("Путь не найден.")

"""
Особенности алгоритма Uniform Cost Search (UCS):
    
- UCS является одним из алгоритмов поиска пути в графе, который ориентирован на нахождение кратчайшего пути от начальной вершины к целевой вершине.
- В отличие от жадных алгоритмов, UCS не использует эвристику для выбора следующей вершины. Вместо этого он рассматривает стоимость каждого возможного пути от начальной вершины к другим вершинам и выбирает путь с наименьшей стоимостью.
- UCS гарантирует нахождение кратчайшего пути от начальной вершины ко всем остальным достижимым вершинам в графе. Это достигается за счет того, что алгоритм исследует пути в порядке их возрастания стоимости.
- По сравнению с алгоритмами поиска в глубину (DFS) и поиска в ширину (BFS), UCS может потребовать больше времени на поиск кратчайшего пути, особенно если граф имеет большую структуру или множество путей с близкими стоимостями.
- UCS является оптимальным алгоритмом, то есть он всегда находит кратчайший путь, если такой существует, хотя он может не быть самым быстрым для некоторых задач, особенно если стоимости ребер неоднородны.
"""