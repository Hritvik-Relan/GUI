import random

def generate_maze(size=30, loops=3):
    maze = [[1 for _ in range(size)] for _ in range(size)]
    start_x, start_y = (0, random.randint(1, size - 2))
    maze[start_x][start_y] = 0
    frontier = [(start_x + 1, start_y)]
    visited = set()
    visited.add((start_x, start_y))
    
    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 < nx < size - 1 and 0 < ny < size - 1 and (nx, ny) not in visited:
                neighbors.append((nx, ny))
        return neighbors
    
    while frontier:
        x, y = random.choice(frontier)
        frontier.remove((x, y))
        neighbors = get_neighbors(x, y)
        
        if neighbors:
            nx, ny = random.choice(neighbors)
            wall_x, wall_y = (x + nx) // 2, (y + ny) // 2
            maze[x][y] = maze[wall_x][wall_y] = 0
            visited.add((x, y))
            visited.add((nx, ny))
            frontier.extend(get_neighbors(nx, ny))
    
    exit_x, exit_y = (size - 1, random.randint(1, size - 2))
    maze[exit_x][exit_y] = 0
    
    for _ in range(loops):
        lx, ly = random.randint(1, size - 2), random.randint(1, size - 2)
        maze[lx][ly] = 0
    
    return maze, (start_x, start_y), (exit_x, exit_y)

def display_maze(maze):
    for row in maze:
        print("".join("#" if cell else " " for cell in row))
    
maze, start, exit = generate_maze()
display_maze(maze)
