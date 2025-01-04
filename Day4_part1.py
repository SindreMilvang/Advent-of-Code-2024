import numpy as np

with open("Day4_input.txt", "r") as file:
    rows = file.readlines()
grid = [list(row.strip()) for row in rows] #2D list of all the characters in the string

def horizontal(rows, word):
    count = 0
    for row in rows:
        count += row.count(word)
    return count

def vertical(grid, word):
    grid_T = np.transpose(np.array(grid))
    count = 0
    for column in grid_T:
        column = "".join(column)
        count += column.count(word)
    return count

def diagonal(grid, word):
    grid = np.array(grid)
    count = 0
    for i in range(-len(grid)+1, len(grid[0])):
        diagonal = np.diagonal(grid, offset = i) #Utilizing numpy's diagonal function
        diagonal = "".join(list(diagonal))
        anti_diagonal = np.diagonal(np.flipud(grid), offset = i)
        anti_diagonal = "".join(list(anti_diagonal))
        count += diagonal.count(word)
        count += anti_diagonal.count(word)
    return count


#Using the functions defined above to count all occurances of XMAS
def main(grid):
    count = 0
    for word in ["XMAS", "SAMX"]: #Takes account for spelling both forward and backwards
        count += horizontal(rows, word)
        count += vertical(grid, word)
        count += diagonal(grid, word)
    return count
print(main(grid))