from abc import ABC, abstractmethod
import random

class Bank(ABC):
    def __init__(self) -> None:
        self.transaction=[]
        self.accounts={}
        self.employees={}


    def create_account(self, email, password):
        for account in self.accounts.values():
            if email == account[1]:
                print("Account Already Exists!")
                return
            
        account_number=random.randint(0, 1)
        initial_balance=0

        while account_number in self.accounts:
            account_number=random.randint(0, 1)

        self.accounts[account_number]=(initial_balance, email, password)
        print("Account Created Successfully!")


    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            balance, email, password=self.accounts[account_number]
            balance+=amount
            self.accounts[account_number]=(balance, email, password)
            self.transaction.append(f"Deposited {amount} to account {account_number}.")
            print("Deposit Successfuly!")
        else:
            print("Account Doesn't Exist!")


    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            balance, email, password=self.accounts[account_number]
            if balance>=amount:
                balance-=amount
                self.accounts[account_number]=(balance, email, password)
                self.transaction.append(f"Withdraw {amount} from account {account_number}.")
                print("Withdraw Successfully!")
            else:
                print("Not Enough Balance!")
        else: 
            print("Account Doesn't Exist!") 


    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance, email, password=self.accounts[account_number]
            print(f"Account {account_number}, Balance: {balance}.")
        else:
            print("Account Doesn't Exist!")


    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            balance_f, email_f, password_f=self.accounts[from_account]
            balance_t, email_t, password_t=self.accounts[to_account]
            if balance_f>=amount:
                balance_f-=amount
                balance_t+=amount
                self.accounts[from_account]=(balance_f, email_f, password_f)
                self.accounts[to_account]=(balance_t, email_t, password_t)
                self.transaction.append(f"Transferred {amount} from account {from_account} to account {to_account}.")
                print("Transfer Successfully!")
            else:
                print("Not Enough Balance!")
        else:
            print("One or Both Accounts Don't Exists!")


    def check_transaction_history(self):
        for transaction in self.transaction:
            print(transaction, end="\n")


    def take_loan(self, account_number):
        if account_number in self.accounts:
            balance, email, password=self.accounts[account_number]
            loan_amount=balance*2
            self.accounts[account_number]=(loan_amount, email, password)
            self.transaction.append(f"Took a Loan of {loan_amount} from account {account_number}.")
            print("Loan Taken Successfully!")
        else:
            print("Account Doesn't Exist!")

    
    def total_available_balance(self):
        total=0
        for account in self.accounts.values():
            balance, email, password=self.accounts[account]
            total+=balance
        print(total)


class User(Bank):
    def __init__(self, email, password) -> None:
        self.email=email
        self.password=password
        super().__init__()
    
    def create_account(self):
        return super().create_account(self.email, self.password)
    
    def deposit(self, account_number, amount):
        return super().deposit(account_number, amount)
    
    def withdraw(self, account_number, amount):
        return super().withdraw(account_number, amount)
    
    def check_balance(self, account_number):
        return super().check_balance(account_number)

    def transfer(self, from_account, to_account, amount):
        return super().transfer(from_account, to_account, amount)
    
    def check_transaction_history(self):
        return super().check_transaction_history()


class Admin(Bank):
    def __init__(self, email, password) -> None:
        self.email=email
        self.password=password
        super().__init__()

    def create_empolyee_account(self, email, password):
        for employee in self.employees.values():
            if email == employee[1]:
                print("Admin Account Already Exists!")
                return
            
        employee_id=random.randint(0, 4)
        while employee_id in self.employees:
            employee_id=random.randint(0, 4)

        self.employees[employee_id]=(employee_id ,email, password)
        print("Admin Account Created Successfully!")

    def get_total_available_balance(self):
        return super().total_available_balance()





user1=User("iraj@gmail.com", "12345678")
user1.create_account()
user1.deposit(0, 500)
user1.deposit(0, 700)
user1.check_balance(0)
user1.take_loan(0)
user1.check_transaction_history()

user2=User("masum@gmail.com", "24681357")
user2.create_account()
user2.deposit(1, 500)
user2.deposit(1, 300)
user2.check_balance(1)
user2.take_loan(1)
user2.check_transaction_history()


admin1=Admin("billa@gmail.com", "1234")
admin1.create_empolyee_account("employee1@gmail.com", "password1")
admin1.get_total_available_balance()















# bank=Bank()
# bank.create_account("iraj@gmail.com", "12345678")
# bank.create_account("iraj@gmail.com", "12345678")
# bank.create_account("iraj23@gmail.com", "12345678")
# bank.create_account("iraj12@gmail.com", "12345678")
# bank.create_account("iraj23@gmail.com", "12345678")
# bank.deposit(3, 500)
# bank.deposit(3, 700)
# bank.deposit(2, 700)
# bank.check_balance(3)
# bank.deposit(2, 700)
# bank.transfer(3, 2, 200)
# bank.check_balance(2)
# bank.check_transaction_history()
# bank.take_loan(2)