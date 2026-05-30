from array import array

arr=list(map(int,input().split()))

    

def insert():
      pos=int(input())
      val=int(input())
      print("lenght",len(arr))
      if pos>len(arr):
          print("Invalid position")
      else:
        arr.insert(pos,val)
        print("Inserted",val,"at position", pos)
     
def delete():
  pos=int(input())
  if (pos>=0) and (pos<len(arr)):
  
      arr.pop(pos)
      print("Deleted element","from position" ,pos)
  else:
      print("Invalid position.")

def view():
    if(arr.count==0):
        print("Array is empty.")
    else:
        
        print("Current array:",arr)
while(True):
      choice=int(input())
     
      match choice:
          case 1:
              insert()
          case 2:
               delete()
          case 3:
                view()
          case 4:
              exit() 
        
    