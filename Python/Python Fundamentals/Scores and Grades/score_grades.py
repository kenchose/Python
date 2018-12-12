import random

print 'Scores and Grades'
def scores_grades(num):
    if num >= 90:
        print 'Score: ' + str(num) + ';' + 'Your grade is A.'
    elif num >=80:
        print 'Score: ' + str(num) + ';' + 'Your grade is B.'
    elif num >= 70:
        print 'Score: ' + str(num) + ';' + 'Your grade is C.'
    else:
        print 'Score: ' + str(num) + ';' + 'Your grade is D.'

for i in range (0, 10):
    random_num = random.random()
    i = random_num * 100
    scores_grades(i)

print 'End of the program. Bye!'