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
 
