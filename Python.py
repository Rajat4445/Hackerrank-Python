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
