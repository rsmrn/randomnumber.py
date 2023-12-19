import random
#Task 1 Guess the number using user input
def guess_random_number(tries,start,stop):
    target_number = random.randint(start,stop)
    while tries != 0:
        print("Number of tries left:",tries)
        user_guess = int(input(f"Guess a number between {start} and {stop}: "))
        if user_guess == target_number:
            print("You guessed the correct number.")
            return
        elif user_guess < target_number:
            print("Guess higher!")    
        elif user_guess > target_number:
            print("Guess lower!")    
        tries -= 1
    print("You have failed to guess the number:",target_number)    

#Task 2 using Linear Search        
def guess_random_num_linear(tries, start, stop):
    target = random.randint(start, stop)
    print("The number for the program to guess is : ", target) 
    for i in range(start, stop+1):
        print("The program is guessing:", i)  

        if i == target:
            print("The program has guessed the correct number." )
            return

        print("Number of tries left: ",tries)
        tries -= 1

        if tries == 0:
            print("The program has failed to guess the correct number.")
            return

#Task 3 using Binary Search      
def guess_random_num_binary(tries,start,stop):
    target_number = random.randint(start,stop)
    print("Random number to find",target_number)
    lower_bound = start
    upper_bound = stop
    for i in range(start,stop):
        guess = (lower_bound + upper_bound) // 2
        if guess == target_number:
            print("Found it!", target_number)
            return
        elif guess < target_number:
            print("Guessing lower!")
            lower_bound = guess + 1
        else:
            print("Guessing higher!")
            upper_bound = guess - 1
    print("Your program failed to find the number.")



"""Driver code for Task 1"""
#guess_random_number(5,0,10)

"""Driver code for Task 2"""
#guess_random_num_linear(5,0,10)


guess_random_num_binary(5,0,100)







