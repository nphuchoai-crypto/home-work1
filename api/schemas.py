# api/ (Tiền sảnh Presentation Layer): Nơi tiếp khách và gọi order, trả món

# endpoints.py (Lễ tân/ Bồi bàn): Nhận HTTP Request

# schemas.py (Menu/ Quy định): Ép kiểu dữ liệu trước khi truyền (Data Validation)
from pydantic import BaseModel

# Input câu 1
class ProductInput(BaseModel):
    id: int
    name: str
    sotck: int
    is_active: bool

# Input câu 2
class CartItem(BaseModel):
    name: str
    price: int
    quantity: int

# Input câu 4
class OrderStatusInput(BaseModel):
    status: str

# Input câu 13
class TotalSpentInput(BaseModel):
    total_spent: int

#  Input câu 15
class UserInput(BaseModel):
    id: int
    name: str
    is_active: bool

# Input câu 16
class Order_IDInput(BaseModel):
    id: int
