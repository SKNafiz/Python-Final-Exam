banks_balance = 0

def bank_balance(customer_balance, number):
    global banks_balance  
    if number == 1:
        banks_balance = banks_balance + customer_balance
    if number == 2:
        banks_balance = banks_balance - customer_balance
    return banks_balance  


class Person:
    def __init__(self, name, email, address, account_number, balance, transaction_history, loan):
        self.name = name
        self.email = email
        self.address = address
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = transaction_history
        self.loan = loan
    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Number: {self.account_number}\nBalance: {self.balance}\nTransaction History: {self.transaction_history}\nLoan: {self.loan}"

current_account_people_list=[]
saving_account_people_list=[]
people_list = []
admin_list=[]
loans=[]
options = 0

class Sign_Up_Customer:
    def sign_up(self):
        Which_Account = int(input("\nWhat Kind of Account Do You Want to Open?\n-->'1' For Current Account & '2' For Saving Account: "))
        name = input("->Enter Your Name: ")
        email = input("->Enter Your Email: ")
        address = input("->Enter Your Address:")
        account_number = name + email
        balance = 0
        loan = 0
        transaction_history = []
        person = Person(name, email, address, account_number, balance, transaction_history, loan=loan)
        if Which_Account == 1:
            current_account_people_list.append(person)
        elif Which_Account == 2:
            saving_account_people_list.append(person)
        people_list.append(person)
        print("-->Successfully Created an Account!")

sign_up_customer = Sign_Up_Customer()

class Log_in_Customer:
    def __init(self):
        self.logged_in_customer = None

    def log_in_customer(self):
        check_email = input("Enter Your Email: ")
        found = False
        
        for email in current_account_people_list:
            if email.email == check_email:
                print("\n-->You Have a Current Account!")
                self.logged_in_customer = email
                customer_modification.modification(self.logged_in_customer)
                found = True
                break
        
        if not found:
            for email in saving_account_people_list:
                if email.email == check_email:
                    print("\n-->You Have a Saving Account!")
                    self.logged_in_customer = email
                    customer_modification.modification(self.logged_in_customer)
                    found = True
                    break
        
        if not found:
            print("\n-->You Don't Have Any Account. You Have to Sign Up First...")
            sign_up_customer.sign_up()

log_in_Customer = Log_in_Customer()

class Customer_modification:
    global options
    def modification(self, customer):
        num = int(input("To Deposit Press '1'\nTo Withdraw Press '2'\nTo Check Available Balance Press '3'\nTo See Transaction History Press '4'\nTo Take Loan Press '5'\nTo Transfer Money to Another Account Press '6': "))
        if num == 1:
            print("\n-->Your Current Balance is", customer.balance)
            amount = int(input("Enter The Amount You Want to Deposit: "))
            customer.balance += amount
            print("-->Successfully Deposited", amount, "Your Current Balance is:", customer.balance)
            customer.transaction_history.append(f"Successfully Deposited {amount}")
            bank_balance(customer_balance=amount, number=1)
        elif num == 2:
            print("\n-->Your Current Balance is", customer.balance)
            amount = int(input("Enter The Amount You Want to Withdraw: "))
            if amount <= customer.balance:
                customer.balance -= amount
                
                balancee = bank_balance(customer_balance=amount, number=2)
                if balancee < 0:
                    print("Bankrupt.")
                else:
                    print("-->Successfully Withdraw", amount, "Your Current Balance is:", customer.balance)
                    customer.transaction_history.append(f"Successfully Withdraw {amount}")
            else:
                print("Withdrawal amount exceeded")
        elif num == 3:
            print("\n-->Your Available Balance is",customer.balance)
        elif num == 4:
            print(customer.transaction_history)
        elif num == 5:
            if options == 0:
                print("\nYou Can Take Loan 2 Times & You Took Loan For",customer.loan,"Times.")
                balance = bank_balance(0, 0)
                if customer.loan < 2:
                    how_much = int(input("How Much Loan Do You Want to Take?: "))
                    if balance < how_much:
                        print("You Can't Take That Much Loan. You Can Take Highest,",balance)
                    else:
                        bank_balance(how_much, 2)
                        customer.balance += how_much
                        print("-->Successfully You Have Taken Loan.",how_much, "Your Current Balance is:", customer.balance)
                        loans.append(how_much)
                        customer.transaction_history.append(f"Loan Tooked: {how_much}")
                        customer.loan = customer.loan + 1
                else:
                    print("You Have Already Took Loan For 2 times!") 
            else :
                print("Sorry, Currently The Loan Option is Off.")
        elif num == 6:
            search_email = input("\nEnter The Email Id to Search: ")
            found = False
            for person in people_list:
                if person.email == search_email:
                    found = True
                    money = int(input("How Much Money Do You Want to Transfer?: "))
                    if customer.balance == 0:
                        print("Your Balance Is 0. You Have To Deposit First.")
                    elif money > customer.balance:
                        print("You Can Only Transfer",customer.balance)
                    else:
                        customer.balance = customer.balance - money
                        person.balance = person.balance - money
                        customer.transaction_history.append(f"Money Trasfared to {person.email}, Amount is {money}")
                        person.transaction_history.append(f"Money Recived from {customer.email}, Amount is {money}")
            if not found:
                print("\nAccount does not exist.")
        else:
            print("\nThere is 1, 2, 3, 4, 5, 6 Option Available. But You Pressed ",num)

customer_modification = Customer_modification()

class Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def __repr__(self) -> str:
        return f"Welcome Sir!!\nAdmin's Name: {self.name}\nAdmin's Email: {self.email}"
    
class Admin_Activities:
    def admin_activities(self):
        global options
        option = int(input("Press '1' to See All User Accounts List,\nPress '2' to See Current Account User Accounts List,\nPress '3' to See Saving Account User Accounts List,\nPress '4' to See Bank's Balance,\nPress '5' to See The Amount of Loan,\nPress '6' to On / Off The Loan Feature,\nPress '7' to Delete Any Account: "))
        if option == 1:
            if not people_list:
                print("\nNo data available yet.")
            else:
                for i, person in enumerate(people_list):
                    print(f"Person {i + 1}:\n{person}")
        elif option == 2:
            if not current_account_people_list:
                print("\nNo data available yet.")
            else:
                for i, person in enumerate(current_account_people_list):
                    print(f"Person {i + 1}:\n{person}")
        elif option == 3:
            if not saving_account_people_list:
                print("\nNo data available yet.")
            else:
                for i, person in enumerate(saving_account_people_list):
                    print(f"Person {i + 1}:\n{person}")
        elif option == 4:
            balance = bank_balance(0,0)
            print(balance)
        elif option == 5:
            i = 0
            for loan in loans:
                i+=loan
            print(i)
        elif option == 6:
            print("\nTo Off The Loan Option Press '1' & To On The Loan Option Press '0'")
            k = int(input("Press Here: "))
            if k == 0:
                options = 0
            if k==1:
                options = 1
        elif option == 7:
            search_email = input("\nEnter The Email Id to Search: ")
            found = False
            for person in people_list:
                if person.email == search_email:
                    person.name = ""
                    person.email = ""
                    person.address = ""
                    person.account_number = ""
                    person.balance = 0
                    person.transaction_history = ""
                    person.loan = ""
                    print("\nSuccessfully Delted Account!")
                    for person in current_account_people_list:
                        if person.email == search_email:
                            person.name = ""
                            person.email = ""
                            person.address = ""
                            person.account_number = ""
                            person.balance = 0
                            person.transaction_history = ""
                            person.loan = ""
                            print("\nSuccessfully Delted Account!")
                    for person in current_account_people_list:
                        if person.email == search_email:
                            person.name = ""
                            person.email = ""
                            person.address = ""
                            person.account_number = ""
                            person.balance = 0
                            person.transaction_history = ""
                            person.loan = ""
                            print("\nSuccessfully Delted Account!")
                    found = True
                    break
            if not found:
                print("\nNo Person With That Name Found.")
        else:
            print("\nThere is 1, 2, 3, 4, 5, 6, 7 Option Available. But You Pressed ",option)        

admin_Activities=Admin_Activities()

class Log_In_Admin:
    
    def log_in_admin(slef):
        search_email = input("\nEnter The Email Id to Search: ")
        found = False
        for admin in admin_list:
            if admin.email == search_email:
                print("\nYou Are an Admin.")
                admin_Activities.admin_activities()
                found = True
                break
        if not found:
            print("No Person With That Name Found.\nYou Have To Sign up First!")
            name=input("Enter Your Name: ")
            email=input("Enter Your Email: ")
            admin = Admin(name=name, email=email)
            print(repr(admin))
            admin_list.append(admin)
            admin_Activities.admin_activities()
            
log_In_Admin=Log_In_Admin()


cnt = 0
while True:
    if cnt == 0:
        print("\nFirst You Have To Sign-Up.Once Signed-Up You Have To Log-in Each Time To Go To That Signed-Up Account!")
        cnt+=1

    print("\nMenu:")
    print("0 - Want to Create an Account.")
    print("2 - Log In(as a customer).")
    print("3 - Create an Admin Account.")
    print("4 - Log In(as a admin).")
    print("1 - Quit")
    choice = input("Enter your choice: ")

    if choice == "0":
        sign_up_customer.sign_up()
        
    elif choice == "1":
        break
            
    elif choice == "2":
        log_in_Customer.log_in_customer()
    
    elif choice == "3":
        name=input("Enter Your Name: ")
        email=input("Enter Your Email: ")
        admin = Admin(name=name, email=email)
        print(repr(admin))
        admin_list.append(admin)
        admin_Activities.admin_activities()
        
    elif choice == "4":
        log_In_Admin.log_in_admin()
        
    else:
        print("Invalid choice. Please select a valid option (0, 1, 2, 3 or 4).")

print("                            -----------Thank You So Much!!!-----------")
