string1 = ''

def is_palindrome(string1):
    new_str = ''
    string2 = ''
    for l in string1:
        if l.isalpha():
            new_str += l
    string2 = new_str[::-1]
    if new_str.lower() == string2.lower():
        return True
    # else:
    #     return False

def main(string1):
    string1 = input("Enter some text: ")
    if is_palindrome(string1) is True:
        print("It is a polindrome")
    else:
        print("It's not a polindrome")

main(string1)
