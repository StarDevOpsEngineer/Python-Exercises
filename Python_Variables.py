balance = 50000
card_number = input("Please Enter your Card number:")
pin = input("Please Enter yur pin:")

if card_number=="1234567" and pin=="1234":
    print("Hi Pieere, Welcome!")
    action = input("Do you want to withraw, deposit or check balance? - Enter w or d or cb:")
if action=="d":
    amount = input("How much would you like to Deposit?")
    amount = float(amount)
    if amount < balance:
        print("The amount provided needs to be more that your current balance.")
    else:
        balance = balance + amount
        print(f"Your current balance is {balance}")
elif action=="w":
    amount = input("How much would you like to Withdraw?")
    amount = float(amount)
    if amount > balance:
        print("The amount provided is more than your current balance.")
    else:
        balance = balance - amount
        print(f"Your current balance is {balance}")
        print("Here is the total you want to withdre:", amount)
elif action=="cb":
    action = input("Would you like to see your Checking or Savings? - Enter C or S:")
    if action=="c":
        print(f"Your Checking Account balance is {balance}")
    if action=="s":
        print(f"Your Savings Account balance is {balance}")
    #else:
        #print("Please enter D for deposit or W for withdraw or CB for check balance")
else:
    print ("The pin or Card number is not Correct. Please Try again!")
    