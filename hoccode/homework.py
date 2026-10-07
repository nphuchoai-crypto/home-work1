
# price = 500000
# discount_percent = 0.1
# khuyen_mai = price * discount_percent
# print("Khuyến mãi:", str(khuyen_mai) + " VND")
# thanh_tien = price - khuyen_mai
# print("Thành tiền:", str(thanh_tien) + " VND")
# salary_per_day = 300000
# working_days = 22
# total_salary = salary_per_day * working_days
# print("Tổng lương:", str(total_salary) + " VND")
# distance_km = 12
# cost_per_km = 5000
# total_cost = distance_km * cost_per_km
# print("Tổng chi phí:", str(total_cost) + " VND")
 # Tính dung lượng bộ nhớ trống
# total_storage = 256
# used_storage = 180
# free_storage = total_storage - used_storage
# print("Bộ nhớ trống:", str(free_storage) + " GB")
# # Kiểm tra khả năng thanh toán 
# balance = 200000 # Số dư tài khoản 
# item_price = 150000 # Giá của mặt hàng
# if balance >= item_price:
#     print("Thanh toán thành công")
# else:
#     print("Bạn không đủ tiền trong tài khoản")

# # Điều kiện miễn phí vận chuyển
# order_value = 250000
# if order_value >= 200000:
#     print("Bạn được miễn phí vận chuyển")
# else:
#     print("Bạn không đủ điều kiện để được miễn phí vận chuyển")

# # Hệ thống phân quyền
# is_logged_in = True
# is_admin = False
# if is_logged_in:
#     if is_admin:
#         print("Chào mừng admin")
#     elif not is_admin:
#         print("Chào mừng người dùng")

# # Xây dựng hệ thống hỗ trợ khách hàng tự động
# hour = 14
# if hour < 18 and hour >= 9:
#     print("Đang trong giờ làm việc")
# else:
#     print("Không trong giờ làm việc")

# # Bạn đang validate dữ liệu từ người dùng 
# email = "user@gmail.com" 
# if "@" in email and "." in email:
#     print("Email hợp lệ")
# else:
#     print("Email không hợp lệ")

# Bạn đang viết backend cho hệ thống ecommerce
order_value = 180000
total = order_value 
if order_value >= 200000:
    print("Bạn được free ship")
elif order_value < 200000:
    phi_ship = 30000
    total = order_value + phi_ship
    print("Bạn phải thanh toán tổng cộng:", str(total) + " VND")