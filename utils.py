from person import Person
from bank_account import BankAccount

def person_data():
    name = input()
    person = Person(name)

    while True:
        acc_number = input()
        balance = float(input())

        person.add_account(BankAccount(acc_number, balance))

        done = input()
        if done == "yes":
            break

    return person


def balance_summary(person_list):
    for person in person_list:
        total_balance = 0
        for account in person.accounts:
            total_balance += account.balance

        print(f"{person.name} : {total_balance:.2f}")
