while True:
    account=100000
    card="c"
    password=1234
    print("________ ATM APPLICATION ________")
    a=input("Insert the card : ")
    if a==card:
        print("Welcome Shaik")
        b=int(input("Enter the Password: "))    
        if b==password:
            option=int(input("\nEnter option: \n1.Balance enq  2.Withdrawal   "))
            if option==1:
                print("Your Balance is:",account)    
            elif option==2:
                withdraw=int(input("Enter the amount to withdraw: "))
                if account >= withdraw:
                    account=account-withdraw
                    print("Withdrawal Successful!")
                    print("Remaining Balance:",account)
                else:
                    print("Insufficient Balance!")
                    print("Available Balance: ",account)
            else:
                print("Invalid option selected.")
        else:
            print("Wrong Password! Access Denied.")
    else:
        print("Invalid Card! Please try again.")
