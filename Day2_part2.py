import numpy as np
import pandas as pd

content = pd.read_csv("/Users/sindre/Downloads/AoC_Day2_input.txt", header = None) 
content = content.to_numpy()
count = 0

def is_safe(report) -> bool:
    steps = report[1:] - report[:-1]
    if not ((steps>0).all() or (steps<0).all()): #Ikke monoton
        return False
    steplength = np.isin(abs(steps), [1,2,3])
    if not steplength.all():  #for store hopp
        return False
    return True

for txt_report in content:
    report = np.array(txt_report[0].split(), dtype = int) #Converts report ro a 1D array of integers
    if is_safe(report): #Counts all reports with zero error levels, as in part 1
        count += 1
    else:
        for i in range(len(report)):    #Iterates through each unsafe report, removes one level and checks if it then is safe
            mod_report = np.delete(report, i)
            if is_safe(mod_report):
                count += 1
                break

print(count)
