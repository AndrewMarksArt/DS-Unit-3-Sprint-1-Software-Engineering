import random
from src.acme import Product


adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30):
    """
    generate n number of products, default = 30 by randomly picking
    an adjective followed by a space then a randomly chosen noun,
    random prices and weights between 5 and 100, random flammability
    between 0.0 and 2.5, appends all products into a list which is returned.

    :param n: int, number of products to generate
    :return: list, list of generated products
    """
    lst = []
    for _ in range(n):
        prod_name = random.choice(adjectives) + ' ' + random.choice(nouns)
        prod_price = random.randint(5, 100)
        prod_weight = random.randint(5, 100)
        prod_flammability = random.uniform(0.0, 2.5)
        prod = Product(name=prod_name,
                       price=prod_price,
                       weight=prod_weight,
                       flammability=prod_flammability)
        lst.append(prod)
    return lst


def inventory_report(products):
    """
    takes a list of products and prints a nice summary
    unique product names, average price, weight, and flammability
    :param products: list of Product Objects
    :return: prints out report
    """
    # get count of unique products from products and print that out
    unique = set([products[i].name for i in range(len(products))])
    print('/////////'*5)
    print(f'\nUnique product names: {len(unique)}\n')

    # get average price, weight and flammability from products
    n = len(products)

    avg_price = sum([products[i].price for i in range(n)]) / n
    money = '${:,.2f}'.format(avg_price)  # format avg price

    avg_weight = sum([products[i].weight for i in range(n)]) / n

    avg_flame = sum([products[i].flammability for i in range(n)]) / n

    # print out averages for report
    print(f'Average price: {money}')
    print(f'Average weight: {avg_weight}')
    print(f'Average flammability: {avg_flame}\n')

    print('/////////' * 5)


if __name__ == '__main__':
    inventory_report(generate_products())
