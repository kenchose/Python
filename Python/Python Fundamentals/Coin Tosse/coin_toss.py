import random

print 'Starting the program...'


def coin_toss(num):
    heads = 'heads'
    tails = 'tails'
    tails_count = 0
    heads_count = 0
    total_count = 1
    coin_toss(i)
    for num in range (0, 5001):
        random_num = random.random()
        i = random_num * 100       
        if i <= 50:
            tails_count += 1
            print "Attempt #" + str(total_count) + " Throwing a coin... It's a tail!... Got " + str(heads_count) + " head(s) so far and " 
            + str(tails_count) + "tail(s) so far."
        else:
            heads_count += 1
            print "Attempt #" + str(total_count) + " Throwing a coin...It's a head!... Got " + str(heads_count) + " head(s) so far and " 
            + str(tails_count) + "tail(s) so far. "
    coin_toss(i)






    
   

    
