#here I am creating bank account and doing some operations deposit , withdraw and display balance and output printed.#here i am creating bank account and doing some operations deposit , withdraw and display balance and output printed.
class bankaccount:

  def __init__(self, account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  #defining deposit 
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("amount deposited ₹{}. new balance: ₹{}".format(amount,
                                                            self.__account_balance))
    else:
      print("invalid deposit ammount.")

  #defining withdraw 
  def withdraw(self,amount):
   if amount > 0 and amount <= self.__account_balance:
     self.__account_balance -= amount
     print("withdraw ₹{}. new balance: ₹{}".format(amount,self.__account_balance))
   else:
     print("invalid withdrawal amount or insufficient balance.")

  #defining to display balance
  def display_balance(self):
   print("account balance for {} (account #{}): ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))

#create an account
account = bankaccount(account_number="9488682602",
                     account_holder_name="Prasanth",
                     initial_balance=10000.0)

#lets do a deposit here to check wheather working or not 
account.display_balance()
account.deposit(1000.0)
account.withdraw(2000.0)
account.withdraw(20000.0)
account.display_balance()