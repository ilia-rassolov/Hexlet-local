catalog_ = {
  1: { 'id': 1, 'name': 'молоко', 'price': 100 },
  2: { 'id': 2, 'name': 'сыр', 'price': 200}
}
product3 = { 'id': 3, 'name': 'чипсы', 'price': 100 }
product4 = { 'id': 4, 'name': 'чипсы', 'price': 100 }


def add_product(catalog, product):
    keys = sorted(catalog.keys())
    key = keys[-1] + 1
    if product not in catalog.values():
        catalog[key] = product
    return catalog


updated_catalog = add_product(catalog_, product3)
updated_catalog = add_product(updated_catalog, product4)
print(updated_catalog)

def get_product_by_id(catalog, id):
    for product in catalog.values():
        if product['id'] == id:
            return product


print(get_product_by_id(catalog_, 3))

def remove_product(catalog, num_product):
    for num_catalog, product in catalog.items():
        if product['id'] == num_product:
            catalog.pop(num_catalog)
            break
    catalog_new = dict()
    for num_catalog_new, product in enumerate(catalog.values(), 1):
        catalog_new[num_catalog_new] = product
    return catalog_new


# updated_catalog = remove_product(updated_catalog, 2)
print(updated_catalog)

def add_to_cart(catalog, cart, product_id, quantity):
    for product in cart:
        if product['id'] == product_id:
            product['quantity'] += quantity
            return cart
    for product in catalog.values():
        if product['id'] == product_id:
            product_cart = dict(product)
            product_cart['quantity'] = quantity
            cart.append(product_cart)
            break
    return cart

cart_ = []
cart_ = add_to_cart(updated_catalog, cart_, 2, 2)
cart_ = add_to_cart(updated_catalog, cart_, 1, 1)
print(f"{cart_=}")

from uuid import uuid4

def place_order(cart, order):
    total_amount = 0
    for product in cart:
        total_amount += product['price'] * product['quantity']
    id_order = str(uuid4())
    new_order = {id_order: {'id': id_order, 'items': cart, 'total_amount': total_amount}}
    return [], new_order


order_ = {}
new_cart, new_order = place_order(cart_, order_)
print(new_cart) # []
print(new_order) # =>


[ {
                "id": 2,
                "name": "Product 2",
                "price": 200,
                "quantity": 3,
            },
            {
                "id": 1,
                "name": "Product 1",
                "price": 100,
                "quantity": 1,
            },
        ]