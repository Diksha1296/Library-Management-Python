def book1():
     print("The book Name is 'The Book of Thanks'")
     print("The Author name is Ralph Waldo Emerson")
     print("The launch date is 23rd May 2024")
     print("The Publisher of book is:Fingerprint!Pub")
     print("The price is INR 199.")
     return exit()

def book2():
    print("The book Name is 'Be Kind'")
    print("The Author name is Robert Green Ingersoll")
    print("The launch date is 30th May 2024")
    print("The Publisher of book is:Fingerprint!")
    print("The price is INR 119.")
    return exit()

def book3():
    print("The book Name is 'The Power of the subconscious Mind'")
    print("The Author name is ROGER FRITZ")
    print("The launch date is 1st September 2019")
    print("The Publisher of book is:Fingerprint!Publishing")
    print("The price is INR 139.") 
    return exit()
     
    





def lib():
    a=int(input("Press 1 for Book info. and 2 for exit:"))
    if(a==1):
        b=int(input("Enter 101 for Book info of 'The Book of Thanks' "
                    "\nEnter 102 for Book info of 'Be Kind'"
                    "\nEnter 103 for Book info of 'The Power of the subconscious Mind'"
                    "\nEnter 4 for exit :"))
        if(b==101):
            return book1()
        elif(b==102):
            return book2()
        elif(b==103):
            return book3()
        else:
            print("Thankyou For Visiting Skill Circle library Sysytem !!!")
    else:
        print("Thankyou For Visiting Skill Circle library")


def exit():
    c=int(input("Do you want to continue or exit??"
           "\nPress 1 for continue and 0 for exit:"))
    if(c==1):
         return lib()
    else:
         print("!!!THANKYOU FOR VISITING SKILL CIRCLE LIBRARY SYSTEM!!!")
         

print("---Welcome to the Skill Circle Library System---")
lib()