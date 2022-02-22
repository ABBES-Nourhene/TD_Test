import unittest
from mock import patch, PropertyMock
from carte_pizzeria import CartePizzeria

class TestCartePizzeria(unittest.TestCase):

    def test_init_cp():
        cp=CP()
        assert cp.__pizzas ==[]:

    @patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
    def test_carte_pizza_is_not_empty(mock_pizzas):
        c = CartePizzeria()
        mock_pizzas.return_value = []
        assert c.is_empty()

    def test_is_empty_success():
        cp=CP()
        #cp.pizzas=[] "si on fait en public"
       assert cp.is_empty()

if __name__ == "__main__":
    unittest.main()