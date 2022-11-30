#### Return_Money
while(True):
    amount=int(input("Enter Remaining Money: "))
    twenty_five=amount//25
    ten=(amount % 25) // 10
    five=((amount % 25 ) % 10) // 5
    one = (((amount % 25) % 10) % 5) //1
    print("No of 25 Coins :",twenty_five)
    print("No of 10 Coins :",ten)
    print("No of  5 Coins :",five)
    print("No of  1 Coins :",one)
    print("Total No of coins :", twenty_five + ten + five + one , "\n")
    if amount == 0:
        print("You don't have to return money")