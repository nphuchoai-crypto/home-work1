# api/ (Tiền sảnh Presentation Layer): Nơi tiếp khách và gọi order, trả món

# endpoints.py (Lễ tân/ Bồi bàn): Nhận HTTP Request

# schemas.py (Menu/ Quy định): Ép kiểu dữ liệu trước khi truyền (Data Validation)


from pydantic import BaseModel

# Input câu 1
class ProductInput(BaseModel):
    id: int
    name: str
    stock: int
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

# Input câu 17
class TransactionInput(BaseModel):
    id: int
    amount: int
    status: str

# Input câu 18
class UserPasswordInput(BaseModel):
    id: int
    name: str
    password: str

# Input câu 19
class OrderCodeInput(BaseModel):
    order_id: int
    user_id: int
    timestamp: str

# Input (câu 22) Tìm sản phẩm giá thấp nhất
class ProductPriceInput(BaseModel):
    name: str
    price: int

# Input câu 24
class CouponInput(BaseModel):
    code: str
    coupon_list: list[str]

# Input câu 25
class ProductCategoryInput(BaseModel):
    name: str
    category: str

# Input câu 27
class NameInput(BaseModel):
    name: str

# Input câu 31
class Customer(BaseModel):
    name: str
    phone: str

class FindCustomerRequest(BaseModel):
    customers: list[Customer]
    phone: str

# Input câu 35: JSON gửi wishlist dạng mảng, Pydantic chuyển thành set.
class WishlistInput(BaseModel):
    product_id: str
    wishlist: set[str]
