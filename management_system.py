
class contact:
    li=[]
    li2=[]

    def input():
        contact.li.clear()
        contact.li2.clear()
        for i in range(10):
            name=input("Enter the name --> ")
            number=input("Enter the number --> ")
            contact.li.append(name)
            contact.li2.append(number)
        print("Contacts saved.")

class new_account(contact):
    def input():
        name=input("Enter the new name --> ")
        number=input("Enter the new number --> ")
        contact.li.append(name)
        contact.li2.append(number)
        print("New account added.")

class edit_account(contact):
    def input():
        way=input("Edit by name or number? (name/number) --> ")
        if way=="name":
            old=input("Enter current name --> ")
            if old in contact.li:
                index=contact.li.index(old)
                contact.li[index]=input("Enter new name --> ")
                print("Name updated.")
            else:
                print("Not found!")
        elif way=="number":
            old=input("Enter current number --> ")
            if old in contact.li2:
                index=contact.li2.index(old)
                contact.li2[index]=input("Enter new number --> ")
                print("Number updated.")
            else:
                print("Not found!")

class search(contact):
    def input():
        way=input("Search by name or number? (name/number) --> ")
        if way=="name":
            name=input("Enter name --> ")
            if name in contact.li:
                i=contact.li.index(name)
                print(contact.li[i], contact.li2[i])
            else:
                print("Not found!")
        elif way=="number":
            num=input("Enter number --> ")
            if num in contact.li2:
                i=contact.li2.index(num)
                print(contact.li[i], contact.li2[i])
            else:
                print("Not found!")

class delete_account(contact):
    def input():
        name=input("Enter the name to delete --> ")
        if name in contact.li:
            i=contact.li.index(name)
            contact.li.pop(i)
            contact.li2.pop(i)
            print("Deleted.")
        else:
            print("Not found!")

class list_account(contact):
    def output():
        if len(contact.li)==0:
            print("No contacts.")
        else:
            for i in range(len(contact.li)):
                print(contact.li[i], "-", contact.li2[i])

while True:
    print("\n1-Fill contacts")
    print("2-New account")
    print("3-Edit account")
    print("4-Search")
    print("5-Delete")
    print("6-List")
    print("7-Exit")

    choice=input("Enter your choice --> ")

    if choice=="1":
        contact.input()
    elif choice=="2":
        new_account.input()
    elif choice=="3":
        edit_account.input()
    elif choice=="4":
        search.input()
    elif choice=="5":
        delete_account.input()
    elif choice=="6":
        list_account.output()
    elif choice=="7":
        print("Goodbye!")
        break
    else:
        print("Error!")
