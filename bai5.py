# class TranslationModel:
#     # 1. Hàm khởi tạo (Constructor) để thiết lập ngôn ngữ gốc và đích
#     def __init__(self,nguon, dich):
#         self.nguon = nguon # Thuộc tính 1
#         self.dich = dich # Thuộc tính 2

#     # 2. Phương thức dịch văn bản
#     # Thêm : str để chỉ định rõ đầu vào là một chuỗi văn bản (string)
#     def dich_van_ban(self, text: str)-> str:
#         # Giả lập quá trình dịch bằng cách in ra màn hình
#         print(f"Đang dịch từ {self.nguon} sang {self.dich}...")
#         print(f"Văn bản gốc: {text}")

#         # Tạo một kết quả dịch giả lập đơn giản
#         ket_qua = f"[Bản dịch giả lập của {text}]"
#         return ket_qua

# # Hãy tạo một đối tượng cụ thể từ Class trên để dịch từ "Tiếng Anh" sang "Tiếng Việt"
# model_cua_toi = TranslationModel("Tiếng Anh", "Tiếng Việt")
# # Chạy thử hành động dịch
# ban_dich = model_cua_toi.dich_van_ban("Hello World")    
# print(ban_dich)

# 1. Định nghĩa "Bản thiết kế" (Class)

# class Car:
#     # Hàm khởi tạo các đặc điểm (thuộc tính) của xe
#     def __init__(self, thuong_hieu, mau_sac, van_toc):

#         self.thuong_hieu = thuong_hieu  # Thuộc tính 1
#         self.mau_sac = mau_sac  # Thuộc tính 2
#         self.van_toc = van_toc  # Thuộc tính 3

#     # Định nghĩa hành động (Phương thức) của xe
#     def khoi_dong(self):
#         print(f"Xe {self.thuong_hieu} màu {self.mau_sac} đang chạy trên cao tốc với tốc độ {self.van_toc}")
#     def bop_coi(self):
#         print("Píp Píp! Tránh đường nào!")

# # 2. Tạo ra các đối tượng (Object) thực tế dựa trên bản thiết kế trên
# xe_cua_Nam = Car("Vinfast", "Màu đỏ", 180)
# xe_cua_Hoai = Car("BMW", "Màu trắng", 200)

# # 3. Tạo ra các hoạt động của xe
# xe_cua_Nam.bop_coi()
# xe_cua_Hoai.khoi_dong()


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance # private
#     def deposit(self, money):
#         self.__balance += money
#     def withdraw(self, money):
#         if money <= self.__balance:
#             self.__balance -= money

#     def get_balance(self):
#         return self.__balance

# account = BankAccount(1000)
# account.deposit(500)
# print(account.get_balance())

# class UserService:
#     def create_user(self, name):
#         return {"name": name}

# class UserCLI:
#     def __init__(self, service):
#         self. service = service

#     def run(self):
#         name = input("Tên: ")
#         user = self.service.create_user(name)
#         print("Created", user)
# if __name__ == "__main__":
#     p = UserService()
#     cli = UserCLI(p)
#     cli.run()

# Dữ liệu ban đầu
data = [1, 2, 3, 4, 5]
# Xử lí tất cả trong một luồng
# Bước 1: Nhân đôi
data = [x * 2 for x in data]
# Bước 2: lọc > 5
data = [x for x in data if x > 5]
# Bước 3: chuyển sang chuỗi
data = [str(x) for x in data]
print(data)

def step_upper(data):
    return [name.upper() for name in data]
def step_filter(data):
    return [name for name in data if len(name) > 3]
def step_prefix(data):
    return ["User:" + name for name in data]

# Pipeline runner
def pipeline(data, step):
    for step in steps:
        data = step(data)
    return data

names = ["An", "Cường", "Hoài", "Anh"]
steps = [step_upper, step_filter, step_prefix]
result = pipeline(names, steps)
print(result)
