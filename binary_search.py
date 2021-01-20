#Binary Search Example - Evan Dieterich 

#Take user input as number between 1 and 100, instruct user to input h if guess is too high and l if guess is too low
x = int(input('Think of a number between 1 and 100: '))
print('Enter H if the guess is too high or L if the guess is too low.')

#Binary search function that halves the guessing range based on user input interatively, returns users number and number of iterations
def guess_num(x):
    step = 0
    low = 1
    high = 100
    ans = (low + high) // 2
    
    while x != ans:
        step += 1
        print('Is the number ' + str(ans))
        guess = input()

        if guess.lower() == "h":
            high = ans
            ans = (low + high) // 2
        elif guess.lower() == "l":
            low = ans
            ans = (low + high) // 2
            
    return print('The number is', ans, '.', 'It took me', step, 'guesses.')

#Call to binary search function that takes in user input as paramater
guess_num(x)
    



