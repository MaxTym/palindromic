string1 = ''

def read_file(string1):
    string1 = open('newfile.txt', 'r')
    return string1.read()

def is_palindrome(string1):
    new_str = ''
    string2 = read_file(string1)
    print(string2)
    for l in string1:
        if l.isalpha():
            new_str += l
    string2 = new_str[::-1]
    print(string2)
    if new_str.lower() == string2.lower():
        return True
    else:
        return False

def main(string1):
    #string1 = input("Enter some text: ")
    #read_file(string1)
    #print(read_file(string1))
    if is_palindrome(string1) is True:
        print("It is a polindrome")
    else:
        print("It's not a polindrome")

main(string1)
