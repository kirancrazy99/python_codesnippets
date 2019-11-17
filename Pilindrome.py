def is_pilindrome(string):
    reverse=string[::-1]
    if string==reverse:
        print("Given string is pilindrome")
    else:
        print("Given string is not pilindrome")


is_pilindrome("racecar")