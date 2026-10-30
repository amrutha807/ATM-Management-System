print("ATM".center(70))
n=int(input("enter pin:"))
m=1432
k=10000
print(" 1.CHECK BALANCE\n","2.DEPOSITE\n","3.WITHDRAW\n","4.SHOW MENU\n","5.EXIT")
if n==m:
     while True :
         v=int(input("please enter a number 1 to 4:"))
         if v>5:
             print("invalied option")
         if v==5:
             print("Exit")
             break
         else:
            if v==1:
                def check_balance():
                  print("Available Balance:",k)
                check_balance()
            elif v==2:
                def deposit(l):
                    global k
                    k=k+l
                    print("successfulli deposited your ammount, if you want check your balance pleas enter option 1")
                l=int(input("enter deposite ammount:"))
                deposit(l)
            elif v==3:
                def withdraw(j):
                    global k
                    if k>=j and j>0:
                        k=k-j
                    else:
                        print("insufficent ammount:")
                    print("successfulli withdral your ammount, if you want check your balance pleas enter option 1")
                j=int(input("enter withdraw ammount:"))
                withdraw(j)
            elif v==4:
                print("1.CHECK BALANCE\n","2.DEPOSITE\n","3.WITHDRAW\n","SHOW MENU\n","exit") 
else:
    print("please enter valid pin:")


    
        
        
    
    



        
    

