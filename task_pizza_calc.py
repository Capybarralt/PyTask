class Ingredient(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_cost(self):
        return self.cost



class Pizza(object):

    def __init__(self, name):
        self.name = name
        self.composition = []

    def get_name(self):
        return self.name

    def add_ingredient(self, ingredient):
        self.composition.append(ingredient)

    def get_cost(self):
        cost = 0
        for i in self.composition:
            cost += i.get_cost()
        return cost

    def get_weight(self):
        weight = 0
        for i in self.composition:
            weight += i.get_weight()
        return weight / 1000


class Order(object):
    def __init__(self):
        self.composition = []

    def add_pizza(self, pizza):
        self.composition.append(pizza)

    def get_cost(self):
        cost = 0
        for i in self.composition:
            cost += i.get_cost()
        return cost

    def print_receipt(self):
        for i in self.composition:
            weight = '%.3f' %i.get_weight()
            cost = '%.2f' %i.get_cost()
            print(f'{i.get_name()} ({weight}г) - {cost}руб')
