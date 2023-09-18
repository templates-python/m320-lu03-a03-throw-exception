import pytest
from bank_account import BankAccount, MoneyDrawError
from customer import Customer
class TestBankAccount:
    @pytest.fixture
    def a_bank_account(self):
        banc_account =  BankAccount(1000, Customer())
        banc_account.booking(2500)
        return banc_account

    def test_bank_account_money_drawing_well(self, a_bank_account):
        amount = a_bank_account.get_money(2000)
        assert amount == 2000
        assert a_bank_account.balance == 500

    def test_bank_account_max_money_drawing(self, a_bank_account):
        a_bank_account.get_money(3500)
        assert a_bank_account.balance == -1000

    def test_bank_account_money_drawing_exception(self, a_bank_account):
        with pytest.raises(MoneyDrawError):
            amount = a_bank_account.get_money(5000)