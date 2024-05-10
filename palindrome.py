# This is the string that read same from backward and forward, example racecar
# The matching is done by looking on the characters 
def is_palindrome(text):
    length=len(text)
    for i in range(0, length//2):
        if (text[i] != text[length-i-1]):
            return False
        else:
            return True
print(is_palindrome("racecar"))
print(5//2)