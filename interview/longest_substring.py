temp_str = []

string = "abcabde"

for i in range(len(string)):
    temp_str.append(string[i])
    if len(set(temp_str)) == len(temp_str):
        continue
    else:
        temp_str.clear()

print(temp_str)