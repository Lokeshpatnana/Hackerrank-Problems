""" 
Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment problems before the lecture. Today he got one tricky question. The problem statement is "A postive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits".

Example:
Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents "5". Hence output will print "5".
"""

"""Solution"""

decimal_value = int(input("Enter Decimal Value:"))
binary_value = bin(decimal_value)[2:]
toggle_value = ""
for i in binary_value:
    if (i == '1'):
        toggle_value += '0'
    else:
        toggle_value += '1'

int_value_after_toggle = int(toggle_value,2)
