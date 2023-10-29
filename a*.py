class node:
  def __init__(self, position, parent=None):
    self.position = position
    self.parent = parent
    self.g = 0
    self.h = 0
    self.f = 0
  
  def __lt__(self, other):
    return self.f < other.f




def calculate_heuristic(current, goal):
  return abs(current.position[0] - goal.position[0]) + abs(current.position[1] - goal.position[1])



def get_neighbors(postion, grid):
  neighbors = list()
  directions = [
      (0, -1), # up
      (0, 1), # down
      (-1, 0), # left
      (1, 0)  # right
  ]

  for x, y in directions:
    new_x = postion[0] + x
    new_y = postion[1] + y
    if 0 <=  new_x < len(grid) and 0 <=  new_y < len(grid[0]) and grid[new_x][new_y] != 1:
      neighbors.append((new_x, new_y))
  return neighbors

def reconstruct_path(current):
  path = list()
  while current is not None:
    path.append(current.position)
    current = current.parent
  return path[::-1]



def aStar_search(grid, start, goal):
  open_set = list()
  closed_set = list()

  start_node = node(start)
  goal_node = node(goal)
  start_node.g = 0
  start_node.h = calculate_heuristic(start_node, goal_node)
  start_node.f = start_node.g + start_node.h
  open_set.append({
        "node" : start_node,
        "pos" : start_node.position,
  })

  while open_set:
    current =  min(open_set, key=lambda element : element["node"].f)
    open_set.remove(current)
    current = current["node"]

    closed_set.append({
        "node" : current,
        "pos" : current.position,
    })

    if current.position == goal:
      return reconstruct_path(current)

    for neighbor in get_neighbors(current.position, grid):
      check_open, check_close = True, True

      neighbor_node = node(neighbor, current)
      neighbor_node.g = current.g + 1
      neighbor_node.h = calculate_heuristic(neighbor_node, goal_node)
      neighbor_node.f = neighbor_node.g + neighbor_node.h

      for element in open_set:
        if element["pos"] == neighbor_node.position:
          if neighbor_node.f < element["node"].f:
            element["node"].f = neighbor_node.f
            check_open = False

      for element in closed_set:
        if element["pos"] == neighbor_node.position:
          if neighbor_node.f < element["node"].f:
            closed_set.remove(element)
            open_set.append({
                  "node" : element,
                  "pos" : element.position,
            })
            check_close = False


      if check_close and check_open:
        open_set.append({
          "node" : neighbor_node,
          "pos" : neighbor_node.position,
      })
  return None
