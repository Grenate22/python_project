from collections import Counter
#this program is use to count occurance in an array
array=['white','blue','green','blue','red','white','green','white','red','white']
colors={}
for color in array:
    if color not in colors:
        colors[color]=1
    else:
        colors[color]+=1
print(colors)
sum = 0
for k in colors:
    sum+=k
print(sum)
#another format to work with counter
c=Counter(array)
print(c)