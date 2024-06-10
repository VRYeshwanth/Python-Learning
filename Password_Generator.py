import random
def create_password(l,ch,n):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special = "@#$&*():;.,`/~-=+"
    total = ""
    s = set(ch)
    if '1' in s:
        total += uppercase
    if '2' in s:
        total += lowercase
    if '3' in s:
        total += numbers
    if '4' in s:
        total += special
    
    for i in range(n):
        passw = ""
        for j in range(l):
            passw += random.choice(total)
        print(passw)

def check_valid(ch):
    if ch.isdigit():
        l = [int(i) for i in ch]
        for i in l:
            if not (i>=1 and i<=4):
                print("ERROR : Numbers from 1 - 4 only are allowed")
                exit(0)
        return True
    else:
        print("ERROR : Numbers only !!!!!")
        exit(0)

print("Welcome to password Generator")
ch = input("Enter a combination of numbers from 1-4 to choose from uppercase, lowercase, numbers and special characters : ")
if check_valid(ch):
    len = int(input("Enter the length of your password : "))
    n = int(input("Enter the number of passwords to be generated : "))
    create_password(len,ch,n)