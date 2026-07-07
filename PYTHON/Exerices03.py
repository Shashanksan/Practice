# class InsufficientBalance(Exception):
#     pass
# class value(Exception):
#     pass
# class atm:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,withdrawAmount):
#         return self.balance-withdrawAmount
        
        
     
# try:
#     amount=atm(10000)
#     withdrawAmount=int(input("Enter the amount to withdraw"))
#     result = amount.withdraw(withdrawAmount)
#     if withdrawAmount<0:
#         raise ValueError
#     elif withdrawAmount>amount.balance:
#         raise InsufficientBalance
#     else:
#         print(f"Withdrawal successful. Remaining balance: Rs.{result}")
        
    
    
    
# except InsufficientBalance as e:
#     print("Transaction Failed: Not enough balance")
    
# except ValueError as e:
#     print("Invalid Amount: Amount must be greater than 0")    
    
class InsufficientBalance(Exception):
    pass


class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, withdrawAmount):
        return self.__balance - withdrawAmount


try:
    balance = int(input())
    amount = int(input())

    if amount <= 0:
        raise ValueError

    if amount > balance:
        raise InsufficientBalance

    atm = ATM(balance)

    remaining = atm.withdraw(amount)

    print(f"Withdrawal successful. Remaining balance: Rs.{remaining}")

except InsufficientBalance:
    print("Transaction Failed: Not enough balance")

except ValueError:
    print("Invalid Amount: Amount must be greater than 0")
    
    
    
---------------------------------------------------------------------------
# Code OG
class InsufficientBalance(Exception):
    pass

class ATM:
    def __init__(self,balance):
        self.__balance=balance
    def withdraw(self,amount):
        return self.__balance-amount
try:
    balance=int(input())

        

    amount=int(input())
    
    
   
    if amount<=0:
        raise ValueError("Invalid Amount: Amount must be greater than 0")
    if amount>balance:
        raise InsufficientBalance
    atm=ATM(balance)
        
    result=atm.withdraw(amount)

    print(f"Withdrawl successful. Remaining balance: Rs.{result}")
        
except InsufficientBalance as e:
    print("Transaction Failed: Not enough balance")
except ValueError as e:
    print(e)