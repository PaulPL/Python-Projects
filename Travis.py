known_users = ["Alice", "Bob", "Clarie", "Dan", "Emma", "Fred", "Gorgie", "Harry"]
print(len(known_users))

while True:
    print("Hi! My name is Travis")

    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the list (y/n)?: ").strip().lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No problem, I did not want you to leave")
            
        
    else:
        print("Hello {}!".format(name))
        add = input("Would you like to be addet to the list (y/n)?: ").strip().lower()
        if add == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add == "n":
            print("No worries, see you around!")
            

    
    

