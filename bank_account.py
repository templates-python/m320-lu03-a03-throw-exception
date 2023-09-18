class MoneyDrawError(Exception):

    def __init__(self, amount, available):
        super().__init__(f'Der Betrag {amount} kann nicht bezogen werden.\nAktuell verfügbar: {available}')

class BankAccount:
    '''
    fügen Sie hier als Erstes den Konstruktor ein.
    '''
    def __init__(self, max_overdraft, customer):
        self._balance   = 0.0
        self._overdraft = max_overdraft
        self._customer  = customer

    '''
    Hier erstellen Sie der Reihe nach die drei getter-Methoden.
    Verwenden Sie dazu den Decorator @property.
    '''

    @property
    def balance(self):
        return self._balance

    @property
    def overdraft(self):
        return self._overdraft

    @property
    def customer(self):
        return self._customer

    '''
    Erstellen Sie der Reihe nach die restlichen zwei Methoden.
    '''

    def booking(self, amount):
        self._balance += amount

    def get_money(self, amount):
        if (self._balance + self._overdraft) >= amount:
            self._balance -= amount
            return amount
        else:
            raise MoneyDrawError(amount, self._balance + self._overdraft)
