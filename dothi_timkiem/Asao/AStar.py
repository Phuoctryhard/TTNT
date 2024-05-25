import heapq

def astar_search(graph, heuristic, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_list:
        current_f_score, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path

        for neighbor in graph[current_node]:
            tentative_g_score = g_score[current_node] + 1  # Assuming uniform edge cost of 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None

# Example heuristic function (you can replace this with your own)
heuristic = {'A': 0, 'B': 4, 'C': 3, 'D': 2, 'E': 3, 'F': 2, 'G': 1, 'H': 0}

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

start_node = 'A'
goal_node = 'H'

path = astar_search(graph, heuristic, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("Path not found")