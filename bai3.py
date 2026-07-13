# gia = [100, 50, 80, 20]

# gio_hang = ["thit", "rau", "traicay", "xaphong"]

gia = {"thit": 100, "rau": 50, "trai cay": 80, "xa phong": 20}

# def tong_tien(gia):
#     total = 0
#     for item in gia:
#         total += gia[item]
#     return total
# print("Tong tien:", tong_tien(gia))

# gia.update({"thit": 50, "trai cay": 60})
# print("Gia moi:", gia)
# print("Tong tien moi:", tong_tien(gia))

# s = {1, 2, 3}
# s.add(4)
# print(s)

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