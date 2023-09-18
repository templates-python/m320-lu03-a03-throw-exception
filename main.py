from customer import Customer
from bank_account import BankAccount
def main():
     banc_account = BankAccount(2500, Customer())
     banc_account.booking(5000)
     print('Brechen Sie die Programmausführung mit der Eingabe -1.\n---')
     print(f'Kontostand = {banc_account.balance}')
     print(f'erlaubter Überzug = {banc_account.overdraft}')
     while True:
         value = float(input('Bezug : '))
         if value < 0:
             break
         # OK, Geld abheben
         banc_account.get_money(value)
         print(f'Kontostand = {banc_account.balance}')



if __name__ == '__main__':
    main()


