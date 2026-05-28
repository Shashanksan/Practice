# from abc import ABC, abstractmethod 

# class abstratc(ABC):
#     @abstractmethod
#     def show(self):
#         pass
# class shashank(abstratc):
#     def main(self):
#         print(self)

#     def show(self):
#         print("abstract method printed")
      
# s1=shashank()

# s1.show()
class parent:
  
  def show(self):
      print(self)
      print("I am 1st shoe method")
      
class child(parent):
    
    def show(self):
        print(self)
        super().show()
        print("I am 2st shoe method")
        
        
ob1=child()
print(ob1)
ob1.show()
