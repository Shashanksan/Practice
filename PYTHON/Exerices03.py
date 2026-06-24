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
class ValueError(Exception):
    pass
class atm:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,withdrawAmount):
        return self.balance-withdrawAmount
try:
    balance=int(input())
    amount=atm(balance)
    withdrawn=int(input())
    result =amount.withdraw(withdrawn)
    if withdrawn<0:
        raise ValueError
    elif withdrawn>balance:
        raise InsufficientBalance
    else:
        print(f"Withdrawl successful. Remaining balance: Rs.{result}")
except InsufficientBalance as e:
    print("Transaction Failed: Not enough balance")
except ValueError as e:
    print("Invalid Amount: Amount must be greater than 0")