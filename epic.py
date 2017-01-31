string1 = ''

def readbyblock(f):
    while True:
        block = []
        for line in f:
            if line = '----\n':
                break
                block.append(line)
        if not block:
            break
        yield block

def read_file(string1):
    inFile = open("newfile.txt")
    string1 = ''
    for line in inFile:
        string1 += line
    return string1
    print(string1)
    inFile.close()

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

def main():
    #string1 = input("Enter some text: ")
    #read_file(string1)
    #print(read_file(string1))
    if is_palindrome(string1) is True:
        print("It is a polindrome")
    else:
        print("It's not a polindrome")

main()
