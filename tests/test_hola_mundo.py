import unittest
from hola_mundo import greeting


class TestGreeting(unittest.TestCase):
    def test_greeting_returns_expected_message(self):
        self.assertEqual(greeting(), "Hola, mundo")


if __name__ == "__main__":
    unittest.main()
