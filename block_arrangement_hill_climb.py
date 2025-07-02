import random

GOAL = ['A', 'B', 'C', 'D']

# Heuristic: number of misplaced blocks
def heuristic(state):
    return sum(1 for i in range(len(state)) if state[i] != GOAL[i])

def get_neighbors(state):
    neighbors = []
    for i in range(len(state) - 1):
        neighbor = state[:]
        neighbor[i], neighbor[i + 1] = neighbor[i + 1], neighbor[i]
        neighbors.append((f"Swap {i} and {i+1}", neighbor))
    return neighbors

def hill_climb(start):
    current = start
    path = []
    while True:
        current_h = heuristic(current)
        print("Current State:", current, "Heuristic:", current_h)
        neighbors = get_neighbors(current)
        next_state = min(neighbors, key=lambda x: heuristic(x[1]), default=(None, current))

        if heuristic(next_state[1]) >= current_h:
            break

        current = next_state[1]
        path.append(next_state[0])

        if current == GOAL:
            break

    return current, path

# Test
initial_stack = ['C', 'A', 'D', 'B']
final, path = hill_climb(initial_stack)

print("\nInitial Stack:", initial_stack)
print("Final Stack:", final)
print("Moves:", path)
