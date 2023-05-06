def calculate_total_with_tax(state, cart):
    """ This function takes the two letter state abbreviation and cart which is a dictionary where each item has
    a type name and price. It checks the items in the cart with a list of tax-exempt items types as well as for the
    word fur in clothing type items. The function then calculates the tax for each item in the cart and adds together
    the final price totals for all items in the cart, and returns that value. """

    tax_rates = {'DE': 0.0, 'NJ': 0.066, 'PA': 0.06}

    exempt_item_types = {'Wic', 'Clothing'}

    total = 0.0

    for item in cart:
        item_type = item['type']
        item_name = item['name']
        item_price = item['price']

        if item_type in exempt_item_types:
            if item_type == 'Clothing':
                if 'fur' in item_name.lower() and state == 'NJ':
                    tax_rate = tax_rates[state]
                else:
                    tax_rate = 0.0
            else:
                tax_rate = 0.0
        else:
            tax_rate = tax_rates[state]

        tax_amount = item_price * tax_rate

        total += item_price + tax_amount

        print(total)

    return total
