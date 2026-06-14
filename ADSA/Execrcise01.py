from array import array
arr=list(map(int,input().split()))
def insert():
    pos=int(input())
    val=int(input())
    print(len(arr))
    if (pos>len(arr)) or (pos<0):
        print("Invalid position.")
    else :
        arr.insert(pos,val)
        print(f"Inserted {val} at position {pos}.")
def delete():
    pos=int(input())
    if(pos>=0)and(pos<len(arr)):
        print(f"Deleted element {arr[pos]} from position {pos}.")
        arr.pop(pos)
    else:
        print("Invalid position.")
      
        
    
def view():
    print(len(arr))
    if(len(arr)==0):
        print("Array is empty")
    else:
        print("Current array:",*arr)
while(True):
    choice=int(input())
    if choice==1:
     insert()
    elif choice==2:
     delete()
    elif choice==3:
     view()
    elif choice==4:   
     exit()