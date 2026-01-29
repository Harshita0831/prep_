#ATM SIMULATOR
#load_data - loads old balance & pin
#save_data - saves current data
#check_balance - Shows balance
#deposit_money - Adds money
#witdraw_money - Removes money
#change_pin - Updates pin
#main - Controls Program
#pass - it does nothing just used to avoid syntax error

#ATM SIMULATOR
file_name = "atm_data.txt"
#balance is a global variable that stores money
balance = 1000
#pin is a global variable that stores ATM pin
pin = "1234"
#LOAD DATA
def load_data():
    global balance, pin             #global keyword allows us to modify outside variables
    try:
        #open a file in read mode
        file = open(file_name,"r")
        #read all lines from the file into a list
        lines = file.readlines()
        #close the file after reading
        file.close()
        #first line contains pin, strip removes \n
        pin = lines[0].strip()
        #second line contains balance
        balance = int(lines[1].strip())
    except:
        #if file does not exist error occurs
        #pass means do nothing
        #program will use default balance and pin
        pass
#CHECK BALANCE
def check_balance():
    print("Your balance is: ",balance)
  
#SAVE DATA
def save_data():
    #opening a file in write mode
    file = open(file_name, "w")
    #write a pin into the file and go to next line
    file.write(pin+"\n")
    #write balance as string
    file.write(str(balance))
    #close the file
    file.close()

#DEPOSIT MONEY
def deposit_money():
    #global allows changing original balance
    global balance
    try:
        amount = int(input("Enter amount to deposit: "))
        balance = balance+amount
        #save updated balance to the file
        save_data()
        print("Money Deposited Successfully")
    except:
        print("Please enter numbers only")


#WITHDRAW MONEY
def withdraw_money():
    global balance
    try:
        amount = int(input("Enter the amount to withdraw: "))
        if amount>balance:
            print("Insufficient Balance!!")
        else:
            balance = balance-amount
            save_data()
            print("Please collect your cash")
    except:
        print("Please enter number only")

#CHANGE PIN
def change_pin():
    global pin
    #ask user for old pin
    old_pin = input("Enter the old pin: ")
    #check if old pin matches
    if old_pin == pin:
        #ask for new pin
        new_pin = input("Enter the new pin: ")
        pin = new_pin
        save_data()
        print("Pin changed successfully")
    else:
        print("Incorrect PIN")

#MAIN
def main():
    #load data
    load_data()
    #ask user to enter pin
    user_pin = input("Enter the pin: ")
    #if pin is wrong stop the program
    if user_pin != pin:
        print("Incorrect PIN")
        return
    while True:
        print("\n-------ATM MENU--------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("Thank you for using ATM")
            break
main()


































        






















