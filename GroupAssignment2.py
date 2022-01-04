import random

amountStudents = 5
amountQuestions = 4
f = open("TestResults.txt", 'w')

for i in range(amountStudents):
    status = True
    statustwo = True
    correct = 0
    while(status==True):
        name = input('Enter the name of the student: ')
        if(len(name) != 0):
            status = False
        else:
            print('No input detected: Please enter a name.')
    while(statustwo==True):
        grade = input('Enter the students grade level (1, 2 or 3): ')
        if ((grade == "1") or (grade == "2") or (grade == "3")):
            statustwo = False
        else:
            print('Incorrect: Please choose from grades 1, 2 or 3.')

    for j in range(amountQuestions):
       #Get the answer from user and convert to integer
        if (grade == "1"):
            #Input 2 random numbers for addition
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            answer = input('What is the sum of ' + str(x) + ' & ' + str(y) + ' = ')
            if answer.isdigit():

                answer = int(answer)
                #if answer is correct, increment the correct answer count
                if x+y == answer:
                    print('Hurray.')
                    correct += 1
            else:
                answer = 0
                print('Incorrect: Please enter numbers.')
        if (grade == "2"):
            #Input 2 random numbers for multiplication
            x = random.randint(1, 30)
            y = random.randint(1, 10)
            answer = input('What is ' + str(x) + ' multiplied by ' + str(y) + ' = ')
            if answer.isdigit():
                answer = int(answer)
                #if answer is correct, increment the correct answer count
                if x*y == answer:
                    print('Hurray.')
                    correct += 1
            else:
                answer = 0
                print('Incorrect: Please enter numbers.')
        if (grade == "3"):
            #Input 2 random numbers for division
            x = random.randint(20, 100) * 2
            y = random.randint(1, 5) * 2
            answer = input('What is ' + str(x) + ' divided by ' + str(y) + ' = ')
            if answer.isdigit():
                answer = int(answer)
                #if answer is correct, increment the correct answer count
                if x/y == answer:
                    print('Hurray.')
                    correct += 1
            else:
                answer = 0
                print('Incorrect: Please enter numbers.')

    #write the result to the file for each student
    f.write(name + ' ' + str(correct)+'\n')

    #print the correct result, for debugging purpose, this line can be removed
    print(correct)
    
f.close()

#Reopen the file in read mode
f = open('TestResults.txt', 'r')

#initialize the winner record
maximum = 0
n = ''
for line in f:

    #read the file line by line, and split using space
    s = line.split(' ')
    name, correct = s[0], int(s[1])

    #if current record is better than maximum, update the winner information
    if correct>maximum:
        n = name
        maximum = correct
f.close()

#Output the winner information
print('The winner is ' + n + ' with ' + str(maximum) + ' correct answers.')

