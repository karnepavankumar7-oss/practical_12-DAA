from itertools import permutations

def tsp_exact(distance_matrix, start=0):
    num_cities = len(distance_matrix)
    other_cities = [i for i in range(num_cities) if i != start]
    
    min_cost = float('inf')
    best_path = []

    # Check every possible permutation of the remaining cities
    for perm in permutations(other_cities):
        current_path = [start] + list(perm) + [start]
        current_cost = 0
        
        # Calculate total distance for this route
        for i in range(len(current_path) - 1):
            current_cost += distance_matrix[current_path[i]][current_path[i + 1]]
            
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return best_path, min_cost

# Example: 4 cities represented as a distance matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = tsp_exact(graph)
print(f"Optimal Path: {path}")
print(f"Minimum Cost: {cost}")
