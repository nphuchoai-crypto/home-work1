# cart_total = 500
# discount = 10

# final = cart_total - cart_total * (discount/100)
# print(cart_total)
# print(discount)
# print(cart_total * (discount/100))
# print(final)

# users = [
#     {"name":"A","age": 20},
#     {"name":"B","age": 18} 
# ]
# adults = []
# for user in users:
#     print("Current User:", user)

#     if user["age"] > 18:
#         print("Adult:", user)
        
#         adults.append(user)

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# # Quy định dữ liệu của một đơn hàng.
# class OrderInput(BaseModel):
#     id: int


# # Hàm xử lý logic tìm đơn hàng mới nhất.
# def latest_order(orders: list[OrderInput]) -> OrderInput | None:
#     if not orders:
#         return None

#     latest = orders[0]

#     for order in orders:
#         if order.id > latest.id:
#             latest = order

#     return latest


# # API nhận danh sách đơn hàng và trả về kết quả.
# @app.post("/orders/latest", response_model=OrderInput | None)
# def get_latest_order(orders: list[OrderInput]):
#     return latest_order(orders)

