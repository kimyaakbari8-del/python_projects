import random
def fact():
    x=random.randint(1,50)
    tries=1
    n=int(input("enter your geust"))
    while x!=n:
        if x>n:
          print("bigger")
        elif x<n:
            print("smaller")
        n=int(input("enter again"))
        tries += 1
    if x==n:
        print("perfect")
        print("tries:",tries)
fact()
print("do you want to play again?")
print("enter yes or nope!")
a=input(">>>")
if a=="nope":
    print("okay bye")
elif a=="yes":
    while a=="yes":
        fact()
        print("do you want to play again?")
        print("enter yes or nope!")
        a=input(">>>")
if a=="nope":
    print("okay bye")
        


