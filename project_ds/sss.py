file_name = "atm_dat.txt"
balance = 1000
pin = "1234"
def load_data():
    global balance, pin
    try:
        file = open(file_name,"r")
        line = file.readlines()
        file.close()
        pin = lines[0].strip()
        balance = int(lines[1].strip())
    except:
        pass
def check_balance():
    print("Your balance is: ", balance)
def save_data():
    try:
        file = open(file_name,"w")
        file.write(pin+"\n")
        file.write(str(balance))
        file.close()
def deposit_money():
    global balance
    try:
        amount = int(input("Enter amount: "))
        balance = balance+amount
        save_data()
        print("Money deposited successfully")
        
