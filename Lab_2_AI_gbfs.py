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

def greedy_best_first_search(graph, start, goal, distance_to_Bucharest):
    visited = [False] * len(graph)
    path = [start]
    
    def heuristic(city_name):
        # Возвращаем расстояние до Бухареста, если имя города есть в словаре, иначе возвращаем максимальное значение
        return distance_to_Bucharest.get(city_name, float('inf'))
    
    while path[-1] != goal:
        current_node = path[-1]
        visited[current_node] = True
        neighbors = [(neighbor, heuristic(city_name)) for city_name, neighbor in cities.items() if graph[current_node][neighbor] > 0 and not visited[neighbor]]
        if not neighbors:
            # Если нет доступных соседей, возвращаемся на предыдущий шаг
            path.pop()
        else:
            # Выбираем соседа с наименьшей эвристикой
            next_node = min(neighbors, key=lambda x: x[1])[0]
            path.append(next_node)
    
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
    
    # Расстояния от каждого города до Бухареста
    distance_to_Bucharest = {
        "Арад": 366, "Бухарест": 0, "Крайова": 160, "Дробита": 242, "Эфорие": 161,
        "Фагарас": 176, "Джурджу": 77, "Хирсова": 151, "Яссы": 226, "Лугой": 244,
        "Мехедия": 241, "Нямц": 234, "Орадя": 380, "Питешти": 100, "РМ": 193,
        "Сибиу": 253, "Тимишоара": 329, "Урзичени": 80, "Васлуй": 199, "Зеринд": 374
    }
    
    start, goal = choose_city(cities)
    
    path = greedy_best_first_search(graph, start, goal, distance_to_Bucharest)
    if path:
        print("Путь из", start, "в", goal, ":", path)
    else:
        print("Путь не найден.")

"""
Особенности алгоритма жадного поиска лучшего соседа (Greedy Best-First Search):
- Greedy Best-First Search использует эвристику, чтобы выбирать следующий узел для исследования на основе его оценки близости к целевому узлу. Это позволяет алгоритму ориентироваться к цели, двигаясь к узлам, которые, по оценке, ближе к целевому узлу.
- Он не гарантирует нахождение кратчайшего пути, так как выбор следующего узла осуществляется только на основе эвристики, а не на основе фактической длины пути.
- В отличие от алгоритмов поиска, таких как DFS и BFS, Greedy Best-First Search может застрять в локальных минимумах или переполнениях из-за одностороннего выбора следующего узла.
- Он может быть эффективным в случае, когда имеется хорошая эвристика, которая правильно оценивает расстояние от текущего узла до целевого узла, и когда граф не содержит слишком много разветвлений или циклов, которые могут привести к плохим выборам.
"""

