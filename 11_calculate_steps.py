'''
You need to get to the mall to buy some new shoes, but you're not sure how to get there. Your city is a n X m rectangular grid of blocks, 
where your home is located at the coordinates (x1, y1) and the mall's location is (x2, y2). It is guaranteed that (x1, y1) and (x2, y2) are not the same.

Since you're not sure exactly how to get to the mall, you follow a movement strategy based on these rules:

Move diagonally on each move, starting in the direction (+1, +1). It means that standing at a cell with coordinates (x, y), you'll move to the cell with coordinates (x + 1, y + 1) 
unless the new cell is outside the city grid,
If the current move would take you outside the city grid, come back and reverse the direction that was leading outside the grid 
(eg: if the x coordinate is outside the grid, reverse the x movement direction),
If the current move would escape the city grid outside of a corner, reverse both directions.
Your task is to determine how many steps it will take to reach the mall at (x2, y2). Return -1 if it's not possible to reach the mall using this strategy.

For better understanding how the movement rules work, take a look at the animations in the examples section.

Notes:

A diagonal movement or a bounce (direction change) each count as a single step.
Coordinates of a cell are defined differently in comparison to mathematical coordinates, take a closer look at the animations in the examples section below.
'''

def steps_to_mall(n, m, x1, y1, x2, y2):
    # initialize starting position and movement direction
    pos = [x1, y1]
    direction = [1, 1]
    steps = 0
    
    # keep track of visited positions to detect cycles
    visited = set()
    visited.add((x1, y1, tuple(direction)))
    
    while pos != [x2, y2]:
        # update position
        pos[0] += direction[0]
        pos[1] += direction[1]
        steps += 1
        print(f"x: {pos[0]}, y: {pos[1]}")
        
        # check if position is outside grid
        if pos[0] < 1:
            pos[0] += direction[0]
        if pos[0] > n:
            pos[0] -= direction[0]
        if pos[1] < 1:
            pos[1] += direction[1]
        if pos[1] > m:
            pos[1] -= direction[1]
        
        # check if we've visited this position before with the same direction
        if (pos[0], pos[1], tuple(direction)) in visited:
            return -1
        visited.add((pos[0], pos[1], tuple(direction)))
        
        # check if we need to reverse direction
        if pos[0] == 1 and direction[0] == -1:
            direction[0] = 1
        elif pos[0] == n and direction[0] == 1:
            direction[0] = -1
        elif pos[1] == 1 and direction[1] == -1:
            direction[1] = 1
        elif pos[1] == m and direction[1] == 1:
            direction[1] = -1
    
    return steps


print(f"{steps_to_mall(10, 10, 1, 1, 1, 10)}")

      