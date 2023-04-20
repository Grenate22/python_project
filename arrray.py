dict = {}
for _ in range(int(input('input a number'))):
    name = input('enter a name')
    score = float(input('input a figure'))
    dict[name] = score

print(dict)
sorting=[]
for value in dict.values():
    sorting.append(value)
print(sorting)
new_value=list(set(sorting))
print(new_value)
new_value.sort()
print(new_value)
second_lowest=new_value[1]
print(second_lowest)


