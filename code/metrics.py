#f = open("/Users/aarasada/champ_ext/data/results/chatGPT-4o_aime_2001_to_2020.csv", "r")
f = open("/Users/aarasada/champ_ext/data/results/llama_aime_2001_to_2020.csv", "r")

#c_count = 0
#nc_count = 0

pos_c = {}
pos_inc = {}

while True:
    line = f.readline()
    if not line:
        break

    line = line[:-1]
    #print(line)
    
    tokens = line.split(",")
    print(tokens)

    print(f"position:{tokens[1]}")
    
    if tokens[3] == 'C':
        if tokens[1] in pos_c:
            pos_c[tokens[1]] += 1
        else:
            pos_c[tokens[1]] = 1
    elif tokens[3] == 'NC':
        if tokens[1] in pos_inc:
            pos_inc[tokens[1]] += 1
        else:
            pos_inc[tokens[1]] = 1

accuracy_first_1 = 100 * pos_c['1'] / (pos_c['1'] + pos_inc['1'])
print(f"accuracy_first_1: {accuracy_first_1}")
        
correct_first_2 = pos_c['1'] + pos_c['2']
incorrect_first_2 = pos_inc['1'] + pos_inc['2']
accuracy_first_2 = 100 * correct_first_2 / (correct_first_2 + incorrect_first_2)
print(f"accuracy_first_2: {accuracy_first_2}")

correct_first_3 = pos_c['1'] + pos_c['2'] + pos_c['3']
incorrect_first_3 = pos_inc['1'] + pos_inc['2'] + pos_inc['3']
accuracy_first_3 = 100 * correct_first_3 / (correct_first_3 + incorrect_first_3)
print(f"accuracy_first_3: {accuracy_first_3}")

correct_first_4 = pos_c['1'] + pos_c['2'] + pos_c['3'] + pos_c['4']
incorrect_first_4 = pos_inc['1'] + pos_inc['2'] + pos_inc['3'] + pos_inc['4']
accuracy_first_4 = 100 * correct_first_4 / (correct_first_4 + incorrect_first_4)
print(f"accuracy_first_4: {accuracy_first_4}")

correct_first_5 = pos_c['1'] + pos_c['2'] + pos_c['3'] + pos_c['4'] + pos_c['5']
incorrect_first_5 = pos_inc['1'] + pos_inc['2'] + pos_inc['3'] + pos_inc['4'] + pos_inc['5']
accuracy_first_5 = 100 * correct_first_5 / (correct_first_5 + incorrect_first_5)
print(f"accuracy_first_5: {accuracy_first_5}")
