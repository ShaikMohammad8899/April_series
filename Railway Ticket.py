#Railway Ticket
while True:
    def ticket():
        tk=1000
        age=int(input("Enter your age:"))
        gender=input("Gender(M/F):").upper()
        if gender=="M":
            if age<60:
                print("Your ticket prize is :",tk)
            else:
                discount=tk*(30/100)
                print("Your ticket prize is:",tk-discount)
        elif gender=="F":
            if age<60:
                discount=tk*(30/100)
                print("Your ticket prize is:",tk-discount)
            else:
                discount=tk*(50/100)
                print("Your ticket prize is:",tk-discount)
        else:
            print("Please a valid Gender")
    print("---------------------------------------------------------")                    
    ticket()
