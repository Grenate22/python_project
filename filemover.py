import os,shutil
for filename in os.listdir('C:/Users/Big P stark/Desktop/roadmap'):
    if filename.endswith('.txt'):
        shutil.move('C:/Users/Big P stark/Desktop/roadmap/%s' %(filename),'C:/Users/Big P stark/Desktop/roadmap/textfile')
        #print('C:/Users/Big P stark/Desktop/roadmap/%s' %(filename))