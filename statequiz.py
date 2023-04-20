import random
#first import the module random
#after that put the state and capital in a dictionary so you can acess them seperately when you need either the state or the capital
nigeria={'Abia':'Umuahia','Adamawa':'Yola','Akwa Ibom':'Uyo','Anambra':'Awka','Bauchi':'Bauchi','Bayelsa':'Yenagoa',
'Benue':'Makurdi','Borno':'Maiduguri','Cross River':'Calabar','Delta':'Asaba','Ebonyi':'Abakaliki','Edo':'Benin City',
'Ekiti':'Ado Ekiti','Enugu':'Enugu','Gombe':'Gombe','Imo':'Owerri','Jigawa':'Dutse','Kaduna':'Kaduna','Kano':'Kano','Katsina':'Katsina',
'Kebbi':'Birnin Kebbi','Kogi':'Lokoja','Kwara':'Ilorin','Lagos':'Ikeja','Nasarawa':'Lafia','Niger':'Minna','Ogun':'Abeokuta',
'Ondo':'Akure','Osun':'Oshogbo','Oyo':'Ibadan','Plateau':'Jos','Rivers':'Port Harcourt','Sokoto':'Sokoto','Taraba':'Jalingo','Yobe':'Damaturu',
'Zamfara':'Gusau','Federal Capital Territory':'Abuja'}
"""
we create two file for the question and file respestively in a write mode and they are to loop 20 times
and we make a header for it by writing to the question file
"""
for quiznum in range(20):
    quizfile=open('capitalquiz%s.txt' %(quiznum+1),'w')
    answerfile=open('capitalquiz_answer%s.txt' %(quiznum+1),'w')
    quizfile.write('name:\n\nDate:\n\ndepartment:\n\n')
    quizfile.write((' '*20)+'state capitals quiz (form %s)' %(quiznum+1))
    quizfile.write('\n\n')
    states=list(nigeria.keys())
    random.shuffle(states)
#we loop 37 times in the first loop that's nested loop
    for questionNum in range(37):
        """
        we create a variable correct answer that will get the corresponding value of the index state
        then a variable wrong answer that will get all list of the values i.e the capital
        then we delete the index of the correct answer from the variable so we an get only the wrong answer 
        then we randomise the wrong answer with sample in range 3
        after then we add the correct answer to the wrong answer so we can make a perfect answer option
        and shuffle it so the correct answer will not keep coming last
        """

        correctanswer=nigeria[states[questionNum]]
        wrongAnswer=list(nigeria.values())
        del wrongAnswer[wrongAnswer.index(correctanswer)]
        wrongAnswer=random.sample(wrongAnswer,3)
        answeroption=wrongAnswer+[correctanswer]
        random.shuffle(answeroption)
        print(states[questionNum])
        print(answeroption)
        print(correctanswer)
        #we then write to the quizfile we open before the stat
        quizfile.write('%s. What is the capital of %s?\n' % (questionNum+1,states[questionNum]))
        for i in range(4):
            quizfile.write('%s. %s\n'% ('ABCD'[i],(answeroption)[i]))
        quizfile.write('\n')
        answerfile.write('%s . %s %s\n' %(questionNum+1,'ABCD'[answeroption.index(correctanswer)],correctanswer))

    quizfile.close()
    answerfile.close()



