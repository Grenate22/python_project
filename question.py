from Classtutor import student
print("Welcome to your CBT exam at peter forum")
question_prompt=[
    "How many state do we have in nigeria?\n (a)30\n (b)34\n (c)28\n (d)36\n\n",
    "what is the capital OF nigeria?\n (a)Lagos\n (b)Ekiti\n (c)Abuja\n (d)kano\n\n",
    "Nigeria is in what continent?\n (a)Africa\n (b)Asia\n (c)Europe\n (d)North america\n\n",
    "What is the capital of ondo?\n (a)Lagos\n (b)Bauchi\n (c)Jalingo\n (d)Akure\n\n"

]
questions=[
    student(question_prompt[0],"d"),
    student(question_prompt[1],"c"),
    student(question_prompt[2],"a"),
    student(question_prompt[3],"d")
]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print(name+" Thank you for participating in our CBT exam\nYour score for the exam is "+ str(score) +"/"+str(len(question_prompt))+" correct")

name=input("Your full name:" )
Age=int(input("Your age:" ))
if Age>=18:
    print("You are qualified for this exam")
    print(name+" Your CBT will start now ")
    run_test(questions)
else:
    print("You are not up to 18 years you can't participate in this CBT exam")


