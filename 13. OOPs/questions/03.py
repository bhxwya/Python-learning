class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Rs.{amount} deposited successfully.")

    def withdraw_money(self, money):
        if self.__balance>=money:
            self.__balance-=money
            print(f"Rs.{money} withdrawn successfully")
        else:
            print("Insufficient Balance")
        
    def get_balance(self):
        print(f"Current Balance : {self.__balance}") 
    
customer = BankAccount("Ansh", 1000)
customer.deposit(500)
customer.withdraw_money(200)

customer.get_balance()