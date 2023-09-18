import pytest
from bank_account import BankAccount
from customer import Customer
from main import draw_money


class TestMain:

    @pytest.fixture
    def a_bank_account(self):
        ba = BankAccount(1000, Customer())
        ba.booking(1000)
        return ba

    def test_draw_money_abort(self, a_bank_account):
        assert draw_money(a_bank_account, 0) == -1
    def test_draw_money_ready(self, a_bank_account, capsys):
        draw_money(a_bank_account, 1500)
        captured = capsys.readouterr()
        assert captured.out == 'Kontostand = -500.0\n'

    def test_draw_money_excpt(self, a_bank_account, capsys):
        draw_money(a_bank_account, 5000)
        captured = capsys.readouterr()
        assert captured.out == 'WARNING: Der Betrag 5000 kann nicht bezogen werden.\nAktuell verfügbar: 2000.0\n'
