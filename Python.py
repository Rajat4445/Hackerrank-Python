## Finding the Percentage ## 
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()                     ## Predefined
    
    sum = 0
    
    values = student_marks[query_name]                 ## Gives the values attached to the key query_name
    
    for i in values:
        sum += i                                    ## Finds the sum of the values
        
    average = sum/len(values)
    
    print('%.2f' % average)              ## Precision to 2 places of decimal
 

## Text Wrap ##
# You are given a string  and width . Your task is to wrap the string into a paragraph of width .

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)               ## This wraps the string wrt width

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
 ## Guide to textwrap function
#Textwrap
#The textwrap module provides two convenient functions: wrap() and fill().
#textwrap.wrap() 
#The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. 
#It returns a list of output lines.
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 
#textwrap.fill() 
#The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.


## Swap Case ##
#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#For Example:
#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2  
#Function Description
#Complete the swap_case function in the editor below.
#swap_case has the following parameters:
#string s: the string to modify
#Returns
#string: the modified string

def swap_case(s):
    
    char = []                        ## Taking all the characters of the string
    for i in range(len(s)):
        char.append(s[i])               ## Appendig all the characters of the string to the emptry list
        
    new_char = []                 ## Appending all the swapped characters to the new empty list
        
    for j in char:
        if j == j.lower():         ## If character is lowercase
            j = j.upper()               ## Convert it to upper
            new_char.append(j)          ## And append to the final list
            
        elif j == j.upper():             ## If character is uppercase
            j = j.lower()               ## Convert it to lower
            new_char.append(j)           ## And append to the final list
            
        else:                           ## Otherwise just append the character to the list
            new_char.append(j)
            
    final = ''.join(new_char)            ## Join all the characters to form a single string which basically has swapped characters
    
    return final                       ## Return the swapped string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

    
 ## Mutations ##

#We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
#Let's try to understand this with an example.
#You are given an immutable string, and you want to make changes to it.

def mutate_string(string, position, character):
    
    string = string                          ##making a variable string
    
    char = []                           ## Empty list which will store all the characters in the string
    
    for i in range(len(string)):  
        char.append(string[i])                 ## Appending all the characters of the string to the empty list
        
    char[position] = character                ## Assigning the value in the string to the new character
    
    final = ''.join(char)                ## Making the final string
    
    return final                  ## Returns the modified string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)



