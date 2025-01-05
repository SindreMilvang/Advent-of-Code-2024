import numpy as np

with open("Day4_input.txt", "r") as file:
    input_data = file.readlines()

grid = np.array([list(row.strip()) for row in input_data]) #2D array of all the characters in the string

def is_X(box):
    if box[1,1] != "A":
        return False
    elif "".join([box[0,0],box[2,2],box[2,0],box[0,2]]) in ["SMSM", "SMMS", "MSSM", "MSMS"]:
        return True
    return False

def main():
    count = 0
    for n in range(len(grid)-2):
        for i in range(len(grid[0])-2):
            box = grid[n:n+3,i:i+3]
            if is_X(box):
                count += 1
    return count

print(main())        