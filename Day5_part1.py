
with open("Day5_input.txt", "r") as file:
    input_data = file.read()
input_data = input_data.split(sep = "\n\n")
rules = input_data[0].split(sep = "\n")
updates = input_data[1].split(sep="\n")
#print(updates)
rulebook = {} #Will include all the numbers (values) that should come after a certain number (key)
for rule in rules:
    key = rule[:2]
    value = rule[3:]
    if key in rulebook.keys():
        rulebook[key].add(value)
    else:
        rulebook[key] = {value}


def main():
    count = 0
    for update in updates:
        correctly_ordered = True
        update = update.split(",")
        #print(update)
        for index, page in enumerate(update):
            if set(update[:index]) & rulebook.get(page, set()):
                correctly_ordered = False
                break
        if correctly_ordered:
            index = int(len(update)/2)
            count += int(update[index])
    return count

print(f"{main()=}")
