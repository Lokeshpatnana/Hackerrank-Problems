""" 
Before the oubreak of corona virus to the world, a meeting happened in a room in Wuhan. A person who attended that meeting had COVID-19 and no one in the room knew about it! So everyone started shaking hands with everyone else in the room as gesture of respect and after meeting unfortunately every one got infected! Given the fact that any two persons shake hand exactly once, Can you tell the total count of handshakes happened in that meeting?

Input Format:
contains an integer N, the total number of people attended that meeting.

Output Format:
Print the number of handshakes.

Example 1: Input:5 Ouput:10
Example 2: Input:10 Output:45
"""
"""Solution"""

"""Method - I"""
def shakeHands(N):
    hs = (N * (N - 1)) // 2
    return hs
    
N = int(input("Persons Attended Meeting:"))
output = shakeHands(N)
print(output)


"""Method - II"""
import math as m 
def shakeHands(N):
    hs = m.comb(N,2)
    return hs
    
N = int(input("Persons Attended Meeting:"))
output = shakeHands(N)
print(output)