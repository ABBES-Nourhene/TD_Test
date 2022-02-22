class CartePizzeria:
    def __init__(self,pizzas=[]):
        self.__pizzas = pizzas
    def is_empty(self):
        #retourne un booléen indiquant si la carte est vide ou non
        liste = [] 
        # len() renvoie le nombre d'éléments
        return len(self.__pizzas) == 0:
    def nb_pizzas(self):
        # retourne le nombre de pizzas de la carte
        return len(self,.__pizzas)
    def add_pizza(self,pizza):
        #ajoute une pizza à la carte
        self.__pizzas.append(pizza)
    def remove_pizza(self,pizza):
        #retire la pizza nommée name de la carte, si celle-ci n'existe pas, 
        #lève une exception CartePizzeriaException
        try
        self.__pizzas.remove(pizza)
        accept ValueError:
        raise CPE("pizza non existante")

    @property 
    def pizzas(self):
        return self.__pizzas  
    #@pizzas.setter
    #def pizzas(self,value):
        #self.__pizzas=value

class CartePizzeriaException(Exception):
    pass




