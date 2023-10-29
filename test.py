from a* import aStar_search

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = aStar_search(grid, start, goal)
if path:
    print("Path found:")
    for point in path:
        print(point)
else:
    print("Path not found.")


#out put 

# Path found:
# (0, 0)
# (0, 1)
# (0, 2)
# (0, 3)
# (0, 4)
# (1, 4)
# (2, 4)
# (3, 4)
# (4, 4)
