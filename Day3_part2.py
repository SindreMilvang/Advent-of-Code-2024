import re
import numpy as np


with open("Day3_input.txt", "r") as file:
    content = file.read()

#regular expression patterns
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"


def find_pattern(content):
    mul_match = re.search(mul_pattern, content)
    if mul_match:
        mul_index = mul_match.end()
    else:
        raise Exception("End of text (mul)") 
    
    dont_match = re.search(dont_pattern, content)
    if dont_match:
        dont_index = dont_match.end()
    else:
        return True, mul_match, 0 
    
    return mul_index < dont_index, mul_match, dont_index

end_of_file = False
enable_counting = True
continue_from_index = 0
count = 0
while not end_of_file:
    try:
        enable_counting, mul_match, dont_index = find_pattern(content[continue_from_index:])
        mul_index = mul_match.end()
    except Exception as e:
        print(e)
        end_of_file = True
        continue
    if enable_counting:
        numbers_in_mul = mul_match.group()[4:-1].split(",")
        count +=int(numbers_in_mul[0])*int(numbers_in_mul[1])
        continue_from_index += mul_index
    else:
        continue_from_index += dont_index
        do_match = re.search(do_pattern, content[continue_from_index:])
        if do_match:
            do_index = do_match.end()
        else:
            end_of_file = True 
        continue_from_index += do_index
    print(f"{enable_counting}: {numbers_in_mul=}, {continue_from_index=}, {count=}")
