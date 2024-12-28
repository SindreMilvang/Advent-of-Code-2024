import numpy as np
import pandas as pd


content = pd.read_csv("/Users/sindre/Downloads/AoC_Day2_input.txt") 
content = content.to_numpy()

count = 0
for report in content:
    report = np.array(report[0].split(), dtype = int)
    steps = report[1:] - report[:-1]
    if not ((steps>0).all() or (steps<0).all()): #Ikke monoton
        continue
    steplength = np.isin(abs(steps), [1,2,3])
    if not steplength.all():  #for store hopp
        continue
    count += 1


    