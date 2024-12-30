import re
import numpy as np

with open("Day3_input.txt", "r") as file:
    content = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"     #Pattern for "mul(3-digit-number,3-digit-number)"
matches = np.array(re.findall(pattern, content), dtype=int) #Finds occurances of the pattern. Each element of the array is a tuple of the two groups (3 digit numbers) 
products = matches[:,0]*matches[:,1] #Multiplies the numbers the tuple

print(f"{sum(products)=}") #Sums all the products
