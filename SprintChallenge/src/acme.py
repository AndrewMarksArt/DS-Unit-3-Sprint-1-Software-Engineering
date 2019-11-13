import random


class Product:
    def __init__(self, name, price=10, flammability=0.5, weight=20):
        """
        an acme product class, takes a product name, price, weight and flammability
        and an id is randomly generated between 1,000,000 and 999,999,999
        :param name: string, no default
        :param price: int, default = 10
        :param weight: int, default = 20
        :param flammability: float, default = 0.5
        """
        if type(name) is not str:
            raise TypeError('name value must be a string')
        if price < 0:
            raise ValueError('price value must be greater than 0')
        if weight < 0:
            raise ValueError('weight value must be greater than 0')
        if flammability < 0:
            raise ValueError('price value must be greater than 0')

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """
        determines the steal ability of the product based on the price / weight
        if ratio is less than 0.5 = 'Not so stealable...'
        if ratio is between 0.5 and 1.0 = 'Kinda stealable.'
        otherwise = 'Very stealable'
        :return: message, str, 'Not so stealable' or 'Kinda stealable' or 'Very tealable'
        """
        ratio = self.price / self.weight
        if ratio < 0.5:
            message = 'Not so stealable...'
        elif 0.5 <= ratio < 1.0:
            message = 'Kinda stealable.'
        else:
            message = 'Very tealable'
        return message

    def explode(self):
        """
        calculates the flammability times the weight and returns a message
        if less than 10 = '...fizzle'
        if >= 10 and < 50 = '...boom!'
        if greater than or equal to 50 = '...BABOOM!!'
        :return: message, str, '...fizzle' or '...boom!' or '...BABOOM!!'
        """
        product = self.flammability * self.weight
        if product < 10:
            message = '...fizzle'
        elif 10 <= product < 50:
            message = '...boom!'
        else:
            message = '...BABOOM!!'
        return message


class BoxingGlove(Product):
    def __init__(self, name, price=10, flammability=0.5, weight=10):
        """
        an acme boxing glove class, takes a product name, price, weight and flammability
        and an id is randomly generated between 1,000,000 and 999,999,999
        :param name: str, boxing glove name
        :param price: int, default = 10
        :param flammability: float, default = 0.5
        :param weight: int, default = 10
        """
        super().__init__(name, price, flammability)
        self.weight = weight
        self.identifier = random.randint(1000000, 9999999)

    @staticmethod
    def explode():
        """
        overrides Product class explode method since boxing gloves don't explode
        :return: str, message saying '...its a glove'
        """
        return '...its a glove'

    def punch(self):
        """
        returns a message base on the boxing gloves weight
        if < 5 = 'That tickles'
        if 5 <= and < 15 = 'Hey that hurts!'
        if > 15 = 'OUCH!'
        :return: message, str, 'That tickles' or 'Hey that hurts!' or 'OUCH!'
        """
        if self.weight < 5:
            message = 'That tickles'
        elif 5 <= self.weight < 15:
            message = 'Hey that hurt!'
        else:
            message = 'OUCH!'
        return message
