
product = [
    {"id": 1, "name": "Áo thun", "stock": 10, "is_active": True},
    {"id": 2, "name": "Quần jean", "stock":0, "is_active": True},
    {"id": 3, "name": "Giày", "stock": 5, "is_active": False},
    {"id": 4, "name": "Nón", "stock": 3, "is_active": True}
]
def filter_available(products):
    available_product = []
    for product in products:
        if product["stock"] > 0 and product["is_active"] == True:
            available_product.append(product)
    return available_product
print("Danh sách còn sản phẩm:", filter_available(product))
