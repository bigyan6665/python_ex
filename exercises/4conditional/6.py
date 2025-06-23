string = input("Enter string = ")
string_rev = string[::-1]
if(string_rev == string):
    print(f"{string} is palindrome")
else:
    print(f"{string} isnot palindrome")