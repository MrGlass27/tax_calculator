import pytest
from taxation import calculate_total_with_tax


def test_nj_tax_one_item():
    state = 'NJ'
    cart = [
        {'type': 'everything else', 'name': 'Computer', 'price': 299.98}
    ]
    expected_charge = 319.78

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_nj_tax_multiple_items():
    state = 'NJ'
    cart = [
        {'type': 'everything else', 'name': 'Computer', 'price': 299.98},
        {'type': 'everything else', 'name': 'Plates', 'price': 21.99},
        {'type': 'everything else', 'name': 'Toaster', 'price': 29.99}
    ]
    expected_charge = 375.19

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_nj_tax_wic():
    state = 'NJ'
    cart = [
        {'type': 'Wic', 'name': 'Bread', 'price': 7.20}
    ]
    expected_charge = 7.20

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_nj_tax_clothing_not_fur():
    state = 'NJ'
    cart = [
        {'type': 'Clothing', 'name': 'Tshirt', 'price': 17.99}
    ]
    expected_charge = 17.99

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_nj_tax_clothing_fur():
    state = 'NJ'
    cart = [
        {'type': 'Clothing', 'name': 'Fur Coat', 'price': 120.52}
    ]
    expected_charge = 128.47

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_nj_tax_all_types():
    state = 'NJ'
    cart = [
        {'type': 'Clothing', 'name': 'Fur Coat', 'price': 120.52},
        {'type': 'Clothing', 'name': 'Tshirt', 'price': 17.99},
        {'type': 'Wic', 'name': 'Bread', 'price': 7.20},
        {'type': 'everything else', 'name': 'Computer', 'price': 299.98}
    ]
    expected_charge = 473.44

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_nj_tax_free_item():
    state = 'NJ'
    cart = [
        {'type': 'everything else', 'name': 'free stuff', 'price': 0},
    ]
    expected_charge = 0

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_de_tax_one_item():
    state = 'DE'
    cart = [
        {'type': 'everything else', 'name': 'Computer', 'price': 299.98}
    ]
    expected_charge = 299.98

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_de_tax_multiple_items():
    state = 'DE'
    cart = [
        {'type': 'everything else', 'name': 'Computer', 'price': 299.98},
        {'type': 'everything else', 'name': 'Plates', 'price': 21.99},
        {'type': 'everything else', 'name': 'Toaster', 'price': 29.99}
    ]
    expected_charge = 351.96

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_de_tax_all_types():
    state = 'DE'
    cart = [
        {'type': 'Clothing', 'name': 'Fur Coat', 'price': 120.52},
        {'type': 'Clothing', 'name': 'Tshirt', 'price': 17.99},
        {'type': 'Wic', 'name': 'Bread', 'price': 7.20},
        {'type': 'everything else', 'name': 'Computer', 'price': 299.98}
    ]
    expected_charge = 445.69

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_de_tax_free_item():
    state = 'DE'
    cart = [
        {'type': 'everything else', 'name': 'free stuff', 'price': 0},
    ]
    expected_charge = 0

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_de_tax_clothing_fur():
    state = 'DE'
    cart = [
        {'type': 'Clothing', 'name': 'Fur Coat', 'price': 120.52}
    ]
    expected_charge = 120.52

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_pa_tax_one_item():
    state = 'PA'
    cart = [
        {'type': 'everything else', 'name': 'Computer', 'price': 299.98}
    ]
    expected_charge = 317.98

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_pa_tax_multiple_items():
    state = 'PA'
    cart = [
        {'type': 'everything else', 'name': 'Computer', 'price': 299.98},
        {'type': 'everything else', 'name': 'Plates', 'price': 21.99},
        {'type': 'everything else', 'name': 'Toaster', 'price': 29.99}
    ]
    expected_charge = 373.08

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_pa_tax_wic():
    state = 'PA'
    cart = [
        {'type': 'Wic', 'name': 'Bread', 'price': 7.20}
    ]
    expected_charge = 7.20

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_pa_tax_clothing_fur():
    state = 'PA'
    cart = [
        {'type': 'Clothing', 'name': 'Fur Coat', 'price': 120.52}
    ]
    expected_charge = 120.52

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_pa_tax_all_types():
    state = 'PA'
    cart = [
        {'type': 'Clothing', 'name': 'Fur Coat', 'price': 120.52},
        {'type': 'Clothing', 'name': 'Tshirt', 'price': 17.99},
        {'type': 'Wic', 'name': 'Bread', 'price': 7.20},
        {'type': 'everything else', 'name': 'Computer', 'price': 299.98}
    ]
    expected_charge = 463.69

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge


def test_pa_tax_free_item():
    state = 'PA'
    cart = [
        {'type': 'everything else', 'name': 'free stuff', 'price': 0},
    ]
    expected_charge = 0

    total_charge = calculate_total_with_tax(state, cart)

    assert total_charge == expected_charge
