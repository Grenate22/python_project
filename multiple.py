def  odd_number(number):
        for num in range(1,number+1):
            if num%2!=0 :
                odd_numbe.append(num)

            if num%2==0:
                even_numbe.append(num)

odd_numbe=[]
even_numbe=[]
numb=int(input('Enter a number: '))
(odd_number(numb))
# i decided to write the below code in this format to see the function of f string from the normal way
print(f"This are the odd_number in {numb} \n  {odd_numbe}")
print("This are the even_number in "+str(numb)+"\n" +str(even_numbe))
