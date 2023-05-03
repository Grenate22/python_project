no_stud = int(input('no of student record: '))
dict = {}
for i in range(no_stud):
    name_of_stud = input('name of student ')
    score_of_stud = list(map(int, input("Enter multiple values: ").split()))
    dict[name_of_stud] = score_of_stud

print(dict)
query_name = input('the name of student to query: ')

query=dict[query_name]
counter=[]
total=0
for val in query:
    counter.append(val)
    total=total+val

print(query)
print(total)
print(total/len(query))