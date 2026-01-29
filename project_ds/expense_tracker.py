#EXPENSE TRACKER PROJECT

#FLOW
#start
#load the old expense from the file
#show menu
#1. Add  expense
#2. view expense
#3. Toatal expense
#4. exit
#user selects one option
#function runs
#save data
#repeat
#"Food":500, "Clothes":1000, "Chores":250


#Functions
#load_data-> reads old expense from file
#save_data-> saves expense to file
#add_expense ->take new expense
#view_expense -> show all expense
#total_expense ->calculates expense
#main -> controls the program


#Code
file_name = "expenses_data.txt"
expenses = []

#Load data
def load_data():
    global expenses
    try:
        file = open(file_name,"r")
        lines = file.readlines()
        file.close()
    for line in lines:
        line = line.strip()
        amount, category, note = line.split(",")      #variables
        expense ={"amount":int(amount), "category":category,"note":note}
        expenses.append(expense)
    except:
        pass
#Save expense
def save_expense():
    file = open(file_name,"w")
    file.write(int(expense))
    file.close()

#add expense
def add_expense():
    global expenses
    




















    
