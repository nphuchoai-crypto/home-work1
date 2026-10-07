
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class DiscountedProduct(Product):
#     def __init__(self, name, price, discount):
#         super().__init__(name, price)  # gọi constructor lớp cha
#         self.discount = discount

#     def final_price(self):
#         return self.price * (1 - self.discount)

# p = DiscountedProduct("Laptop", 1000, 0.1)
# print(p.final_price())

class User:
    def __init__(self, password):
        self.__password = password

    def change_password(self, old_password, new_password):
        if old_password != self.__password:
            raise ValueError ("Mật khẩu cũ không đúng.")
        if len(new_password) < 8:
            raise ValueError ("Mật khẩu mới phải có ít nhất 8 kí tự!")

        self.__password = new_password

user = User("12345678")
print("\n---Test mật khẩu cũ---")
try: 
    user.change_password("abc123","newpassword")
    print("Đổi mật khẩu thành công")
except ValueError as e:
        print("Lỗi:", e)
print("\n---TEST MẬT KHẨU MỚI QUÁ NGẮN---")
try:
     user.change_password("12345678","1234")
     print("Đổi mật khẩu thành công!")
except ValueError as e:
     print("Lỗi:", e)
        





    



    