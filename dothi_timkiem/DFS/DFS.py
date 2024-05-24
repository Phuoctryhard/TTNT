import time

def DFS(initialState, goal):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop(len(frontier)-1)
        explored.append(state)
        if goal == state:
            return explored
        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)
    return False

if __name__ == '__main__':
    graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F', 'G'],
        'D' : [],
        'E' : ['H'],
        'F' : ['H'],
        'G' : ['H'],
        'H' : []
    #    'A' : ['B', 'C'],
    #    'B' : ['D', 'E'],
    #    'C' : ['F', 'G'],
    #    'D' : ['H', 'I'],
    #    'E' : ['J', 'K'],
    #    'F' : ['L', 'M'],
    #    'G' : ['N', 'O'],
    #    'H' : ['P', 'Q' , 'R'],
    #    'I' : ['S', 'T', 'U'],
    #    'J' : ['V'],
    #    'K' : [],
    #    'L' : ['W', 'X', 'Y', 'Z'],
    #    'M' : [],
    #    'N' : [],
    #    'O' : [],
    #    'P' : [],
    #    'Q' : [],
    #    'R' : [],
    #    'S' : [],
    #    'T' : [],
    #    'U' : [],
    #    'V' : [],
    #    'W' : [],
    #    'X' : [],
    #    'Y' : [],
    #    'Z' : []
    }

    result = DFS('A', input("Enter goal: "))
    end_point = ''
    if result:
        s = 'Explored '
        for i in result:
            end_point = i
            s += i + ' '
            print(s)
            # time.sleep(1)
        print(end_point)
    else:
        end_point = '404 Not Found!'
        print(end_point)