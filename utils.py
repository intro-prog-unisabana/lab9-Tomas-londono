from person import Person
from bank_account import BankAccount

def person_data():
    name = input("Enter the person's name:\n")
    person = Person(name)

    while True:
        acc_number = input("Enter a 4-digit account number:\n")
        balance = float(input("Enter the initial balance:\n"))

        account = BankAccount(acc_number, balance)
        person.add_account(account)

        done = input("Are you done adding accounts? (yes/no):\n")
        if done.lower() == "yes":
            break

    return person


def balance_summary(person_list):
    for person in person_list:
        total_balance = 0
        for account in person.accounts:
            total_balance += account.balance

        print(f"{person.name} : {total_balance:.2f}")# utils.py
