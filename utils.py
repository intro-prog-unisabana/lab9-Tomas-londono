from person import Person
from bank_account import BankAccount

def person_data():
    print("Enter the person's name:")
    name = input()
    person = Person(name)

    while True:
        print("Enter a 4-digit account number:")
        acc_number = input()
        print("Enter the initial balance:")
        balance = float(input())

        account = BankAccount(acc_number, balance)
        person.add_account(account)

        print("Are you done adding accounts? (yes/no):")
        done = input()
        if done.lower() == "yes":
            break

    return person


def balance_summary(person_list):
    for person in person_list:
        total_balance = 0
        for account in person.accounts:
            total_balance += account.balance

        print(f"{person.name} : {total_balance:.2f}")# utils.py
