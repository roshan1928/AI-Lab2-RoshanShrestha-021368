from collections import deque

GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Manhattan Distance Heuristic
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = (val - 1) // 3, (val - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Convert 2D list to tuple for hashing
def state_to_tuple(state):
    return tuple([tuple(row) for row in state])

# Get possible moves
def get_neighbors(state):
    directions = [("up", -1, 0), ("down", 1, 0), ("left", 0, -1), ("right", 0, 1)]
    neighbors = []
    x, y = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]

    for name, dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append((name, new_state))
    return neighbors

def bfs(start):
    queue = deque()
    visited = set()
    queue.append((start, []))

    while queue:
        current, path = queue.popleft()
        visited.add(state_to_tuple(current))

        if current == GOAL_STATE:
            return path

        for move, neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                queue.append((neighbor, path + [move]))
                print("Explored State:", neighbor, "Heuristic:", manhattan(neighbor))

    return None

# Test
initial_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
solution = bfs(initial_state)

print("\nInitial State:", initial_state)
print("Solution Path:", solution)
