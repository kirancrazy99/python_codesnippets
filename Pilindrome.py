import sys
import os

def is_pilindrome(string):
    reverse=string[::-1]
    if string==reverse:
        print("Given string is pilindrome")
    else:
        print("Given string is not pilindrome")

        
user_input = os.environ.get('user_input')    
is_pilindrome(user_input)
