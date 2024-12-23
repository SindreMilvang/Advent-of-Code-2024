import numpy as np
#Part 1
content = np.loadtxt("/Users/sindre/Downloads/AoC_day1_input.txt")  #Loads a .txt file as numpy arrays
list1, list2 = np.split(np.transpose(content), 2)                   #Creates two arrays
difference = abs(np.sort(list1)-np.sort(list2))                     #Sorts and takes the difference of the arrays
print(np.sum(difference))                                           #Prints the sum of the differences

#Part 2
similarity_score = 0
for i in list1[0]:
    similarity_score += np.count_nonzero(list2[0] == i)*i
print(similarity_score)
