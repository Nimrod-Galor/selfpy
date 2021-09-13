def sort_prices(list_of_tuples):
    """
    sort tuple list by price high to low
    :list_of_tuples list of tuples
    :type list
    :return sorted list of tuples
    :rtype list
    """
    return sorted(list_of_tuples, key=get_price, reverse=True)

def get_price(t):
    """
    extract price from tuple
    :t tuple
    :type tuple
    :return second item of tuple
    :rtype int
    """
    return t[1]

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))