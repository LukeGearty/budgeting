# A program that takes in a user's weekly pay check, and then divides it according to user input
## ask for user input
def savings_money(paycheck, savings):
    # convert savings to decimal
    decimal = savings / 100
    money_savings = paycheck * decimal
    return str(round(money_savings, 2))
def main():
    try:
        paycheck = float(input("Enter your paycheck, after taxes, for the week: "))
        savings = float(input("As a percentage, how much would you like to save?: "))
        amount = savings_money(paycheck, savings)
        print(f"You need to put ${amount} away to save {savings}% of ${paycheck}.")
    except:
        print("Invalid input")

if __name__=="__main__":
    main()
