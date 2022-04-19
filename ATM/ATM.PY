def atm_my():
    print("...........WELCOME!!!!!.........")
    print ("Punjab National Bank welcome you")
    print("Insert your ATM")
    balance=50000
    pin=1111
    language=input("select language:English or Hindi:-")
    if language=="English" or language=="english":
        user_pin=int(input("Please Enter Pin:-"))
        if user_pin==pin:
                print("Type of Transaction available:- \n a.balance enquiry \n b.cash_withdrawal \n c.deposit money \n d.Transfer Money")
                user_option=input("Enter  your type of transactions:-")
                if user_option=="a" or user_option=="A":
                    pin=int(input("enter your pin= "))
                    if user_pin==pin:
                        print("Your Total  Balance=",balance)
                    else:
                        print("Invalid Pin!!")
                if user_option=="b" or user_option=="B":
                    user_withdraw=int(input("Enter the amount to be withdraw:-"))
                    if user_withdraw<=balance:
                        pin=int(input("Enter your pin= "))
                        if user_pin==pin:
                            print("Your transaction is successful")
                            print("Remaining Balance is Rs=",balance-user_withdraw)
                        else:
                            print("Invalid Pin!!")
                    else:
                            print("Insufficient Balance")
                if user_option=="c" or user_option=="C" :
                    pin=int(input("enter your pin= "))
                    if user_pin==pin:
                        user_deposit=int(input("Enter the amount to be deposited:-"))
                        print ("your total balance is Rs=",balance+user_deposit)
                    else:
                        print("Invalid Pin!!")
                elif user_option=="d" or user_option=="D":
                    transfer_money=int(input("Enter the amount to be transfered ="))
                    if transfer_money>0:
                        balance=balance-transfer_money
                        pin=int(input("enter your pin= "))
                        if user_pin==pin:
                            print("Successful Transfer")
                            print("Remanining Balance=",balance)
                        else:
                            print("Invalid Pin!!")
                    else:
                        print("please enter a valid amount to proceed")    
    if language=="Hindi" or language=="hindi":
        print("Unavailable")
    user_exit=input("Do you want to exit:-yes or no ")
    if user_exit=="yes" or user_exit=="y" or user_exit=="Y":
        print("Thank you for banking with us.")
        print("You Can Take Your ATM")
    else:
        atm_my()
atm_my()