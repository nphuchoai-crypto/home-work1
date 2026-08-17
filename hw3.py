# Viết hàm nhận product_id và danh sách tất cả sản phẩm. Trả về tối đa limit sản phẩm cùng rating cao nhất.

# products = [
#     {"id": 1, "name": "Áo polo", "category": "ao", "rating": 4.5},
#     {"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8},
#     {"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2},
#     {"id": 4, "name": "Quần jeans","category": "quan","rating": 4.7},
#     {"id": 5, "name": "Áo sơ mi", "category": "ao", "rating": 4.6},
# ]
# def related_products(product_id, products, limit):
#     category = ""
#     for product in products:
#         if product["id"] == product_id:
#             category = product["category"]
#         break
#     print(category)

#     rated_products = []
#     for product in products:
#         if product["category"] == category and product["id"] != product_id:
#             rated_products.append(product)
#     print(rated_products)
#     rated_products.sort(key = lambda x: x["rating"], reverse = True)
#     return rated_products[:limit]
  

# print(related_products(product_id=1, products=products, limit=3))

# Home work 1: Kho thương mại điện tử cần lọc sản phẩm ttonf kho trước khi hiển thị lên trang chủ
# Viết hàm filter_available nhận danh sách sản phẩm và trả về các sản phẩm có stock > 0 và is_active == True

# products = [
#     {"id": 1, "name": "Áo thun", "stock": 10, "is_active": True},
#     {"id": 2, "name": "Quần jean", "stock": 0, "is_active": True},
#     {"id": 3, "name": "Giày sneaker","stock": 5, "is_active": False},
#     {"id": 4, "name": "Nón baseball","stock": 3, "is_active": True},
# ]

# def filter_available(product_list):
#     danh_sach_san_pham = []
#     for product in product_list:
#         if product["stock"] > 0 and product["is_active"] == True:
#             danh_sach_san_pham.append(product)
#     return danh_sach_san_pham
# print(filter_available(products))

# Bài 20: Kiểm tra xung đột kho hàng trong flash sale
# Viêt hàm kiểm tra các sản phẩm trong flash_sale_items có trùng với chiến dịch đang hoạt động không, báo cáo chi tiết


# active_campaigns = {
#     "clearance": {"SP001","SP005","SP009"},
#     "bundle_deal": {"SP003","SP007","SP011"},
#     "new_arrival": {"SP013","SP015"},
# }

# flash_sale_items = {"SP001","SP003","SP007","SP020","SP025"}

# def check_conflicts(flash_sale_items, active_campaigns):
#     conflicts = []
#     safe_item = []
#     has_conflict = False

#     for item in flash_sale_items:
#         item_conflict = False
#         for key, value in active_campaigns.items():
#             if item in value:
#                 conflicts.append(item)
#                 has_conflict = True
#                 item_conflict = True
#                 break
#         if item_conflict == True:
#                 safe_item.append(item)
                
               
#     return {
#             "has_conflict": True,
#             "conflicts": {"SP001": ["clearance"],
#             "SP003": ["bundle_deal"],
#             "SP007": ["bundle_deal"]},
#             "safe_items": {"SP020", "SP025"}
#         } 

# print(check_conflicts(flash_sale_items, active_campaigns))

# Bài tập 1: Xây dựng class Product
# Xây dựng một class Product với các yêu cầu sau:
# • Thuộc tính: product_id, name, price, quantity (tồn kho), category
# • Hàm __init__() khởi tạo các thuộc tính trên
# • Phương thức apply_discount(discount_percent): giảm giá sản phẩm (trả về giá sau
# giảm)
# • Phương thức is_in_stock(): kiểm tra xem sản phẩm còn trong kho hay không
# Yêu cầu: Viết code và chạy với 2-3 sản phẩm khác nhau.

from decimal import Decimal

class Product:
        def __init__(self, product_id: int, name: str, price: float, quantity: int, category: str): 
        # Kiểm tra dữ liệu đầu vào có hợp lệ hay không
            if price < 0 or quantity < 0: # Giá và số lượng tồn kho phải là số dương
                raise ValueError(" Giá và số lượng tồn kho phâi là số dương")
            # Raise là câu lệnh để ném ra một ngoại lệ (exception) khi điều kiện không thoả mãn

            self.product_id = product_id
            self.name = name
            self.price = Decimal(price) # Sử dụng Decimal để tránh lỗi làm tròn số 
            self.quantity = quantity
            self. category = category

        def apply_discount(self, discount_percent: float) -> float:
            if discount_percent < 0 or discount_percent > 100:
                raise ValueError(" Phần trăm giảm giá phải nằm trong khoảng từ 0 đến 100")

        # Tính giá sau khi giảm giá
            discount_amount = self.price * Decimal(discount_percent / 100)
            final_price = self.price - discount_amount
            return float(final_price) # Trả về giá sau khi giảm giá dưới dạng float

        def is_in_stock(self) -> bool:
            """ 
            Kiểm tra xem sản phẩm còn trong kho hay không
            """
            return self.quantity > 0
            # """ """ Docstring giải thích cho phương thức, giúp người đọc dễ hiểu code hơn

        def __str__(self):
                """ Phiên dịch đối tượng thành chuỗi để hiển thị thông tin sản phẩm """
                stock_status = "Còn hàng" if self.is_in_stock() else "Hết hàng"
                return f"[{self.product_id}] {self.name} - Giá: {self.price:,.0f}đ -  Trạng thái: {stock_status}"
            # f"" là cú pháp f - string cho phép chèn biến vào chuỗi, {self.price:,.0f}đ ngăn cách hàng nghìn và hàng trăm, không có số thập phân

# Test case
if __name__ == "__main__":
        # 1. Tạo các sản phẩm khác nhau

        p1 = Product(product_id=101, name="Đồng hồ báo thức", price=399000, quantity=10, category=" Đồ gia dụng")
        p2 = Product(product_id=102, name="Bàn phím cơ Loree", price=1299000, quantity=0, category="Thiết bị điện tử")
        p3 = Product(product_id=103, name="Tai nghe Sony WH-1000XM4", price=4990000, quantity=5, category="Thiết bị điện tử")

        products = [p1, p2, p3]
        print("--- Danh sách sản phẩm ---")
        for p in products:
            print(p)

        print("\n--- Kiểm tra giảm giá ---")
        # Kiểm tra tồn kho và giảm giá
        for p in products:
                if p.is_in_stock():
                  # Chạy campaign giảm giá 20% cho các sản phẩm còn trong kho
                    discounted_price = p.apply_discount(20)
                    print(f"Sản phẩm {p.name} còn trong kho, giá sau khi giảm 20%: {discounted_price:,.0f}đ")
                else: 
                     print(f"Sản phẩm {p.name} đã hết hàng, không thể áp dụng giảm giá")


# Bài tập 2: Xây dựng class Customer với Encapsulation
# Xây dựng class Customer (khách hàng) với:
# • Thuộc tính public: customer_id, name
# • Thuộc tính protected: _email
# • Thuộc tính private: __password, __credit_balance (số dư tài khoản)
# • Hàm getter và setter cho __credit_balance (setter chỉ cho phép giá trị >= 0)
# • Phương thức add_credit(amount): nạp tiền vào tài khoản
# • Phương thức use_credit(amount): sử dụng tiền từ tài khoản (kiểm tra đủ số dư)
# Yêu cầu: Kiểm tra access control - đảm bảo không thể truy cập trực tiếp __password từ bên ngoài

from decimal import Decimal

class Customer:
    """ Clas Customer đại diện cho khách hàng trong hệ thống với các thuộc tính và phương thức liên quan đến thông tin cá nhân và số dư
        Quản lý tài khoản an toàn thông qua Encapsulation và Strict Typing 
    """
    def __init__(self, customer_id: int, name: str, email: str, password: str, credit_balance: float):
         # 1. Thuộc tính public
            self.customer_id = customer_id
            self.name = name
            # 2. Thuộc tính protected
            self._email = email
            # 3. Thuộc tính private
            self.__password = password
            self.__credit_balance = Decimal('0') # Khởi tạo số dư là 0, sử dụng Decimal để tránh làm tròn số

    # Đóng gói cho credit_balance với getter và setter
    @property
    def credit_balance(self) -> Decimal:
          """ Getter cho số dư tài khoản và trả về giá trị dưới dạng Decimal """
          return self.__credit_balance

    @credit_balance.setter
    def credit_balance(self, value: Decimal):
        """ Setter cho số dư tài khoản và chỉ cho phép giá trị >= 0"""
        # Type checking để đảm bảo giá trị là số thực
        if not isinstance(value,  Decimal):
            raise TypeError("Số dư tài khoản phải là kiểu Decimal, không phải kiểu khác")
        # Kiểm tra giá trị >= 0
        if value < Decimal('0'):
            raise ValueError("Số dư tài khoản phải >= 0")

        self.__credit_balance = value

    # Phương thức nạp tiền vào tài khoản

    def add_credit(self, amount: Decimal):
         """ Nạp tiền vào tài khoản, amount phải là số dương """
        # Type checking để đảm bảo amount là kiểu Decimal
         if not isinstance(amount, Decimal):
              raise TypeError("Số tiền nạp vào phải là kiểu Decimal")
        # Kiểm tra số tiền nạp vào phải là số dương 
         if amount <= 0:
                raise ValueError("Số tiền nạp vào phải là số dương") 
         
         self.__credit_balance += amount  # Tự động gọi gián tiếp qua setter để kiểm tra giá trị
         print(f"Đã nạp {amount:,.0f}đ vào tài khoản của {self.name}. Số dư hiện tại {self.__credit_balance:,.0f}đ")

    # Phương thức sử dụng tiền từ tài khoản
    def use_credit(self, amount: Decimal):
        """ Sử dụng tiền từ tài khoản, kiểm tra đủ số dư """
        # Type checking để đảm bảo amount là kiểu Decimal
        if not isinstance(amount, Decimal):
            raise TypeError("Số tiền sử dụng phải là kiểu Decimal")
        # Kiểm tra số tiền sử dụng phải là số dương 
        if amount <= 0:
            raise ValueError("Số tiền sử dụng phải là số dương") 

        if amount > self.__credit_balance:
            raise ValueError(f"Số dư không đủ. Số dư hiện tại: {self.__credit_balance:,.0f}đ")
        
        self.__credit_balance -= amount  # Tự động gọi gián tiếp qua setter để kiểm tra giá trị
        print(f"Đã sử dụng {amount:,.0f}đ từ tài khoản của {self.name}. Số dư còn lại {self.__credit_balance:,.0f}đ")

# Test case
if __name__ == "__main__":
    # Tạo một khách hàng 
    print("\n--- 1.Tạo khách hàng ---")
    cus1 = Customer(customer_id=101, name="Nguyễn Văn A", email="nguyenvana@example.com", password="password123", credit_balance=1000000)
    print(f"Khách hàng: {cus1.name}, ID: {cus1.customer_id}")
    print(f"Email (Protected): {cus1._email}")

    print("\n---2.TEST LOGIC TÀI KHOẢN (HAPPY PATH) ---")
    cus1.add_credit(Decimal('500.00'))
    cus1.use_credit(Decimal('200.00'))

    print("\n---3.TEST LOGIC TÀI KHOẢN(EGDE CASE)---")
    try:
        cus1.use_credit(Decimal('1000.00')) # Cố tình tiêu quá số dư
    except ValueError as e:
        print(e)
    try:
        cus1.add_credit(Decimal('-100.00')) # Cố tình nạp số âm
    except ValueError as e:
         print(e)

    print("\n---4.TEST ACCESS CONTROL (Encapsulation)--- ")
    # Test 4.1 test kiểu dữ liệu truyền là int thay vì là Decimal
    try: 
        cus1.credit_balance = 100 # cố tình nhập sai kiểu dữ liệu
    except TypeError as e:
        print(e)
    # Test 4.2 cố tình gắn số dư âm thông qua setter (kiểu Decimal nhưng là số âm)
    try:
         cus1.credit_balance = Decimal('-100.00') # Cố  tình gắn số âm
    except ValueError as e:
         print(e)

    # Test 4.3 thử truy cập biến Private__Password từ bên ngoài
    print("\n---Thử truy cập password từ bên ngoài---")
    print(cus1._Customer__password)
    try: 
         print(cus1.__password)
    except AttributeError:
         print("-> Mật khẩu đã được ẩn đi")

                                




 
     
     
           
            
          





      
                



                
        

        

