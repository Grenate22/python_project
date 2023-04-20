#! python3
#this program is how database works
#first create empty dictionary
friends={}
#ask the owner to input his prsonal details
#we set the personal detials he input as default profile just like how phonebook works on our phone
personal_name=input('Enter your personal name: ')
friends.setdefault(personal_name, 'myself')
while True:
    print('Enter a name to check your relation with me: (blank to quit)')
    name=input()
    if name=="":
        break
    if name in friends:
        #we check maybe the value exist in the database already if not you have to input yourself
        print(friends[name].title(),'is your relation to me')
    else:
        print('you have to declare yourself first')
        print('who are you to me? ')
        relation=input()
        friends[name]=relation
        print('your relation to me have been updated')