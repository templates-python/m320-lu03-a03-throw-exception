from customer import Customer
from bank_account import BankAccount


def draw_money(bank_account, amount):
    if amount <= 0:
        return -1
    # OK, Geld abheben
    else:
        bank_account.get_money(amount)
        print(f'Kontostand = {bank_account.balance}')


def main():
     banc_account = BankAccount(2500, Customer())
     banc_account.booking(5000)
     print('Brechen Sie die Programmausführung mit der Eingabe -1.\n---')
     print(f'Kontostand = {banc_account.balance}')
     print(f'erlaubter Überzug = {banc_account.overdraft}')
     while True:
         value = float(input('Bezug : '))
         if draw_money(banc_account, value) == -1:
             break


if __name__ == '__main__':
    main()