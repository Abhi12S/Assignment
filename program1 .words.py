word = "which is better python 2 or python 3"
list_a = word.split()
list_a = sorted(list_a)

count = 0
result = []
for char in list_a:
    count = list_a.count(char)
    pair = (char, count)
    if (pair not in result):
        result.append(pair)
    count = 0

for res_pair in result:
    print(res_pair)
