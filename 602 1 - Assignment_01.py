#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = input('Enter the score for test 1: ')
test2 = input('Enter the score for test 2: ')
test3 = input('Enter the score for test 3: ')
# Needed to add test3 variable allowing value input by the user

# Calculate the average test score.
average = (float(test1) + float(test2) + float(test3)) / 3
    #Remove indent before average, Treat test numbers as number, Added parentheses around sum of test scores otherwise order of operations would cause only test3 to be divided by 3 and then summing that value with test1 and test2
    
# Print the average.
print('The average score is', str(average))
    #Added converting average variable to a string as required by the print function

# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE:
    #Changed variable name to uppercase letters since that the variable created on line 7
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
rect1_width = input('Enter the width for rectangle 1: ')
rect1_length = input('Enter the length for rectangle 1: ')
rect2_width = input('Enter the width for rectangle 2: ')
rect2_length = input('Enter the length for rectangle 2: ')

rect1_area = float(rect1_length)*float(rect1_width)
rect2_area = float(rect2_length)*float(rect2_width)

print('The areas of rectangles 1 and 2 are ',str(rect1_area),' and ',str(rect2_area))

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  
first_name = input('Enter your first name: ')
age = input('What is your age: ')
      
#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
print('Happy birthday ',first_name,'! You are ', str(age), ' years old today!')

