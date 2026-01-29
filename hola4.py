contact = {}
while True:
    print("\n----Contact Book----")
    print("1. Add Contact")
    print("2.View Contact ")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice here")

    #for adding contacts
    if choice == "1":
        name = input("Enter Name: ")
        #contact[name] = phone
        print("Contact added successfully")
        
    #for view contact
    elif choice == "2":
        if contact:
            print("\nSaved Contact: ")
            for name, phone in contact.items():
                print(name,":", phone)
        else:
            print("No contact found")

    #for search contact
    elif choice == "3":
        name = input("Enter name to search:")
        if name in contact:
            print("Phone number: ", contact[name])
        else:
            print("Contact not found")
            
    #delete contact
    elif choice == 4:
        name = input("Enter the name you want to delete: ")
        if name in contact:
            del contact[name]           #or contact.pop(name)
            print("Contact deleted")
        else:
            print("Contact not Found")
            
    #exit
    elif choice == 5:
        print("Thank you for using contact book")
        break
    else:
        print("Invalid choice!! Please Try again")
    
