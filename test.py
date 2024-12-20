import unittest
from bankautomaat import bankaccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = bankaccount("42069420", "2771", "Raul Mendez", 100)

    def test_constructor(self):
        """Test de constructor van de bankrekening."""
        self.assertEqual(self.account.account_id, "42069420")
        self.assertEqual(self.account.pin_code, "2771")
        self.assertEqual(self.account.holder_name, "Raul Mendez")
        self.assertEqual(self.account.balance, 100)

    def test_deposit(self):
        """Test de stortfunctie."""
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 200)

        self.account.deposit(-50)
        self.assertEqual(self.account.balance, 200)

    def test_withdraw(self):
        """Test de afhaalfunctie."""
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 50)

        self.account.withdraw(-50)
        self.assertEqual(self.account.balance, 50)

    def test_invalid_input(self):
        """Test ongeldige invoer voor stortingen en opnames."""
        with self.assertRaises(TypeError):
            self.account.deposit('Vijfenvijftig')

        with self.assertRaises(TypeError):
            self.account.withdraw("Twintig")

if __name__ == '__main__':
    unittest.main()
