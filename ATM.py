class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
            self.check_balance()
        else:
            print("Deposit amount should be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.check_balance()
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount should be greater than zero.")

def main():
    atm = ATM(1000)  # Starting balance
    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
