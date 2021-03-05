
"""Write a function named test_sqrt that prints a table like the following using a while loop, where "diff" is the absolute value of the difference between my_sqrt(a) and math.sqrt(a). 

a = 1 | my_sqrt(a) = 1 | math.sqrt(a) = 1.0 | diff = 0.0
a = 2 | my_sqrt(a) = 1.41421356237 | math.sqrt(a) = 1.41421356237 | diff = 2.22044604925e-16
a = 3 | my_sqrt(a) = 1.73205080757 | math.sqrt(a) = 1.73205080757 | diff = 0.0
a = 4 | my_sqrt(a) = 2.0 | math.sqrt(a) = 2.0 | diff = 0.0
a = 5 | my_sqrt(a) = 2.2360679775 | math.sqrt(a) = 2.2360679775 | diff = 0.0
a = 6 | my_sqrt(a) = 2.44948974278 | math.sqrt(a) = 2.44948974278 | diff = 0.0
a = 7 | my_sqrt(a) = 2.64575131106 | math.sqrt(a) = 2.64575131106 | diff = 0.0
a = 8 | my_sqrt(a) = 2.82842712475 | math.sqrt(a) = 2.82842712475 | diff = 4.4408920985e-16
a = 9 | my_sqrt(a) = 3.0 | math.sqrt(a) = 3.0 | diff = 0.0 

Modify your program so that it outputs lines for a values from 1 to 25 instead of just 1 to 9. 
    """
import math

def mysqrt(a):    
    x = a/2
    while True:
        estimated_root = (x + a/x) / 2
        if estimated_root == x:
            return estimated_root
            break
        x = estimated_root

def test_sqrt(list_of_a):
    """the function calculates the square root"""
    first_column = "a"
    sec_column = "mysqrt(a)"
    third_column = "math.sqrt(a)"
    fourth_column = "diff"
    
    spacing1 = " "
    spacing2 = " " * 4
    spacing3 = ""
    
    print(first_column, spacing1, sec_column, spacing2, third_column, spacing3, fourth_column)
    print("-" + "     " + "---------" + "    "+ "--------" + "   " + "----")
    
    for a in list_of_a:
        row1 = float(a)
        row2 = mysqrt(a)
        row3 = math.sqrt(a)
        row4 = abs(mysqrt(a) - math.sqrt(a))

        print(row1, "{:<15f}".format(row2), "{:<13f}".format(row3), row4)

test_sqrt(range(1,26))
