def recursion(string1):
    if len(string1) == 0:
        return string1
    else:
        return string1[-1] + recursion(string1[0:-1])

def is_palindrome(string1):
    new_str = ''
    new_str1 = ''
    for l in string1:
        if l.isalpha():
            new_str1 += l
    rev_string = recursion(string1)
    for l in rev_string:
        if l.isalpha():
            new_str += l
    if new_str1.lower() == new_str.lower():
        return True
    else:
        return False

def main():
    string1 = input("Enter some text: ")
    if is_palindrome(string1) is True:
        print("It is a palindrome")
    else:
        print("It's not a palindrome")

main()
